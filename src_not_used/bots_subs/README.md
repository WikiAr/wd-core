# bots_subs - Wikidata Bot Framework

## Project Overview

`bots_subs` is the core Wikidata bot framework for the `wd_core` project. It provides a layered abstraction for programmatically editing Wikidata items through the Wikidata API -- setting labels, descriptions, claims, aliases, qualifiers, and sitelinks. It also includes a SPARQL query engine and a direct SQL connector for querying Wikimedia database replicas.

### Main Modules and Components

| Module | Purpose |
|--------|---------|
| `hi_api/` | Authenticated Wikidata editing layer (Facade pattern) |
| `hi_api/__init__.py` | `HimoAPIBot` - main facade class |
| `hi_api/h_wd_newapi/` | Login wrapper and low-level API poster |
| `hi_api/req_bots_new/` | Domain-specific operations: claims, descriptions, labels |
| `hi_api/utils/` | Error handling, lag management, JSON response parsing |
| `wd_api/` | Older API layer: read queries, SPARQL, batch descriptions |
| `wd_api/wd_bot.py` | Wikidata entity retrieval functions |
| `wd_api/wd_sparql_bot.py` | SPARQL query engine using SPARQLWrapper |
| `wd_api/wd_desc.py` | Description-setting orchestrator |
| `wd_api/newdesc.py` | Batch description management |
| `wd_api/submit_bot.py` | Standalone API submission function |
| `open_url.py` | Simple HTTP GET utility |
| `qs_bot.py` | QuickStatements API interface |
| `wiki_sql.py` | Direct SQL connector to Wikimedia Cloud replicas |

### Technologies and Dependencies

- **Python 3.10+**
- **requests** - HTTP client for all API calls
- **pymysql** - Direct SQL to Wikimedia Cloud replicas
- **pywikibot** - Config for DB credentials; URL encoding
- **newapi** (custom) - `WikiLoginClient`, `AllAPIS` for authenticated Wikidata API access
- **SPARQLWrapper** - SPARQL queries to Wikidata Query Service
- **colorlog** - Colored console logging

---

## Architecture & Code Quality Review

### Code Organization
Well-structured with clear separation between `hi_api/` (new authenticated layer) and `wd_api/` (older read-oriented layer). The `hi_api` subsystem uses proper sub-packages for different concerns (login, operations, utils).

### Design Patterns
- **Facade Pattern**: `HimoAPIBot` unifies login, API posting, claims, labels, and descriptions
- **Inheritance**: `WdAPI` extends `WD_ERRORS_HANDLER`
- **Adapter/Wrapper**: Login adapts `newapi.AllAPIS`; `submit_bot` adapts `requests` + `pywikibot`
- **Retry with backoff**: `WdAPI.post_to_newapi()` retries on `maxlag` up to 4 times
- **Adaptive rate-limiting**: `lag_bot` polls Wikidata for replication lag and adjusts sleep times

### Maintainability: 6/10
Good structural separation. The `hi_api` facade is clean. However, heavy `sys.argv` coupling and module-level side effects reduce testability.

### Readability: 6/10
Good docstrings in `hi_api` functions with Args/Returns. Consistent logging with color markers. Some poor naming (`quary` instead of `query`).

### Scalability: 7/10
Adaptive lag management, batch SPARQL pagination, and session reuse support reasonable scale.

---

## Strengths

- **Functional completeness**: Covers labels, descriptions, claims, qualifiers, aliases, sitelinks, SPARQL, and SQL
- **Good docstrings**: Several functions have detailed Google-style docstrings
- **Consistent logging**: Uses Python's `logging` module with color-coded markers
- **Error handling**: Multiple layers with specific handling for known Wikidata API error codes
- **Lag management**: Thoughtful adaptive rate-limiting based on Wikidata replication lag
- **Facade pattern**: `HimoAPIBot` provides a clean unified interface

---

## Weaknesses

- **Hardcoded local paths**: `sys.path.append("I:/core/bots/new/newapi_bot")` in `wd_login_wrap.py`
- **Module-level side effects**: `wd_desc.py` instantiates `HimoAPIBot` at import time (triggers login)
- **Mutable default arguments**: `work_api_desc(newdesc, qid, fixlang=[])` - classic Python pitfall
- **Duplicated `ask_put()` function**: Identical function in both `descriptions_wd.py` and `labels_wd.py`
- **`sys.argv` coupling**: At least 10 different behavioral flags controlled via `sys.argv`
- **No tests**: Despite `.vscode/settings.json` enabling pytest, no test files exist

---

## Critical Issues

1. **Hardcoded Windows path** (`wd_login_wrap.py` line 9): `sys.path.append("I:/core/bots/new/newapi_bot")` breaks on any non-Windows machine.

2. **Hardcoded path in SQL guard** (`wiki_sql.py` line 26): `os.path.isdir("I:/core/bots")` for detecting SQL availability.

3. **Module-level login** (`wd_desc.py` line 19): `HimoAPIBot(mr_or_bot="bot")` at import time triggers network login.

4. **Mutable default arguments** (`wd_desc.py`, `claims_wd.py`): `fixlang=[]` and `qualifiers=[]` are shared across calls.

5. **`do_lag()` dead code** (`lag_bot.py` line 149): `GG = False` always set, making while loop execute only once.

---

## Areas That Need Attention

- **Tests**: Zero test files despite pytest configuration
- **Configuration**: Replace `sys.argv` flags with proper config object or `argparse`
- **Paths**: Remove all hardcoded local paths
- **Dependencies**: `newapi` package is not publicly available; `colorlog` not declared in requirements
- **Documentation**: Module-level docs exist but no architecture overview

---

## Improvement Plan

### Quick Wins
- Remove hardcoded paths; use relative imports or environment variables
- Fix mutable default arguments (`fixlang=None` pattern)
- Remove duplicate `ask_put()` function
- Fix `do_lag()` loop bug

### Medium-term Improvements
- Replace `sys.argv` coupling with `argparse` or config object
- Lazy-load `HimoAPIBot` (not at import time)
- Add type hints to all public functions
- Create shared constants module for magic numbers

### Long-term Refactoring
- Add comprehensive pytest suite
- Merge `hi_api` and `wd_api` into a single coherent API layer
- Implement proper dependency injection for testability
- Create proper Python package with `pyproject.toml`

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 6/10 |
| **Production Readiness** | Medium - functional but fragile, no tests |
| **Technical Debt** | Medium - two API layers, sys.argv coupling, hardcoded paths |
| **Risk Assessment** | Medium - hardcoded paths break deployment, mutable defaults cause bugs |
| **Maintainability** | 6/10 - good structure but poor testability |
