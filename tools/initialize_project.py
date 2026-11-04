#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-SANSEVIERIA-1.0
"""Customize the unmodified template notice for a newly created project."""
import argparse
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="OWNER/REPOSITORY, for example SANSEVIERIA-OU/my-project")
    parser.add_argument("--name", help="Project display name")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        parser.error("Use OWNER/REPOSITORY, not a URL.")
    if args.name and any(c in args.name for c in "\r\n"):
        parser.error("The project name must be one line.")
    root = Path(__file__).resolve().parents[1]
    notice = root / "NOTICE"
    text = notice.read_text(encoding="utf-8")
    if "Project: SANSEVIERIA project template\n" not in text:
        parser.error("NOTICE is already customized; edit it without overwriting component exceptions.")
    text = text.replace("Project: SANSEVIERIA project template\n",
                        f"Project: {args.name or args.repository.split('/')[1]}\n")
    text = text.replace("Official repository: https://github.com/SANSEVIERIA-OU/project-template\n",
                        f"Official repository: https://github.com/{args.repository}\n")
    notice.write_text(text, encoding="utf-8")
    print("NOTICE updated. Review its scope, third-party notices and build instructions before release.")


if __name__ == "__main__":
    main()
