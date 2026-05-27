# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Wikidata bot framework focused on programmatically enriching Wikidata items with Arabic-language (and multilingual) labels, descriptions, aliases, and claims. Queries Wikidata via SPARQL, identifies items needing Arabic metadata, generates translations through lookup tables and AI (Google Gemini), and writes results back via the Wikidata API. Supports dozens of entity types: people, scientific articles, astronomical objects, geographic entities, films, books, taxa, and Wikidata properties.

## Commands

### Run Tests

```bash
pytest                    # All tests (network disabled by default)
pytest -m unit            # Unit tests only
pytest -m all             # All tests including slow ones
pytest -k "test_name"     # Single test by name
```

`pytest.ini` sets `testpaths = tests`, `pythonpath = .`, `--maxfail=25`, `--durations=10`, `--strict-markers`. Network sockets disabled by autouse fixture in `conftest.py`.

### Lint & Format

```bash
ruff check src/           # Lint
ruff check --fix src/     # Lint with auto-fix
ruff format src/          # Format
black src/                # Format (alternative)
isort src/                # Sort imports
mypy src/                 # Type check
```

Line length is 120 across all tools. Target Python 3.13.

Pre-commit hooks configured (pyupgrade, bandit, mypy, yesqa, standard hooks).

### Install Dependencies

```bash
pip install -r requirements.txt       # Runtime
pip install -r dev-requirements.txt   # Testing
```

Runtime: `PyMySQL`, `Requests`, `SPARQLWrapper`, `wikitextparser`, `python-dotenv`, `tqdm`.
Dev: `pytest`, `pytest-mock`, `pytest-cov`, `pytest-socket`.

## Architecture

```
Layer 1: Entry Points
  si3g.py | si3g_qua.py | jsub.py | fill_ar_props.py | fam.py | new3.py | labels.py

Layer 2: Core Orchestrators
  nep/si3.py (P31 dispatch) | neq/nldes3.py (missing desc) | cy/do_text.py (cycling) | people/new3.py

Layer 3: Description Generators
  nep/bots/* | des/* | WDYe/* | cy_bot/* | people/*

Layer 4: Data & API Layer
  bots_subs/hi_api/  (authenticated writes via HimoAPIBot facade)
  bots_subs/wd_api/  (reads, SPARQL, batch descriptions)
  desc_dicts/         (multilingual description data)
  wd_utils/           (JSON I/O, URL fetching)
  logging_config/     (centralized colored logging)
```

### Key Abstractions

- **`HimoAPIBot`** (`bots_subs/hi_api/__init__.py`) -- Facade class unifying login, API posting, claims, labels, and descriptions. Used by 8+ packages.
- **`WdAPI`** (`bots_subs/hi_api/h_wd_newapi/wd_newapi_bot.py`) -- Low-level authenticated API poster with retry logic.
- **`wd_sparql_bot`** (`bots_subs/wd_api/wd_sparql_bot.py`) -- SPARQL query engine using SPARQLWrapper.
- **`newdesc`** (`bots_subs/wd_api/newdesc.py`) -- Batch description management.
- **`DescraptionsTable`** (`desc_dicts/descraptions.py`) -- Facade aggregating all multilingual description dictionaries.
- **`setup_logging()`** (`logging_config/__init__.py`) -- Centralized logging with inline `<<color>>` markup.

### Key Modules

- **`src/nep/`** -- Main description bot framework. `si3.py` dispatches by P31 type, `si3g.py` and `si3g_qua.py` are entry points.
- **`src/neq/`** -- Missing Arabic description finder via SPARQL.
- **`src/des/`** -- Arabic description & label bot suite (geographic, books, films, railways, sports).
- **`src/WDYe/`** -- Wikidata label & description bot scripts (bulk, medical terms, streets, sitelinks).
- **`src/people/`** -- People (Q5) description bot with occupation/nationality tables.
- **`src/cy/`** -- Arabic Wikipedia cycling race results bot.
- **`src/prop_labs/`** -- Property Arabic translation bot using Google Gemini AI.
- **`src/alabel/`** -- Arabic label adder from sitelinks.
- **`src/desc_dicts/`** -- Multilingual description data layer (62KB+ of hardcoded translation tables).
- **`src/bots_subs/wiki_sql.py`** -- SQL connector to Wikimedia Cloud replicas.
- **`src/bots_subs/qs_bot.py`** -- QuickStatements API interface.

### Entry Points

```bash
python3 core8/pwb.py nep/si3g -newpages:200              # Add descriptions to new items
python3 core8/pwb.py nep/si3g_qua                         # SPARQL-based people descriptions
python3 core8/pwb.py neq/nldes3 a2r sparql:Q482994        # Find missing Arabic descriptions
python3 core8/pwb.py wd_gent -mynewpages:10 -ns:0         # Pywikibot generator entry
```

Some entry points run directly (not via pwb.py):
```bash
python3 src/des/fam.py                  # Generic description adder
python3 src/people/new3.py              # People description bot
python3 src/alabel/labels.py            # Arabic labels from sitelinks
python3 src/prop_labs/fill_ar_props.py  # AI-powered property translation
```

CLI arguments use `arg.partition(":")` pattern (no argparse).

### Patterns to Know

- **SPARQL-driven batch processing** -- Query -> iterate -> edit (every package).
- **`{1: value}` mutable dict pattern** -- used instead of `global` keyword everywhere.
- **Module-level side effects** -- importing modules triggers login, computation, or sys.argv modification.
- **Mixed Arabic/English** in comments, variable names, and string literals.
- **Data-as-code** -- Large Python files that are essentially translation dictionaries (31KB+ in `occupationsall.py`, 80KB+ in `p155tables.py`).

## Environment

Bot credentials from environment variables:
- `WIKIPEDIA_BOT_USERNAME` / `WIKIPEDIA_BOT_PASSWORD` -- primary bot account
- `WIKIPEDIA_HIMO_USERNAME` / `WIKIPEDIA_HIMO_PASSWORD` -- alternate account

The `newapi` package (at `I:/core/bots/new/newapi_bot`) provides `WikiLoginClient` and `AllAPIS` for authenticated Wikimedia API access.

## Deployment

Deployed to Wikimedia Toolforge. GitHub Actions workflow (`deploy.yml`) SSHs to server on push to `main` and runs `shs/update_wd.sh`. CI (`pytest.yml`) runs tests on PRs using Python 3.13.
