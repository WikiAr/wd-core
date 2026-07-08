# cy - Arabic Wikipedia Cycling Race Results Bot

## Project Overview

`cy` is a Wikidata/Wikipedia bot system for Arabic Wikipedia that automatically updates cycling race result tables. It fetches cycling race results from Wikidata via SPARQL queries, parses existing Arabic Wikipedia page templates, generates updated wikitext template rows (with race names, dates, jerseys, rankings, flags), compares old vs. new data, and saves changes back to Arabic Wikipedia.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `cy6.py` | Single-page entry point |
| `jsub.py` | Batch processing entry point |
| `jsub.sh` | Toolforge job submission script |
| `mv.py` | Template mover/refactorer (moves inline templates to subpages) |
| `cy_bot/cy_api.py` | Wikipedia API client (authentication, page read/write) |
| `cy_bot/cy_sparql.py` | Wikidata SPARQL client for cycling race data |
| `cy_bot/do_text.py` | Core processing engine (705 lines) |
| `cy_bot/cy_regs.py` | Existing data parser |
| `cy_bot/cy_helps.py` | Utility/helper functions |
| `cy_bot/useraccount.py` | Dead code - unused credential reader |

### Technologies and Dependencies

- **Python 3.10+**
- **requests** - HTTP client for Wikipedia and Wikidata APIs
- **wikitextparser** (`wtp`) - Parsing MediaWiki wikitext templates
- **tqdm** - Progress bars (in `mv.py`)
- Internal: `wd_gent`, `api_page`, `logging_config`

---

## Architecture & Code Quality Review

### Code Organization
Three entry points (`cy6.py`, `jsub.py`, `mv.py`) converge on core logic in `cy_bot/do_text.py`. The `cy_bot/` sub-package separates API, SPARQL, parsing, and text generation concerns.

### Design Patterns
- **Pipeline pattern**: SPARQL query -> `fix_results` -> `fix_date` -> `make_temp_lines` -> `make_new_section` -> `do_One_Page`
- **Multiple entry points**: Single page, batch, and template refactoring modes
- **Environment-based configuration**: Credentials via env vars, test modes via `sys.argv`

### Maintainability: 4/10
`do_text.py` at 705 lines is the monolithic core with 10+ module-level mutable dicts. Heavy global state coupling.

### Readability: 3/10
Opaque variable names (`tao`, `qoo`, `faso`, `sss`). No docstrings. Mixed string formatting styles. Arabic template names throughout.

### Scalability: 5/10
Batch processing via `jsub.py` with skip lists. No connection pooling or retry logic beyond SPARQL.

---

## Strengths

- **Functional pipeline**: The SPARQL -> parse -> generate -> save pipeline works end-to-end
- **Retry logic in SPARQL**: `GetSparql()` relaxes filters and retries if initial query returns few results
- **Template refactoring**: `mv.py` can extract inline templates to transcludable subpages
- **Test mode**: `TEST[1]`/`TEST[2]` flags for debugging

---

## Weaknesses

- **Global mutable state everywhere**: 10+ module-level dicts in `do_text.py` modified by functions
- **Login at import time**: `cy_api.py` line 90 calls `login()` at module level
- **Duplicated code**: `find_cy_temp()` in both `cy_helps.py` and `mv.py`; credential reading duplicated
- **Dead code**: `useraccount.py` entirely unused; `qu_2018`, `q22u`, `_tata` never referenced
- **No docstrings**: Almost no functions have docstrings
- **Hardcoded domain logic**: Template names, property IDs, flag mappings all hardcoded

---

## Critical Issues

1. **Operator precedence bug** (`do_text.py` line 657):
   ```python
   if states[title]["new_line"] != 0 or states[title]["removed_line"] != 0 and text != NewText:
   ```
   Due to `and` binding tighter than `or`, this evaluates incorrectly. Likely intent:
   ```python
   if (new_line != 0 or removed_line != 0) and text != NewText:
   ```

2. **Duplicate p585 check** (`do_text.py` line 370):
   ```python
   date = params.get("p585") or params.get("p582") or params.get("p585") or {}
   ```
   `p585` checked twice; one should be `p580`.

3. **`HeadVars` unbounded growth** (`do_text.py`): Appended to in `make_new_section()` on every call, growing without bound across multiple page processing calls.

4. **Bare exception swallowing** (`cy_helps.py` line 143): `printo()` catches `BaseException` and silently prints empty string.

---

## Areas That Need Attention

- **Testing**: Zero test files
- **Error handling**: No try/except in main processing pipeline
- **Dead code cleanup**: Remove `useraccount.py`, unused SPARQL queries, `_tata`
- **Documentation**: No function docstrings, no architecture docs
- **Configuration**: Hardcoded template names should be in config

---

## Improvement Plan

### Quick Wins
- Fix operator precedence bug on line 657
- Fix duplicate `p585` check (change to `p580`)
- Remove dead code (`useraccount.py`, unused queries)
- Reset `HeadVars` at start of each page processing

### Medium-term Improvements
- Refactor `do_text.py` into smaller, stateless functions
- Extract global state into a processing context class
- Add error handling to the processing pipeline
- Lazy-load `cy_api` login

### Long-term Refactoring
- Add pytest test suite
- Implement proper `argparse`
- Create configuration file for template names and property IDs
- Add retry/backoff for API calls

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 4/10 |
| **Production Readiness** | Low - critical bugs, no tests, heavy global state |
| **Technical Debt** | High - 705-line monolith, 10+ global dicts, duplicated code |
| **Risk Assessment** | High - operator precedence bug causes incorrect saves, unbounded memory growth |
| **Maintainability** | 4/10 - poor naming, no docs, monolithic core |
