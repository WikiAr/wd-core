# neq - Wikidata Missing Arabic Description Finder

## Project Overview

`neq` is a Wikidata bot module that finds items missing Arabic descriptions and generates/appplies them. It queries Wikidata via SPARQL with pre-built queries for dozens of entity types, extracts Arabic labels from results, and delegates description-writing to `nep.nldesc.action_one_item()`.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `nldes3.py` | Main orchestrator - CLI parsing, SPARQL execution, item processing |
| `quarries.py` | SPARQL query builder/registry - builds `SPARQLSE` dict mapping QIDs to queries |
| `nldesc.commands.txt` | Reference file with 111 example CLI commands |

### Technologies and Dependencies

- **Python 3.10+**
- Internal: `bots_subs.wd_api.wd_sparql_bot`, `nep.nldesc`, `nep.new_way`, `nep.tables.lists`, `desc_dicts.descraptions`, `logging_config`

---

## Architecture & Code Quality Review

### Code Organization
Two-file structure: `quarries.py` builds query registry at import time; `nldes3.py` is the orchestrator. Clean separation of concerns.

### Design Patterns
- **Query Registry pattern**: `SPARQLSE` dict maps entity types to SPARQL queries
- **Builder pattern**: `do_qua()` is a parametric query builder
- **Generator pipeline**: Uses `sparql_generator_big_results` for large result sets
- **Randomized processing**: Queries shuffled randomly to distribute load

### Maintainability: 5/10
Clean two-file structure but heavy module-level side effects in `quarries.py`.

### Readability: 4/10
Unusual mutable dict pattern (`{1: value}`). Dead code. No docstrings.

### Scalability: 6/10
Generator-based pagination handles large result sets. Random shuffling distributes load.

---

## Strengths

- **Functional end-to-end**: Finds items missing Arabic descriptions and sets them
- **Query builder**: `do_qua()` reduces repetition in SPARQL construction
- **Random shuffling**: Distributes processing across entity types
- **Reference commands file**: `nldesc.commands.txt` documents all supported entity types

---

## Weaknesses

- **No error handling**: Zero try/except blocks in either file
- **Module-level side effects**: `quarries.py` checks `sys.argv` during import
- **Unusual mutable dict pattern**: `{1: value}` instead of simple variables
- **Dead code**: Unused `quaa` variable in `get_sparql_queries()`
- **No tests**: Zero test files

---

## Critical Issues

1. **Probable bug: `SPARQLSE[scdw]` overwrite** (`quarries.py` lines 117, 123): After loop over `others_list`, `scdw` retains last value. Assignments `SPARQLSE[scdw] = ...` overwrite the last item twice - likely accidental copy-paste.

2. **Probable bug: `len(pigenerator)`** (`nldes3.py` line 118): `sparql_generator_big_results` returns a generator; `len()` on a generator raises `TypeError` unless it has `__len__`.

3. **Dead code** (`nldes3.py` line 79): `quaa` variable constructed but never used.

4. **Fragile Arabic detection** (`nldes3.py` line 62): `just_get_ar()` uses absence of lowercase Latin letters as proxy for Arabic text - could misidentify other scripts.

---

## Areas That Need Attention

- **Error handling**: Add try/except for network and SPARQL failures
- **Testing**: Add pytest tests
- **Dead code**: Remove unused `quaa` variable
- **Documentation**: Add function and module docstrings

---

## Improvement Plan

### Quick Wins
- Fix `SPARQLSE[scdw]` overwrite bug
- Fix `len(pigenerator)` bug
- Remove dead `quaa` variable
- Add basic error handling

### Medium-term Improvements
- Move `quarries.py` module-level code into a function
- Replace `{1: value}` pattern with proper config
- Add type hints
- Add `argparse` for CLI

### Long-term Refactoring
- Add pytest test suite
- Extract SPARQL query templates to config files
- Implement retry logic for API calls

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 4/10 |
| **Production Readiness** | Low - no error handling, probable bugs |
| **Technical Debt** | Medium - module-level side effects, dead code |
| **Risk Assessment** | Medium - `len()` on generator crashes, overwrite bug |
| **Maintainability** | 5/10 - clean structure but poor practices |
