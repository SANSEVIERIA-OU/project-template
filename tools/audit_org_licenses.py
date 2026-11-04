#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-SANSEVIERIA-1.0
"""Read-only audit using your local gh authentication; includes accessible private repos."""
import argparse
import base64
import hashlib
import json
import subprocess
from urllib.parse import quote

from check_license import EXPECTED_SHA256


def api(*args):
    return subprocess.run(["gh", "api", *args], text=True, capture_output=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--org", default="SANSEVIERIA-OU")
    args = parser.parse_args()
    result = api(f"orgs/{quote(args.org, safe='')}/repos?per_page=100&type=all", "--paginate", "--jq",
                 ".[] | {full_name, fork, archived, default_branch}")
    if result.returncode:
        raise SystemExit(result.stderr.strip())
    failures = 0
    for line in result.stdout.splitlines():
        repo = json.loads(line)
        name = repo["full_name"]
        if repo["fork"] or repo["archived"]:
            print(f"SKIP {name}: fork or archived repository; retain upstream terms.")
            continue
        licence = api(f"repos/{name}/contents/LICENSE?ref={quote(repo['default_branch'], safe='')}")
        if licence.returncode:
            failures += 1
            print(f"FAIL {name}: LICENSE is missing or unreadable; verify access before drawing conclusions.")
            continue
        data = json.loads(licence.stdout)
        if data.get("type") != "file" or data.get("encoding") != "base64":
            failures += 1
            print(f"FAIL {name}: LICENSE is not an ordinary readable file.")
            continue
        digest = hashlib.sha256(base64.b64decode(data["content"])).hexdigest()
        good = digest == EXPECTED_SHA256
        failures += not good
        print(f"{'PASS' if good else 'FAIL'} {name}: {'canonical licence' if good else 'different licence'}")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
