# SANSEVIERIA project template

Modello ufficiale per i nuovi progetti software di SANSEVIERIA OÜ. Include il testo integrale e invariato della **SANSEVIERIA License 1.0**, le regole per contribuire e un controllo automatico su ogni push e pull request.

La licenza è **source-available**, con reciprocità e autorizzazioni commerciali: non è una licenza approvata OSI. I componenti di terzi mantengono i propri termini. Leggere [LICENSE](LICENSE), [NOTICE](NOTICE) e [CONTRIBUTING.md](CONTRIBUTING.md).

## Creare un progetto

Su GitHub scegliere **Use this template → Create a new repository**, come proprietario `SANSEVIERIA-OU`, e la visibilità appropriata. In alternativa:

```sh
gh repo create SANSEVIERIA-OU/nome-progetto --template SANSEVIERIA-OU/project-template --private --clone
cd nome-progetto
python3 tools/initialize_project.py SANSEVIERIA-OU/nome-progetto --name "Nome progetto"
python3 tools/check_license.py --repository SANSEVIERIA-OU/nome-progetto
```

Il comando usa un repository privato come impostazione prudente per il nuovo progetto; scegliere `--public` quando si intende pubblicarlo. L'inizializzazione modifica solo l'avviso del nuovo progetto, senza cambiare la licenza comune. Rivedere il perimetro dei file, i titolari e le eccezioni per componenti di terzi, lasciando invariato il paragrafo *Acceptance* richiesto dalla sezione 9; sostituire questa guida con descrizione, build e installazione del progetto e salvare le modifiche con un commit.

Il controllo CI richiede che `NOTICE` identifichi il repository effettivo: sul nuovo progetto segnala l'avviso ancora riferito al template finché non viene inizializzato. Le nuove versioni non aggiornano automaticamente i repository già creati dal modello.

## Cosa controlla l'automazione

`tools/check_license.py` confronta `LICENSE` con l'impronta del testo aziendale 1.0 e verifica la presenza dell'avviso del progetto. Funziona senza rete, senza segreti e con permessi GitHub di sola lettura. I test includono controprove con licenza mancante, clausole alterate e avviso riferito a un altro repository.

Il controllo non è un audit di titolarità o compatibilità delle dipendenze e non applica una licenza ad altri file per magia. Non è automaticamente obbligatorio per il merge: eventuali protezioni del ramo vanno configurate secondo il piano GitHub e le regole del progetto. Chi può modificare o rimuovere il workflow può modificare anche questo controllo.

Per censire i repository accessibili dell'organizzazione, eseguire localmente con la propria autenticazione `gh`:

```sh
python3 tools/audit_org_licenses.py --org SANSEVIERIA-OU
```

Il censimento legge i rami predefiniti, include i repository privati accessibili, segnala differenze e non scrive nulla. Fork e repository archiviati sono indicati come esclusi. Non esportare credenziali personali nei workflow; il controllo per repository non ne richiede.

## Applicazione ai progetti esistenti

Aggiungere il testo comune, un `NOTICE` specifico e il controllo mediante una modifica dedicata. Conservare le eccezioni di terzi, verificare intestazioni, metadati e pacchetti ed evitare di attribuire alla società diritti che non possiede. Aggiungere il solo file radice non corregge automaticamente intestazioni o concessioni in conflitto.

GitHub non eredita `LICENSE` da un repository `.github` dell'organizzazione. Questo template è una procedura comune per i progetti che lo usano, non un'impostazione globale della piattaforma. [Documentazione GitHub](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

La licenza è una sola per tutti i progetti: le migliorie emerse da un progetto vanno nel template o in una nuova versione comune, mai in varianti per prodotto. La dichiarazione in [CONTRIBUTING.md](CONTRIBUTING.md) include il consenso alle versioni successive comuni, così i contributi possono seguire la licenza quando evolve.

I contributori conservano i propri diritti. Le autorizzazioni commerciali seguono la sezione 7 della licenza e richiedono l'autorità prevista dai titolari. Le decisioni su merge e rilasci ufficiali seguono [GOVERNANCE.md](GOVERNANCE.md); i marchi seguono [TRADEMARKS.md](TRADEMARKS.md).
