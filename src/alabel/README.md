# alabel - Wikidata Arabic Label Adder

## Project Overview

`alabel` is a single-purpose Wikidata bot module that adds Arabic labels to Wikidata items. It queries the Wikidata MySQL database for Arabic Wikipedia article items that lack an Arabic label in Wikidata, then copies the Arabic Wikipedia page title as the Wikidata Arabic label.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `__init__.py` | Package init; imports `logging_config` |
| `labels.py` | Main script: SQL query + Wikidata API label-setting |

### Technologies and Dependencies

- **Python 3.10+**
- **pymysql** (via `bots_subs.wiki_sql`) - SQL connector to Wikimedia Cloud replicas
- **requests** (via `bots_subs.hi_api`) - Wikidata API client
- Internal: `bots_subs.wiki_sql`, `bots_subs.hi_api.HimoAPIBot`, `logging_config`

---

## Architecture & Code Quality Review

### Code Organization
Minimal - a single 91-line script file. Procedural structure with global state, CLI parsing at module level, and one `main()` function.

### Design Patterns
- **Module-level side effects**: `HimoAPIBot` instantiated at import time (triggers Wikidata login)
- **Mutable container pattern**: `Limit = {1: ""}` uses dict-as-mutable-box instead of a global variable
- **Facade pattern**: `HimoAPIBot` aggregates multiple API operations behind one interface

### Maintainability: 3/10
Single file, but no abstractions, no tests, no error handling.

### Readability: 5/10
Arabic docstrings explain purpose. Code is short and linear. Variable naming is inconsistent.

### Scalability: 6/10
SQL query with configurable LIMIT handles large result sets reasonably.

---

## Strengths

- **Simple and focused**: Does one thing (add Arabic labels from sitelinks)
- **Uses `Add_Labels_if_not_there`**: Checks for existing labels before writing
- **Configurable via CLI**: Supports `-limit:` argument

---

## Weaknesses

- **No `if __name__ == "__main__"` guard**: CLI parsing runs on import
- **Module-level API login**: Import triggers network request
- **Broad exception handling**: Catches all exceptions silently
- **Inconsistent naming**: Mix of `Quaa`, `Limit`, `WD_API_Bot`, `qid`

---

## Critical Issues

1. **SQL Injection vulnerability** (line 60): Limit value from `sys.argv` is directly concatenated into SQL query without sanitization: `Quaa += f"limit {Limit[1]}"`.

2. **Missing space in SQL** (line 60): Produces `...limit 20` without space before "limit" - SQL syntax error.

3. **Potentially broken query** (line 29-30): TODO comment notes `wikidatawiki_p.wbt_item_terms` table does not exist. Query may be non-functional.

4. **`main()` never called**: No `if __name__ == "__main__": main()` block at bottom of file.

---

## Areas That Need Attention

- **Security**: SQL injection via limit parameter
- **Functionality**: Potentially broken SQL query (missing table)
- **Testing**: Zero tests
- **Documentation**: No function docstrings

---

## Improvement Plan

### Quick Wins
- Add `if __name__ == "__main__": main()` guard
- Fix SQL concatenation (add space, sanitize limit)
- Replace `except Exception` with specific exception types

### Medium-term Improvements
- Use parameterized SQL queries
- Lazy-load `HimoAPIBot` (not at import time)
- Add type hints and docstrings

### Long-term Refactoring
- Add pytest test suite
- Implement proper `argparse`
- Consider moving to the `newdesc` abstraction for consistency

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 3/10 |
| **Production Readiness** | Low - SQL injection risk, potentially broken query |
| **Technical Debt** | Medium - small codebase but multiple issues |
| **Risk Assessment** | High - SQL injection, broken query, no error handling |
| **Maintainability** | 3/10 - minimal code but no tests or guards |
