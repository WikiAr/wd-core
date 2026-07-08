# wd_utils - Utility Functions for JSON I/O and URL Fetching

## Project Overview

`wd_utils` is a small utility package providing JSON file I/O with time-based cache validation and remote JSON fetching from Wikidata user pages. It serves as infrastructure for the `desc_dicts` package's three-tier data loading strategy.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `__init__.py` | Empty package marker |
| `utils.py` | All utility functions (84 lines) |

### Key Functions

| Function | Purpose |
|----------|---------|
| `load_data_from_url(page_name)` | Fetches JSON from Wikidata user page |
| `get_file_date(file_path)` | Returns file modification date as YYYY-MM-DD string |
| `open_file_json(file_path)` | Reads and parses a JSON file |
| `are_dates_same(today, file_date)` | Compares two date strings for equality |
| `open_file_json_check_time(file_path)` | Reads JSON only if modified today (time-based cache) |
| `save_json_data(file_path, data)` | Serializes Python object to JSON file |

### Technologies and Dependencies

- **Python 3.10+**
- **requests** - HTTP client for URL fetching
- Standard library: `datetime`, `json`, `logging`, `os`, `pathlib`

---

## Architecture & Code Quality Review

### Code Organization
Single-file module with 6 focused functions. Easy to understand at a glance. Clear purpose and scope.

### Design Patterns
- **Time-based cache**: `open_file_json_check_time` loads only if file was modified today
- **Silent error handling**: All functions catch broad `Exception`, log, and return safe defaults
- **UTF-8 with Unicode preservation**: `ensure_ascii=False` in `json.dump` preserves Arabic text

### Maintainability: 7/10
Simple, focused functions. Good use of `pathlib`. Minor inconsistencies.

### Readability: 7/10
Clear function names (except "descraptions" typo). Good type hints on most functions.

### Scalability: 6/10
Per-call session creation is wasteful. Otherwise no scalability concerns.

---

## Strengths

- **Simple and focused**: Each function does one thing
- **Proper pathlib usage**: Type hints use `Path`, existence checks before operations
- **UTF-8 encoding**: Explicit `encoding="utf-8"` for non-ASCII content
- **Unicode preservation**: `ensure_ascii=False` in `json.dump`
- **Good test coverage**: `tests/desc_dicts/test_utils.py` covers most functions

---

## Weaknesses

- **Persistent typo**: "descraptions" in default parameter and throughout codebase
- **Per-call session creation**: `requests.session()` created on every `load_data_from_url` call
- **Mixed `print` and `logger`**: Non-200 HTTP responses use `print()` instead of `logger`
- **Broad `except Exception` everywhere**: Masks bugs, makes debugging difficult
- **`save_json_data` silently swallows errors**: No way for callers to know if write failed

---

## Critical Issues

1. **Per-call session creation** (`load_data_from_url`): Creates `requests.session()` on every call instead of reusing. Wastes TCP connection pooling.

2. **Broad exception handling**: All functions catch `Exception` indiscriminately. Code bugs (TypeError, AttributeError) are silently swallowed alongside expected errors.

3. **`save_json_data` silent failure**: Returns `None` whether it succeeds or fails. No error propagation.

---

## Areas That Need Attention

- **Session reuse**: Create module-level or injected session
- **Exception specificity**: Use `json.JSONDecodeError`, `requests.RequestException`, `OSError`
- **Test coverage**: `load_data_from_url` and `save_json_data` are not tested
- **Missing type hints**: `save_json_data`, `load_data_from_url`, `open_file_json` lack return types

---

## Improvement Plan

### Quick Wins
- Reuse `requests.Session` at module level
- Replace `print()` with `logger.warning()` for HTTP errors
- Add return type hints to `save_json_data`, `load_data_from_url`, `open_file_json`

### Medium-term Improvements
- Use specific exception types instead of broad `except Exception`
- Add return value indicating success/failure for `save_json_data`
- Add `__all__` definition to `utils.py`
- Fix `os.path.getmtime` to use `Path.stat().st_mtime`

### Long-term Refactoring
- Add pytest tests for `load_data_from_url` and `save_json_data`
- Consider adding async support for URL fetching
- Add configurable timeout parameter

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 6/10 |
| **Production Readiness** | Medium - functional but wasteful and fragile |
| **Technical Debt** | Low-Medium - small codebase, minor issues |
| **Risk Assessment** | Low - silent failures are inconvenient but not dangerous |
| **Maintainability** | 7/10 - simple, focused, well-tested |
