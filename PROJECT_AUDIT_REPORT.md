# wd_core Project Audit Report

**Date:** 2026-05-26
**Scope:** Full codebase audit of `src/` (12 subdirectories, ~150 Python files)
**Auditor:** Automated Code Review System

---

## Executive Summary

### Overall Purpose

`wd_core` is a **Wikidata bot framework** focused on programmatically enriching Wikidata items with Arabic-language (and multilingual) labels, descriptions, aliases, and claims. The system queries Wikidata via SPARQL, identifies items needing Arabic metadata, generates translations through lookup tables and AI (Google Gemini), and writes results back via the Wikidata API. It supports dozens of entity types including people, scientific articles, astronomical objects, geographic entities, films, books, taxa, and Wikidata properties.

### Main Technologies

| Technology | Usage |
|-----------|-------|
| Python 3.10+ | Primary language |
| requests / SPARQLWrapper | HTTP and SPARQL queries to Wikidata |
| pywikibot | Wikimedia API integration |
| pymysql | Direct SQL to Wikimedia Cloud replicas |
| wikitextparser | MediaWiki wikitext parsing |
| google.generativeai | AI-powered translation (Gemini) |
| colorlog | Colored console logging |
| tqdm | Progress bars |
| jsonlines | JSONL file I/O |

