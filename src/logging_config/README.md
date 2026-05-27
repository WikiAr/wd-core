# logging_config - Colored Logging Configuration

## Project Overview

`logging_config` provides a centralized logging setup for the entire `wd_core` project. It implements custom inline color markup (`<<color>>` tags) in log messages, colored console output via `colorlog`, and optional file logging. This module is imported by all other packages in the project.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `__init__.py` | Single-file module with all functionality (201 lines) |

### Key Functions

| Function | Purpose |
|----------|---------|
| `setup_logging(name, level, log_file, propagate)` | Main entry point - configures a named logger |
| `get_color_table()` | Builds cached dict mapping color names to ANSI escape templates |
| `format_colored_text(textm)` | Parses `<<color>>` tags and applies ANSI color codes |
| `wrap_color_messages(format_message)` | Wraps logging formatter to apply inline colorization |
| `prepare_log_file(log_file, project_logger)` | Resolves log file path and creates parent directories |
| `file_logger(log_file, project_logger, numeric_level)` | Attaches plain-text FileHandler to a logger |

### Technologies and Dependencies

- **Python 3.10+**
- **colorlog** - Colored console logging (third-party, **not declared in requirements.txt**)
- **functools** - `lru_cache` for color table
- Standard library: `logging`, `os`, `re`, `sys`, `pathlib`

---

## Architecture & Code Quality Review

### Code Organization
Single-file module. All functions are tightly coupled around the logging concern. Clean public API via `setup_logging()`.

### Design Patterns
- **Facade Pattern**: `setup_logging()` encapsulates formatter, handler, and file setup
- **Caching/Memoization**: `get_color_table()` uses `@functools.lru_cache`
- **Guard Clause/Idempotency**: `setup_logging()` checks for existing handlers to prevent duplicates
- **Monkey-Patching**: `wrap_color_messages` patches `formatMessage` on formatter instance
- **Stack-based Parsing**: `format_colored_text` uses color stack for nested `<<color>>` tags

### Maintainability: 6/10
Single file is easy to understand. But fragile monkey-patching and complex regex parsing reduce maintainability.

### Readability: 5/10
Complex `format_colored_text` logic with stride-4 zip is hard to follow. Docstring says "Prints" but function returns.

### Scalability: 7/10
Caching and guard clauses prevent performance issues. Regex recompilation per call is a minor concern.

---

## Strengths

- **Idempotent setup**: Safe to call `setup_logging()` multiple times
- **Custom color markup**: `<<color>>` tags enable inline colored text in logs
- **Colored console output**: Uses `colorlog` for terminal-friendly output
- **File logging support**: Optional plain-text file handlers with `.err` suffix for warnings
- **Environment variable expansion**: Log file paths support `$VAR` and `~` expansion

---

## Weaknesses

- **Undeclared dependency**: `colorlog` not in `requirements.txt` or `pyproject.toml`
- **Monkey-patching**: Directly patches `formatter.formatMessage`, coupling to `colorlog` internals
- **Fragile parsing**: `format_colored_text` uses complex stride-4 zip on regex split results
- **No `__all__` definition**: `from logging_config import *` exports everything

---

## Critical Issues

1. **Bug: `data["light"] = 0`** (line 48): Sets value to integer `0` instead of string. Using `<<light>>` tag causes `TypeError` because `int % str` is invalid.

2. **Bug: `None` return not checked** (lines 183, 188): `prepare_log_file()` can return `None`, but `setup_logging()` calls `.with_suffix(".err")` on it, causing `AttributeError`.

3. **Bug: `file_logger` no `None` guard** (line 197): If `log_file` is `None`, `FileHandler(None)` raises `TypeError`.

4. **Bug: Fallback values use `0`** (lines 40-46): `data.get(color, 0)` returns `0` (int) for missing colors, causing `TypeError` on `cc % text`.

---

## Areas That Need Attention

- **Declare `colorlog` dependency**: Add to `requirements.txt`
- **Fix `None` handling**: Check `prepare_log_file()` return before using
- **Fix integer fallback**: Change `0` to `""` in color table aliasing
- **Performance**: Compile regex at module level instead of per-call

---

## Improvement Plan

### Quick Wins
- Fix `data["light"] = 0` to `data["light"] = ""`
- Fix `data.get(color, 0)` fallback to `data.get(color, "")`
- Add `None` check after `prepare_log_file()` call
- Add `colorlog` to `requirements.txt`

### Medium-term Improvements
- Compile `colorTagR` regex at module level
- Fix docstring mismatch ("Prints" -> "Returns")
- Add type hints to all functions
- Add `__all__` definition

### Long-term Refactoring
- Replace monkey-patching with proper logging filter
- Simplify `format_colored_text` parsing logic
- Add pytest tests for color parsing edge cases
- Consider using `rich` library instead of custom color system

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 5/10 |
| **Production Readiness** | Medium - works but has 4 bugs |
| **Technical Debt** | Medium - monkey-patching, complex parsing |
| **Risk Assessment** | Medium - `None` dereference crashes logging setup |
| **Maintainability** | 6/10 - single file, but complex internals |
