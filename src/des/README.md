# des - Wikidata Arabic Description & Label Bot Suite

## Project Overview

`des` is a Wikidata bot suite focused on adding Arabic (and multi-language) descriptions and labels to Wikidata items across dozens of entity categories. It automates: adding missing Arabic descriptions to geographic entities, books, films, galaxies, railways, and more; adding missing Arabic labels based on English labels; and transliterating Cyrillic labels to Latin script.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `desc.py` | Main orchestrator for geographic/organizational descriptions |
| `book.py` | Descriptions for books/stories ("{type} by {author}") |
| `film.py` | Descriptions for films ("film from {year}, directed by {director}") |
| `fam.py` | Generic description-adder for multiple entity types |
| `p155.py` | Arabic label-creation for sports events (P155/P156) |
| `na.py` | Label-naming from Wikimedia category names |
| `railway.py` | Descriptions for railway stations/lines |
| `ru_st_2_latin.py` | Cyrillic-to-Latin transliteration for Russian/Serbian |
| `galaxy.py` | Descriptions for galaxies |
| `numb.py` | Arabic description for prime numbers |
| `point.py` | P585 (point in time) claims for sports events |
| `contries2.py` | Country name lookup table (~190 countries) |
| `p155tables.py` | Sports term translation tables (80KB, largest file) |
| `places.py` | Place type lookup table (~200 QIDs) |

### Technologies and Dependencies

- **Python 3.10+**
- **pywikibot** - Wikimedia Python library (in `film.py`, `ru_st_2_latin.py`)
- **tqdm** - Progress bars (in `fam.py`)
- Internal: `bots_subs.hi_api.HimoAPIBot`, `bots_subs.wd_api.*`, `bots_subs.qs_bot`, `desc_dicts.descraptions`, `api_page`

---

## Architecture & Code Quality Review

### Code Organization
Flat script-per-entity-type structure. Each file handles one domain (books, films, railways, etc.). Data files (`contries2.py`, `p155tables.py`, `places.py`) are co-located with logic files.

### Design Patterns
- **Mutable dict as mutable scalar**: `{1: value}` pattern used throughout instead of `global` keyword
- **CLI via sys.argv**: Manual `arg.partition(":")` parsing instead of `argparse`
- **Template-method for SPARQL**: Query strings built as templates with `%s` or `.replace()`
- **Random sampling**: `fam.py` randomly selects 10 entity types per run
- **QuickStatements batching**: `desc.py` can batch descriptions into QuickStatements

### Maintainability: 4/10
Significant code duplication between `book.py` and `film.py`. Inconsistent naming. No shared abstractions.

### Readability: 4/10
Misspelled identifiers (`DescraptionsTable`, `lenth`). No type hints. Minimal docstrings. Arabic comments inaccessible to non-Arabic readers.

### Scalability: 5/10
SPARQL pagination supports large result sets. But per-item API calls with no batching limit throughput.

---

## Strengths

- **Comprehensive entity coverage**: Handles 30+ entity types across geographic, cultural, and scientific domains
- **Multilingual support**: Many files support 10-40+ languages per description
- **QuickStatements integration**: Can batch edits via QuickStatements for efficiency
- **Resilient data loading**: 3-tier fallback (JSON -> URL -> hardcoded) in description dictionaries

---

## Weaknesses

- **Massive code duplication**: `book.py`/`film.py` share nearly identical `MakeDesc()`, `Gquery2()`, `one_*_item()` patterns
- **Misspelled identifiers**: `DescraptionsTable`, `Qid_Descraptions`, `Space_Descraptions`, `lenth`
- **Module-level side effects**: Multiple files execute queries at import time
- **Bare `except BaseException`**: Used in `na.py`, `film.py`, `point.py`
- **Inconsistent API usage**: `film.py` uses `pywikibot.ItemPage` while others use custom `wd_bot`
- **Hardcoded data**: `p155tables.py` is 80KB of inline dictionaries

---

## Critical Issues

1. **Bare `except BaseException`** (`na.py` line 31, `film.py` line 84, `point.py` line 31): Catches `SystemExit` and `KeyboardInterrupt`.

2. **Unused variables** (`book.py` line 291): `keys = ["ar"]` overwrites computed keys, making preceding loop pointless.

3. **Potential off-by-one** (`fam.py` line 136): `num += 1` after `enumerate(json1, start=1)` makes counter start at 2.

4. **Protein in places table** (`places.py` line 339): `placesTable["Q8054"] = {"ar": "بروتين"}` (protein) is semantically wrong for a "places" table.

5. **Inconsistent translations** (`film.py`): Uses `pywikibot.ItemPage` directly, creating unnecessary dependency.

---

## Areas That Need Attention

- **Testing**: Zero test files
- **Code duplication**: Extract shared `MakeDesc`, `Gquery2`, `one_item` patterns
- **Naming**: Fix persistent "descraptions" typo
- **Dead code**: Remove commented-out blocks in `book.py`, `film.py`, `desc.py`
- **Configuration**: Extract Q-IDs, P-IDs, and language codes to constants

---

## Improvement Plan

### Quick Wins
- Replace `except BaseException` with `except Exception`
- Fix `keys = ["ar"]` override bug in `book.py`
- Remove dead/commented-out code
- Fix off-by-one in `fam.py`

### Medium-term Improvements
- Consolidate `book.py`/`film.py` into shared description generator
- Extract `p155tables.py` data to JSON files
- Add type hints and docstrings
- Standardize on one API approach

### Long-term Refactoring
- Create abstract base class for entity-type description generators
- Add pytest test suite
- Implement proper `argparse` across all modules
- Create centralized constants module for Q-IDs and P-IDs

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 4/10 |
| **Production Readiness** | Low - no tests, significant bugs, high duplication |
| **Technical Debt** | High - 80KB data files inline, massive duplication |
| **Risk Assessment** | Medium - bare excepts mask errors, off-by-one in pagination |
| **Maintainability** | 4/10 - poor naming, high duplication, no abstractions |