### General Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Entry Points                              │
│  si3g.py | si3g_qua.py | jsub.py | fill_ar_props.py | ...  │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│              Core Orchestrators                               │
│  nep/si3.py (P31 dispatch) | neq/nldes3.py (missing desc)   │
│  cy/do_text.py (cycling) | people/new3.py (people)           │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│           Description Generators                             │
│  nep/bots/* | des/* | WDYe/* | cy_bot/* | people/*          │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│              Data & API Layer                                │
│  bots_subs/hi_api/ (authenticated writes)                    │
│  bots_subs/wd_api/ (reads, SPARQL, batch desc)              │
│  desc_dicts/ (multilingual description data)                 │
│  wd_utils/ (JSON I/O, URL fetching)                          │
└─────────────────────────────────────────────────────────────┘
```

The system is organized as a collection of loosely coupled bot scripts sharing a common API layer (`bots_subs`), data layer (`desc_dicts`), and utility layer (`wd_utils`). Each subdirectory in `src/` handles a specific domain (people, cycling, properties, etc.) with its own entry points and domain logic.

---

## Project Health Assessment

### Overall Code Quality: 4/10

The codebase is functional but suffers from pervasive quality issues across all modules:
- Inconsistent naming conventions (mix of `snake_case`, `CamelCase`, `camelCase`, `SCREAMING_SNAKE`)
- Cryptic variable names throughout (`FFF`, `xsxsxsx`, `fafafa`, `tao`, `qoo`, `sss`)
- Persistent misspellings in identifiers (`descraptions`, `instractions`, `quary`, `lenth`)
- Massive commented-out code blocks (60% of some files)
- No type hints in the vast majority of code

### Maintainability: 4/10

- High code duplication: at least 8 pairs of near-identical files across packages
- No shared base classes or abstract interfaces
- Heavy reliance on global mutable state via `{1: value}` dict anti-pattern
- Module-level side effects (login, computation, `sys.argv` modification on import)
- Mixed Arabic/English comments reduce accessibility

### Scalability: 5/10

- SPARQL pagination and generator patterns handle large datasets
- Adaptive lag management in `bots_subs` prevents API overload
- But synchronous blocking in all batch loops limits throughput
- Per-call `requests.session()` creation wastes connection pooling
- No connection reuse or session management in most modules

### Security Posture: 3/10

- **Plaintext API key in `.env` tracked in git** (`prop_labs/`)
- SQL injection vulnerability in `alabel/labels.py`
- Bare `except BaseException` catches `SystemExit` and `KeyboardInterrupt` in 5+ files
- HTTP (not HTTPS) URLs for external site fetching in `med.py`
- SPARQL injection risk via string formatting throughout
- Placeholder User-Agent email violates Wikidata bot policy

### Production Readiness: 3/10

- Zero automated tests in 10 of 12 packages
- No CI/CD pipeline configuration
- No dependency management (`requirements.txt` incomplete, `colorlog` undeclared)
- Hardcoded Windows-specific paths (`I:/core/bots/...`) break on any other environment
- No configuration management (all config hardcoded or via `sys.argv`)
- No logging aggregation or monitoring

---

## Cross-Project Analysis

### Shared Architectural Patterns

| Pattern | Prevalence | Assessment |
|---------|-----------|------------|
| SPARQL-driven batch processing | All bot modules | Functional but no shared abstraction |
| Translation table pattern | `desc_dicts`, `WDYe`, `des`, `people` | Effective but duplicated |
| `{1: value}` mutable dict | Every package | Anti-pattern; should use config classes |
| `sys.argv` manual parsing | Every entry point | Should use `argparse` |
| Module-level side effects | 80%+ of files | Prevents testing, causes import failures |
| Facade pattern (`HimoAPIBot`) | `bots_subs` | Good design, well-implemented |

### Repeated Weaknesses

1. **`{1: value}` mutable dict pattern** - Used in every single package as a workaround for Python scoping. Found in: `alabel`, `bots_subs`, `cy`, `des`, `desc_dicts`, `nep`, `neq`, `people`, `prop_labs`.

2. **Module-level side effects** - Importing any module triggers network requests, `sys.argv` parsing, computation, or `time.sleep()`. Found in: `alabel`, `bots_subs/wd_api/wd_desc.py`, `cy/cy_bot/cy_api.py`, `des/*`, `nep/si3g.py`, `nep/si_tables.py`, `people/new3.py`, `prop_labs/gemini_bot.py`.

3. **Bare `except BaseException`** - Catches `SystemExit` and `KeyboardInterrupt`, preventing clean shutdown. Found in: `WDYe/label.py`, `WDYe/labelnumber.py`, `des/na.py`, `des/film.py`, `des/point.py`.

4. **No `if __name__ == "__main__"` guards** - Code executes at import time. Found in: `alabel/labels.py`, `WDYe/filmseries.py`, `WDYe/module.py`, `WDYe/template.py`, `WDYe/wikicategory.py`, `WDYe/d1.py`, `WDYe/street.py`, `prop_labs/openrouter.py`.

5. **Code duplication** - At least 8 file pairs are near-identical:
   - `WDYe/alias.py` / `WDYe/disam2.py`
   - `WDYe/indy.py` / `WDYe/label.py`
   - `WDYe/chem.py` / `WDYe/chem2.py`
   - `WDYe/template.py` / `WDYe/wikicategory.py`
   - `des/book.py` / `des/film.py`
   - `nep/nldesc.py` / `nep/si3.py`
   - `cy/cy_bot/cy_helps.py:find_cy_temp` / `cy/mv.py:find_cy_temp`
   - `prop_labs/openrouter.py` / `prop_labs/fill_ar_props.py`

6. **Inconsistent API usage** - Three different approaches to Wikidata API calls:
   - `HimoAPIBot` (new authenticated layer)
   - `newdesc` / `wd_bot` (older layer)
   - `pywikibot` directly

### Common Technical Debt

| Category | Count | Impact |
|----------|-------|--------|
| Dead/commented-out code | Every package | Readability, maintenance burden |
| Unused variables/functions | 20+ instances | Confusion, false dependencies |
| Misspelled identifiers | 15+ unique typos | Searchability, professionalism |
| Missing docstrings | 90%+ of functions | Onboarding, maintenance |
| Missing type hints | 95%+ of code | IDE support, bug prevention |
| Magic numbers/strings | Everywhere | Configuration flexibility |

### Dependency Issues

1. **Undeclared dependencies**: `colorlog` not in any `requirements.txt`
2. **Custom `newapi` package**: Not publicly available; hardcodes Windows path
3. **Hardcoded local paths**: `I:/core/bots/new/newapi_bot` in `wd_login_wrap.py`, `I:/core/bots` in `wiki_sql.py`
4. **Missing `.env2`**: `prop_labs/chutes.py` and `prop_labs/openrouter.py` reference non-existent file
5. **No `pyproject.toml`**: No modern Python packaging configuration

### Integration Concerns

1. **Tight coupling via `sys.argv`**: Behavioral flags propagate through import chains
2. **No shared constants**: Q-IDs, P-IDs, and language codes hardcoded as string literals everywhere
3. **Circular-ish dependencies**: `desc_dicts` depends on `wd_utils`; `nep` depends on `des`, `desc_dicts`, `people`; `neq` depends on `nep`
4. **No API versioning**: Changes to `bots_subs` break all consumers simultaneously

---

## Critical Findings

### High-Risk Issues

| # | Issue | Location | Severity |
|---|-------|----------|----------|
| 1 | **Plaintext API key in git** | `prop_labs/.env` | **CRITICAL** |
| 2 | **SQL injection** | `alabel/labels.py:60` | **CRITICAL** |
| 3 | **Operator precedence bug** | `cy/do_text.py:657` | **HIGH** |
| 4 | **Duplicate p585 check (should be p580)** | `cy/do_text.py:370` | **HIGH** |
| 5 | **Dead loop (iterates empty dict)** | `nep/si3.py:87` | **HIGH** |
| 6 | **`len()` on generator** | `neq/nldes3.py:118` | **HIGH** |
| 7 | **Trailing space in QID key** | `nep/si_tables.py:37` | **HIGH** |
| 8 | **No-op merge loses data** | `people/occupationsall.py:621` | **HIGH** |
| 9 | **`None` dereference in logging** | `logging_config:183,188` | **MEDIUM** |
| 10 | **List mutation during iteration** | `WDYe/med.py:312-318,343-349` | **MEDIUM** |

### Security Vulnerabilities

| # | Vulnerability | Location | Impact |
|---|--------------|----------|--------|
| 1 | Plaintext API key tracked in git | `prop_labs/.env` | Credential theft |
| 2 | SQL injection via `sys.argv` | `alabel/labels.py` | Database compromise |
| 3 | HTTP (not HTTPS) external URLs | `WDYe/med.py` | MITM attacks |
| 4 | SPARQL injection via string formatting | All SPARQL modules | Data exfiltration |
| 5 | Bare `except BaseException` | 5+ files | Masks security errors |
| 6 | Hardcoded credentials path | `bots_subs/hi_api/h_wd_newapi/wd_login_wrap.py` | Credential exposure |
| 7 | Placeholder User-Agent email | `prop_labs/wd_Session.py` | Policy violation |

### Performance Bottlenecks

| # | Bottleneck | Location | Impact |
|---|-----------|----------|--------|
| 1 | Per-call `requests.session()` creation | `wd_utils/utils.py`, `bots_subs/open_url.py` | No connection pooling |
| 2 | Synchronous batch loops | All bot modules | Slow throughput |
| 3 | Module-level computation on import | `nep/quarries.py` (300 lines), `people/new3.py` | Slow startup |
| 4 | Unbounded chat history | `prop_labs/gemini_bot.py` | Memory growth, context overflow |
| 5 | `HeadVars` unbounded growth | `cy/do_text.py` | Memory leak across pages |
| 6 | Regex recompiled per call | `logging_config:66` | CPU waste in hot path |

### Stability Concerns

| # | Concern | Location | Impact |
|---|---------|----------|--------|
| 1 | Import triggers network login | `bots_subs/wd_api/wd_desc.py`, `cy/cy_bot/cy_api.py` | Import failures |
| 2 | Import triggers `sys.argv` modification | `nep/si3g.py` | Breaks other modules |
| 3 | Import triggers `time.sleep(1)` | `people/new3.py` | Blocks startup |
| 4 | Mutable default arguments | `bots_subs/wd_api/wd_desc.py`, `nep/nldesc.py` | Shared state bugs |
| 5 | No retry logic in most modules | All except `bots_subs` and `prop_labs` | Transient failures crash |
| 6 | Broken JSON fallback parser | `nep/others/read_json.py:64` | Silent data corruption |

### Missing Infrastructure

| # | Missing | Impact |
|---|---------|--------|
| 1 | Automated test suite (10/12 packages) | No regression detection |
| 2 | CI/CD pipeline | No automated quality gates |
| 3 | `.gitignore` for secrets | Credential leaks |
| 4 | `requirements.txt` / `pyproject.toml` | Dependency management |
| 5 | Linting configuration (ruff/flake8) | No code style enforcement |
| 6 | Type checking (mypy) | No static analysis |
| 7 | Pre-commit hooks | No automated checks |
| 8 | Logging aggregation | No production monitoring |
| 9 | Error tracking (Sentry) | No crash reporting |
| 10 | Documentation site | No developer onboarding |

---

## Strengths

### Strong Engineering Decisions

1. **Facade pattern in `bots_subs/hi_api`**: `HimoAPIBot` provides a clean, unified interface to Wikidata editing operations. Well-structured with clear separation of concerns (claims, descriptions, labels).

2. **3-tier data loading in `desc_dicts`**: Local JSON cache -> remote URL -> hardcoded backup ensures the bot always functions, even offline. Smart resilience design.

3. **Adaptive rate-limiting in `bots_subs/hi_api/utils/lag_bot.py`**: Polls Wikidata for replication lag and dynamically adjusts sleep times. Prevents API overload without hardcoded delays.

4. **Table-driven architecture in `nep`**: Entity types mapped via QID lookup tables allow adding support for new types by adding data, not code.

5. **Gender-aware Arabic grammar**: Multiple modules properly handle masculine/feminine forms for Arabic descriptions, which is linguistically non-trivial.

### Reusable Components

| Component | Reuse | Quality |
|-----------|-------|---------|
| `bots_subs/hi_api/HimoAPIBot` | Used by 8+ packages | Good facade |
| `bots_subs/wd_api/wd_sparql_bot` | Used by 10+ packages | Solid SPARQL engine |
| `bots_subs/wd_api/newdesc` | Used by 10+ files in WDYe/des | Good batch abstraction |
| `desc_dicts/descraptions.py` | Used by 12+ packages | Well-structured data layer |
| `wd_utils/utils.py` | Used by desc_dicts + tests | Clean utility functions |
| `logging_config` | Imported by all packages | Good color logging system |

### Well-Structured Modules

- **`bots_subs/hi_api/`**: Clean sub-package structure with proper `__init__.py` exports
- **`desc_dicts/`**: Good separation of data, logic, and fallback mechanisms
- **`wd_utils/`**: Focused, single-responsibility utility module with tests
- **`nep/bots/scientific_article.py`**: Sophisticated 20+ language date formatting

---

## Improvement Roadmap

### Immediate Fixes (Week 1)

| # | Action | Files | Effort |
|---|--------|-------|--------|
| 1 | **Rotate leaked API key and add `.env` to `.gitignore`** | `prop_labs/.env`, `.gitignore` | 15 min |
| 2 | **Fix SQL injection in `alabel/labels.py`** | `alabel/labels.py:60` | 30 min |
| 3 | **Fix operator precedence bug** | `cy/do_text.py:657` | 5 min |
| 4 | **Fix duplicate p585 check** | `cy/do_text.py:370` | 5 min |
| 5 | **Fix dead loop (ggx -> gg)** | `nep/si3.py:87` | 5 min |
| 6 | **Fix `len()` on generator** | `neq/nldes3.py:118` | 5 min |
| 7 | **Fix trailing space in QID key** | `nep/si_tables.py:37` | 5 min |
| 8 | **Fix no-op merge** | `people/occupationsall.py:621` | 5 min |
| 9 | **Fix `None` dereference in logging** | `logging_config:183,188` | 15 min |
| 10 | **Fix list mutation during iteration** | `WDYe/med.py:312-318,343-349` | 30 min |

**Total estimated effort: ~2 hours**

### Short-term Improvements (Weeks 2-4)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Add `if __name__ == "__main__"` guards to all files | Prevents import side effects | 2 hours |
| 2 | Remove dead/commented-out code | Reduces confusion | 4 hours |
| 3 | Replace `except BaseException` with `except Exception` | Allows clean shutdown | 30 min |
| 4 | Change HTTP URLs to HTTPS | Security | 15 min |
| 5 | Fix mutable default arguments | Prevents shared state bugs | 1 hour |
| 6 | Create `requirements.txt` with all dependencies | Dependency management | 30 min |
| 7 | Add `.gitignore` for secrets and caches | Security | 15 min |
| 8 | Remove hardcoded Windows paths | Portability | 1 hour |
| 9 | Reuse `requests.Session` at module level | Performance | 1 hour |
| 10 | Delete abandoned files (`gemini_bot copy.py`, `useraccount.py`) | Cleanup | 15 min |

**Total estimated effort: ~11 hours**

### Medium-term Improvements (Months 1-2)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Consolidate duplicate file pairs (8 pairs identified) | Reduces maintenance by 40% | 2 days |
| 2 | Replace `{1: value}` pattern with config dataclasses | Readability, testability | 2 days |
| 3 | Implement `argparse` across all entry points | Usability, validation | 2 days |
| 4 | Extract hardcoded data dictionaries to JSON files | Maintainability | 1 day |
| 5 | Create shared constants module for Q-IDs, P-IDs, languages | Consistency | 1 day |
| 6 | Add type hints to all public functions | Bug prevention, IDE support | 3 days |
| 7 | Standardize on `HimoAPIBot` for all API calls | Consistency | 2 days |
| 8 | Add proper docstrings to all modules and functions | Onboarding | 2 days |
| 9 | Fix `lru_cache` size in `desc_dicts` | Correctness | 15 min |
| 10 | Implement proper logging (replace `print()` calls) | Observability | 1 day |

**Total estimated effort: ~16 days**

### Long-term Strategic Refactoring (Months 3-6)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Create pytest test suite for all packages | Regression prevention | 2 weeks |
| 2 | Set up CI/CD pipeline (GitHub Actions) | Automated quality gates | 2 days |
| 3 | Add ruff/flake8 linting with pre-commit hooks | Code style enforcement | 1 day |
| 4 | Add mypy type checking | Static analysis | 2 days |
| 5 | Create abstract base class for description generators | Extensibility | 1 week |
| 6 | Merge `hi_api` and `wd_api` into single coherent API | Simplification | 1 week |
| 7 | Implement async batch processing | Throughput | 1 week |
| 8 | Create formal `TranslationProvider` interface in `prop_labs` | Provider flexibility | 2 days |
| 9 | Consolidate 3 translation caches into 1 | Data consistency | 2 days |
| 10 | Create proper Python package with `pyproject.toml` | Distribution | 1 day |

**Total estimated effort: ~7 weeks**

### Security Hardening Priorities

| Priority | Action | Timeline |
|----------|--------|----------|
| **P0** | Rotate leaked Gemini API key | Immediately |
| **P0** | Add `.env` to `.gitignore` | Immediately |
| **P0** | Fix SQL injection in `alabel/labels.py` | Week 1 |
| **P1** | Change all HTTP URLs to HTTPS | Week 1 |
| **P1** | Parameterize SPARQL queries | Month 1 |
| **P1** | Replace placeholder User-Agent email | Week 1 |
| **P2** | Implement credential management (env vars or secrets manager) | Month 2 |
| **P2** | Add input validation for all `sys.argv` parsing | Month 2 |
| **P3** | Implement rate-limiting for all API calls | Month 3 |

### DevOps and Testing Recommendations

| Recommendation | Priority | Timeline |
|---------------|----------|----------|
| Create `requirements.txt` with pinned versions | High | Week 1 |
| Add `.gitignore` for `__pycache__`, `.env`, `*.pyc` | High | Week 1 |
| Set up pytest with basic smoke tests | High | Month 1 |
| Add GitHub Actions CI (lint + test) | Medium | Month 1 |
| Add pre-commit hooks (ruff, mypy) | Medium | Month 2 |
| Create Dockerfile for reproducible environment | Low | Month 3 |
| Add Sentry or similar error tracking | Low | Month 3 |
| Create developer onboarding documentation | Low | Month 3 |

---

## Shared Module Dependencies

This repo imports the following shared modules from `shared/`:

| Module | Import | Usage |
|--------|--------|-------|
| `himo_api` | `from himo_api import New_Himo_API` | Wikidata bot API (`NewHimoAPIBot`) for authenticated item editing |
| `wd_api` | `from wd_api import wd_sparql_bot` | Wikidata SPARQL queries for item discovery |
| `logging_config` | `from logging_config import setup_logging` | Colored logging with Toolforge config |
| `new_all` | `from new_all import ...` | Unified bot runner/orchestrator |
| `gent` | `from gent import ...` | Generator list utilities for page iteration |
| `likeapi` | `from likeapi import ...` | Template processing, references, encoding |

Note: `wd_core` also has its own internal `bots_subs/hi_api/` and `bots_subs/wd_api/` layers that provide Wikidata API access. The shared modules above are used for supplementary functionality and the `newapi` package (external) provides `WikiLoginClient` and `AllAPIS`.

See [`shared/`](../shared/) for module-level READMEs and architecture reviews.

---

## Final Evaluation

### Overall Project Score: 4/10

The codebase is **functional and domain-expertise-rich** but suffers from systemic quality issues that make it fragile, hard to maintain, and unsuitable for production without significant remediation.

### Risk Level: HIGH

- Leaked API key in version control
- SQL injection vulnerability
- Multiple high-severity bugs (operator precedence, dead loops, `len()` on generators)
- No automated tests to catch regressions
- Hardcoded paths prevent deployment outside development machine

### Technical Debt Level: HIGH

- ~8 pairs of duplicate files
- Pervasive global mutable state
- Module-level side effects on import
- No shared abstractions or constants
- Mixed API approaches (3 different Wikidata client patterns)
- Dead code in every package

### Estimated Production Readiness: 20%

The system works in its current development environment but:
- Cannot be deployed to production servers (hardcoded Windows paths)
- Has no monitoring or error tracking
- Has no automated quality gates
- Has known data-corruption bugs (operator precedence, list mutation)
- Has security vulnerabilities (credential leak, SQL injection)

### Recommended Next Steps

1. **Immediately** (today): Rotate the leaked API key, add `.gitignore`
2. **This week**: Fix all 10 critical/high-severity bugs listed in Immediate Fixes
3. **This month**: Add `if __name__` guards, remove dead code, create `requirements.txt`
4. **Next month**: Consolidate duplicates, add `argparse`, create pytest suite
5. **Quarter 2**: Full type hints, abstract base classes, CI/CD pipeline
6. **Quarter 3**: Async processing, proper packaging, production deployment readiness

The codebase contains significant domain knowledge about Wikidata, Arabic linguistics, and multilingual description generation. Preserving this expertise while modernizing the engineering practices should be the primary goal of any refactoring effort.
