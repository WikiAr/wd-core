# nep - Wikidata Arabic Description Bot Framework

## Project Overview

`nep` is the main Wikidata description bot framework for the `wd_core` project. It automatically generates and adds Arabic-language (and sometimes multi-language) descriptions to Wikidata items. The bot fetches items via SPARQL or generators, determines their type (P31), and dispatches to specialized description generators for people, taxa, scientific articles, astronomical objects, geographic entities, films, books, and more.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `si3.py` | **Core engine** - Central orchestrator dispatching by P31 type |
| `si3g.py` | Generator-based runner (newpages, usercontribs, file, page sources) |
| `si3g_qua.py` | SPARQL-based people description runner |
| `nldesc.py` | Legacy Dutch/Arabic description generator |
| `space_others.py` | Space & geographic entity descriptions |
| `new_way.py` | P1433 (published in) article type descriptions |
| `work_new.py` | Range-based runner (process by Q-number range) |
| `wr_people.py` | People (Q5) description generator |
| `bots/helps.py` | Utility functions (API wrappers, caching, label lookup) |
| `bots/its.py` | Item type-specific description builders (~15 functions) |
| `bots/scientific_article.py` | Scientific article descriptions (20+ languages) |
| `bots/tax_desc.py` | Biological taxon description generator |
| `tables/lists.py` | Entity type lists and categorizations |
| `tables/nats.py` | Nationality adjective tables (~200 countries) |
| `tables/cash.py` | Pre-populated label cache (92 constellations) |
| `tables/si_tables.py` | Configuration tables and flags |
| `tables/str_descs.py` | Structured description tables (Dutch legacy) |
| `others/read_json.py` | JSON file reader with fallback parsing |
| `others/read_np.py` | New types analyzer |
| `tests/test_si3.py` | Manual test harness (not pytest) |

### Technologies and Dependencies

- **Python 3.10+**
- **python-dateutil** - Date parsing
- Internal: `bots_subs.wd_api.*`, `bots_subs.hi_api`, `des.*`, `desc_dicts.*`, `people.*`, `logging_config`, `api_page`, `wd_gent`

---

## Architecture & Code Quality Review

### Code Organization
Well-structured with clear separation: entry points (`si3g.py`, `si3g_qua.py`, `work_new.py`), core engine (`si3.py`), specialized generators (`bots/`), data tables (`tables/`), and utilities (`others/`).

### Design Patterns
- **Strategy Pattern (implicit)**: `ISRE()` dispatches to different generators based on P31 value
- **Table-Driven Design**: Lookup tables map QIDs to labels, properties, and metadata
- **Caching**: `Get_label()` in `helps.py` implements in-memory label cache
- **Fallback Chain**: Try specific description first, then generic patterns, then skip

### Maintainability: 5/10
Good structural separation but heavy code duplication between `nldesc.py` and `si3.py`. Global mutable state throughout.

### Readability: 4/10
Cryptic variable names (`wdi`, `gg`, `sasa`, `Faso`). No function docstrings. Mixed Arabic/English comments. Placeholder docstrings.

### Scalability: 6/10
SPARQL pagination and generator patterns support large datasets. In-memory caching reduces API calls.

---

## Strengths

- **Comprehensive entity coverage**: Handles 50+ entity types through table-driven dispatch
- **Gender-aware Arabic grammar**: Different prepositions for masculine/feminine nouns
- **Scientific article support**: 20+ language descriptions with localized date formats
- **New type tracking**: Automatically logs unrecognized P31 types for future support
- **Multiple entry points**: Generator, SPARQL, range-based, and test modes

---

## Weaknesses

- **Heavy code duplication**: `nldesc.py` duplicates `si3.py` dispatch logic; `lng_canbeused` defined in two files
- **Global mutable state**: `new_types`, `MainTestTable`, `offsetbg`, `labels_cach` modified across modules
- **Side effects at import time**: `si3g.py` modifies `sys.argv`; `si_tables.py` parses `sys.argv` on import
- **No automated tests**: `test_si3.py` is a manual harness, not pytest
- **Inconsistent naming**: Mix of `snake_case`, `CamelCase`, `camelCase`
- **Legacy Dutch code**: `str_descs.py` and `nldesc.py` contain Dutch-language remnants

---

## Critical Issues

1. **Dead loop** (`si3.py` line 87): `for ggx in ggx.keys()` iterates over `{}` (empty dict) - loop body never executes. Should be `gg.keys()`.

2. **Trailing space in QID key** (`si_tables.py` line 37): `"Q13442814 "` has trailing space, causing lookups to fail.

3. **Mutable default argument** (`nldesc.py`): `action_one_item(lngr, q, item={}, claimstr="")` - classic Python anti-pattern.

4. **`sys.argv` modification at import** (`si3g.py` lines 63-64): `sys.argv.append("-family:wikidata")` is a dangerous side effect.

5. **Broken JSON fallback** (`others/read_json.py` line 64): `fa = f"{{fa}}"` creates literal string `{fa}` instead of reconstructing JSON.

---

## Areas That Need Attention

- **Testing**: Replace manual test harness with pytest
- **Code duplication**: Consolidate `nldesc.py` and `si3.py`
- **Global state**: Refactor into context objects or config classes
- **Dead code**: Remove commented-out blocks, unused imports
- **Documentation**: Add function docstrings

---

## Improvement Plan

### Quick Wins
- Fix `ggx` iteration bug (change to `gg`)
- Fix trailing space in QID key
- Fix mutable default argument
- Remove `sys.argv.append` from import-time code

### Medium-term Improvements
- Consolidate `nldesc.py` into `si3.py` (remove duplication)
- Refactor global state into context/config classes
- Add proper `argparse` to all entry points
- Add type hints to public functions

### Long-term Refactoring
- Create abstract base class for description generators
- Add comprehensive pytest suite
- Implement proper dependency injection
- Extract all data tables to JSON files
- Remove legacy Dutch code

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 5/10 |
| **Production Readiness** | Medium - functional but fragile |
| **Technical Debt** | High - duplication, global state, legacy code |
| **Risk Assessment** | Medium - dead loop bug, trailing space key, sys.argv mutation |
| **Maintainability** | 5/10 - good structure but poor naming and duplication |
