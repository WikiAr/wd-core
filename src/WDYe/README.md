# WDYe - Wikidata Arabic Label & Description Bot Scripts

## Project Overview

WDYe is a collection of Wikidata bot scripts focused on enriching Wikidata items with Arabic (and sometimes multilingual) labels, aliases, and descriptions. The package runs SPARQL queries against the Wikidata Query Service to identify items needing Arabic labels/descriptions, then writes them via a custom API layer.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `common.py` | Main bulk description-adding script for many entity types (names, years, categories, etc.) |
| `med.py` | Arabic medical term labels/aliases from external medical dictionaries |
| `street.py` | Dutch street descriptions for ~400 Netherlands municipalities |
| `label.py` | Arabic labels from Arabic Wikipedia sitelinks |
| `indy.py` | Arabic labels from Arabic Wikipedia sitelinks (standalone pywikibot version) |
| `catwithoutp31.py` | Adds P31=Q4167836 to category items missing classification |
| `category.py` | Copies Arabic labels to Wikidata category items |
| `ali.py` | Arabic aliases for "Abdul" name patterns |
| `alias.py` | Fixes Persian disambiguation page descriptions |
| `disam2.py` | Fixes Persian disambiguation descriptions (Quarry variant) |
| `chem.py` / `chem2.py` | Fixes beetle/insect species descriptions |
| `filmseries.py` | Arabic descriptions for film series items |
| `labelnumber.py` | Converts Indic numerals to Western Arabic numerals in labels |
| `module.py` / `template.py` / `wikicategory.py` | Descriptions for Wikimedia modules/templates/categories |
| `month.py` | Arabic descriptions for month/island items |
| `d.py` / `d1.py` | Description-adding via SPARQL queries |

### Technologies and Dependencies

- **Python 3.10+**
- **pywikibot** - Wikimedia Python library (used in `indy.py`, `label.py`, `labelnumber.py`)
- **requests** - HTTP client (via `bots_subs.open_url`)
- **wikitextparser** - MediaWiki wikitext parsing
- Internal: `bots_subs.hi_api.HimoAPIBot`, `bots_subs.wd_api.*`, `desc_dicts.descraptions`, `logging_config`

---

## Architecture & Code Quality Review

### Code Organization
The package follows a flat script-per-task structure. Each file handles one entity type or task. There are no subdirectories, no shared base classes, and minimal abstraction between files.

### Design Patterns
- **SPARQL-driven batch processing**: Query -> iterate -> edit (dominant pattern)
- **Translation table pattern**: Most files define `translations` dicts mapping English to Arabic
- **Two API layers**: Some files use `HimoAPIBot` directly, others use `newdesc` abstraction, some use `pywikibot` directly

### Maintainability: 4/10
Significant code duplication (`alias.py`/`disam2.py`, `indy.py`/`label.py`, `chem.py`/`chem2.py`, `template.py`/`wikicategory.py`). Inconsistent coding styles across files. No shared utilities or base classes.

### Readability: 4/10
Poor variable names (`FFF`, `xsxsxsx`, `fafafa`, `mam`, `quuu`). Mixed Arabic/English comments. No docstrings on functions. Massive commented-out code blocks (~60% of `common.py`).

### Scalability: 5/10
The SPARQL batch processing pattern scales reasonably, but hardcoded data dictionaries (400+ entries in `street.py`) and lack of database-backed storage limit flexibility.

---

## Strengths

- **Comprehensive entity coverage**: Handles dozens of Wikidata entity types
- **Reusable `newdesc` abstraction**: The most common pattern (SPARQL -> set descriptions) is well-abstracted in `bots_subs.wd_api.newdesc`
- **Consistent Arabic docstrings**: Module-level docstrings describe each script's purpose
- **Interactive/automatic toggle**: Several scripts support both interactive and batch modes

---

## Weaknesses

- **Massive code duplication**: At least 4 pairs of near-identical files
- **Inconsistent API usage**: Three different approaches (`HimoAPIBot`, `newdesc`, `pywikibot`)
- **No `if __name__ == "__main__"` guards**: Many files execute at import time
- **Dead code everywhere**: Unused functions, commented-out blocks, unused imports
- **Hardcoded data**: `street.py` has 400+ municipality entries inline; `ali.py` has 60+ QIDs inline

---

## Critical Issues

1. **List mutation during iteration** (`med.py` lines 312-318, 343-349): `Item_tab.remove(alia)` inside `for alia in Item_tab` causes elements to be skipped.

2. **Bare `except BaseException`** (`label.py`, `labelnumber.py`): Catches `SystemExit` and `KeyboardInterrupt`, preventing clean shutdown.

3. **HTTP (not HTTPS) URLs** (`med.py`): External medical dictionary sites are fetched over insecure HTTP.

4. **Fragile HTML parsing** (`med.py`): Regex-based HTML scraping will break on any website markup change.

5. **Shadowing builtins**: `template.py` and `wikicategory.py` shadow `list`; `labelnumber.py` shadows `max`.

6. **SPARQL injection risk**: Queries built via string formatting rather than parameterized queries.

---

## Areas That Need Attention

- **Missing tests**: Zero test files in the entire package
- **No shared utility module**: Common patterns should be extracted
- **Stale `__init__.py`**: Logging setup is commented out and references unimported `Path`
- **No dependency management**: No `requirements.txt` or `pyproject.toml` specific to this package
- **Configuration management**: All config is hardcoded; no external config files

---

## Improvement Plan

### Quick Wins
- Add `if __name__ == "__main__"` guards to all files
- Remove dead/commented-out code
- Fix list mutation bugs in `med.py`
- Change HTTP URLs to HTTPS in `med.py`
- Replace `except BaseException` with `except Exception`

### Medium-term Improvements
- Consolidate duplicate files (`alias.py`/`disam2.py`, `indy.py`/`label.py`, etc.)
- Extract hardcoded data dictionaries to JSON/data files
- Create a shared base module for common patterns
- Add proper docstrings and type hints
- Standardize on one API approach (`HimoAPIBot` or `newdesc`)

### Long-term Refactoring
- Implement proper `argparse` for all CLI interfaces
- Add comprehensive test suite with pytest
- Create a plugin/registry architecture for entity type handlers
- Implement proper error handling and retry logic
- Add configuration management (YAML/TOML config files)

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 4/10 |
| **Production Readiness** | Low - functional but fragile, no tests, many bugs |
| **Technical Debt** | High - massive code duplication, dead code, inconsistent patterns |
| **Risk Assessment** | Medium-High - list mutation bugs, bare excepts, SPARQL injection risk |
| **Maintainability** | 4/10 - poor naming, no abstractions, high duplication |
