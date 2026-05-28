# desc_dicts - Wikidata Multilingual Description Data Layer

## Project Overview

`desc_dicts` is the centralized data layer for the `wd_core` Wikidata bot. It stores and serves all multilingual description text used by the bot, organized by Wikidata entity type (QID). The package provides a resilient 3-tier data loading strategy (local JSON cache -> remote Wikidata URL -> hardcoded Python backup) to ensure the bot always has access to description data.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `descraptions.py` | **Main entry point** - Facade/aggregator that exports all description dictionaries |
| `descraptions_dict.py` | Core hardcoded data file (62KB, ~1480 lines of multilingual dictionaries) |
| `descraptions_dict_new.py` | Dynamic data loader with 3-tier fallback (JSON -> URL -> hardcoded) |
| `taxones.py` | Biological taxonomy translation tables (142 taxa, 64 rank prefixes) |
| `tiny_wrwr.py` | Small description dictionary (~89 QIDs) |
| `descraptions.json` | Cached JSON data from Wikidata (49KB) |
| `replace_descraptions.json` | Description correction rules (564B) |

### Technologies and Dependencies

- **Python 3.10+**
- **requests** (via `wd_utils.utils`) - Fetching JSON from Wikidata
- **functools** - `lru_cache` for data loading
- Internal: `wd_utils.utils`, `logging_config`

---

## Architecture & Code Quality Review

### Code Organization
Clean separation between data files (`descraptions_dict.py`, `taxones.py`) and logic (`descraptions_dict_new.py`, `descraptions.py`). The facade pattern in `descraptions.py` provides a single import point for the entire codebase.

### Design Patterns
- **Facade Pattern**: `descraptions.py` aggregates data from multiple sources behind clean exports
- **Strategy/Chain of Responsibility**: `get_data()` tries local JSON -> remote URL -> hardcoded backup
- **Caching**: `@functools.lru_cache(maxsize=1)` on `get_data()`
- **Pure Data Module**: `descraptions_dict.py`, `taxones.py`, `tiny_wrwr.py` contain no logic

### Maintainability: 6/10
Good separation of data and logic. Well-structured fallback system. But 62KB inline data file and persistent typos reduce maintainability.

### Readability: 5/10
Inline comments reference Wikidata discussion topics (good traceability). But misspelled identifiers throughout ("descraptions").

### Scalability: 7/10
JSON-based data loading with URL fallback scales well. Cache prevents repeated fetches.

---

## Strengths

- **Resilient 3-tier data loading**: Always functional even without network access
- **Comprehensive multilingual coverage**: 100+ languages for some entities
- **Community traceability**: Inline comments link to Wikidata discussion topics
- **Clean facade**: Single import point (`from desc_dicts.descraptions import DescraptionsTable`)
- **Good test coverage**: `wd_utils.utils` functions have pytest tests

---

## Weaknesses

- **Persistent typo**: "descraptions" used everywhere instead of "descriptions"
- **Debug code in production** (`tiny_wrwr.py` lines 92-94): `for ps in tiny_wrwr: if ps in Qid_Desc: print(ps)` runs at import time
- **Malformed QID key**: `Q1013520000000000000000000000000000` in `descraptions_dict.py` (should be `Q1013520`)
- **`lru_cache` size mismatch**: `maxsize=1` is too small for 2 distinct arguments
- **62KB monolithic data file**: `descraptions_dict.py` could be split or replaced by JSON

---

## Critical Issues

1. **Malformed QID key** (`descraptions_dict.py` line 135): `Q1013520000000000000000000000000000` is clearly a data error. Comment confirms intent is `Q1013520`.

2. **Debug code at import time** (`tiny_wrwr.py` lines 92-94): Prints to stdout on every import.

3. **Cache thrashing** (`descraptions_dict_new.py`): `maxsize=1` means alternating calls to `get_data("descraptions")` and `get_data("replace_descraptions")` evict each other.

---

## Areas That Need Attention

- **Fix malformed QID key**: Change `Q1013520000000000000000000000000000` to `Q1013520`
- **Remove debug code**: Wrap `tiny_wrwr.py` loop in `if __name__ == "__main__"`
- **Fix cache size**: Change `maxsize=1` to `maxsize=2` or `maxsize=None`
- **Consider splitting**: 62KB data file could be split by domain

---

## Improvement Plan

### Quick Wins
- Fix malformed QID key
- Remove debug code from `tiny_wrwr.py`
- Fix `lru_cache` maxsize to 2
- Fix commented-out `Path` import in `__init__.py`

### Medium-term Improvements
- Split `descraptions_dict.py` into domain-specific files
- Add type hints to exported dictionaries
- Move JSON files to a dedicated data directory
- Fix "descraptions" typo in variable names (breaking change)

### Long-term Refactoring
- Replace 62KB Python data file entirely with JSON
- Add validation for JSON data integrity
- Implement proper caching with TTL instead of date-check
- Add comprehensive tests for data loading fallback chain

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 6/10 |
| **Production Readiness** | Medium - functional with good fallback, but data errors |
| **Technical Debt** | Medium - misspellings, debug code, large inline data |
| **Risk Assessment** | Low-Medium - malformed QID causes silent data loss |
| **Maintainability** | 6/10 - good architecture, poor naming |
