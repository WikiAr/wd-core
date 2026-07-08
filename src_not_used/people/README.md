# people - Wikidata People Description Bot

## Project Overview

`people` is a Wikidata bot module for adding multilingual descriptions to human (Q5) items. It generates descriptions by combining nationality translations with occupation translations (e.g., "Yemeni footballer" -> Arabic/Bengali/Spanish/French equivalents), with gender-aware forms. The bot queries Wikidata via SPARQL, matches items by their English description, and writes new descriptions via the API.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `new3.py` | **Main bot** - orchestrates SPARQL queries and description writing |
| `occupationsall.py` | Occupation translation tables (31KB, largest source file) |
| `people_get_topic.py` | Core data module - occupation/nationality QID mappings |
| `Nationalities.py` | Loads nationality translations from JSON |
| `add_qids.py` | Debug/utility script for QID mapping verification |
| `translationsNationalities.json` | Nationality translations (~190 countries, 12 languages) |
| `translationsOccupations.json` | Occupation translations (~80+ occupations, multiple languages) |

### Technologies and Dependencies

- **Python 3.10+**
- Internal: `bots_subs.wd_api.wd_sparql_bot`, `bots_subs.wd_api.wd_desc`, `logging_config`

---

## Architecture & Code Quality Review

### Code Organization
Data flows from JSON files through Python loader modules, gets cross-joined at runtime in `new3.py`, is used to query Wikidata via SPARQL, and written back via the API. Clean separation between data, mapping, and orchestration.

### Design Patterns
- **Template/placeholder pattern**: `~` in occupation keys replaced by nationality adjective at runtime
- **Gender-aware translations**: Separate male/female forms per language, selected by P21 claim
- **SPARQL batching**: Description lookups batched into groups of `qualimit` size
- **Mutable dict singletons**: `{1: value}` pattern for configuration values

### Maintainability: 5/10
Good data/logic separation. But significant side effects at import time and global mutable state.

### Readability: 4/10
Cryptic variable names (`kkkk`, `cccc`, `tra_occ_2`). No type hints. Mixed Arabic/English comments.

### Scalability: 6/10
SPARQL batching and random nationality sampling handle large datasets.

---

## Strengths

- **Gender-aware descriptions**: Proper male/female forms for Arabic and other languages
- **Comprehensive data**: ~190 nationalities, ~80+ occupations, 12 languages
- **SPARQL batching**: Avoids overly large `VALUES` clauses
- **JSON-based data**: Translations stored in external JSON files (easily editable)

---

## Weaknesses

- **Side effects at import time**: `new3.py` calls `make_Tabs(Tab)` and `time.sleep(1)` on import
- **`get_topic()` requires sys.argv**: Only returns value if `"returnlab"` is in `sys.argv`
- **Bug: `translations_all` no-op merge** (`occupationsall.py` line 621): Merges dict with itself
- **Side-effect print loop** (`occupationsall.py` lines 650-652): Prints on every import
- **Triple duplicate log line** (`new3.py` lines 275-277): Same message logged 3 times
- **No tests**: Zero test files

---

## Critical Issues

1. **No-op merge** (`occupationsall.py` line 621):
   ```python
   translations_all = {**translationsOccupations, **translationsOccupations}
   ```
   Second operand should be `translationsOccupations_new`.

2. **`get_topic()` unusable as library** (`people_get_topic.py`): Returns `""` unless `"returnlab"` is in `sys.argv`. Makes the function nearly useless for callers.

3. **Side-effect sleep** (`new3.py` line 69): `time.sleep(1)` at module scope on import.

4. **Empty `compare_files/` directory**: Leftover placeholder with only empty `__pycache__`.

---

## Areas That Need Attention

- **Testing**: Zero test files
- **Side effects**: Remove import-time computation and sleep
- **Bug fixes**: Fix no-op merge, duplicate log lines
- **Documentation**: Add function docstrings

---

## Improvement Plan

### Quick Wins
- Fix `translations_all` merge (use `translationsOccupations_new`)
- Remove `time.sleep(1)` from module scope
- Remove side-effect print loop from `occupationsall.py`
- Fix duplicate log lines in `new3.py`

### Medium-term Improvements
- Make `get_topic()` work without `sys.argv` dependency
- Move `make_Tabs()` call into `main()` function
- Add type hints and docstrings
- Replace `{1: value}` pattern with proper config

### Long-term Refactoring
- Add pytest test suite
- Implement proper `argparse`
- Extract cross-product logic into reusable utility
- Add error handling for JSON loading and SPARQL queries

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 5/10 |
| **Production Readiness** | Medium - functional but fragile |
| **Technical Debt** | Medium - side effects, bugs, poor naming |
| **Risk Assessment** | Medium - no-op merge loses data, import side effects |
| **Maintainability** | 5/10 - good data separation, poor code practices |
