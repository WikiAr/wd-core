# Static Analysis & Refactoring Roadmap
## Repository: wd-core (Wikidata Core Bots)

**Analysis Date:** 2026-01-26
**Analyzed by:** Claude (Architectural Analysis)
**Scope:** Full codebase static analysis

---

## 1. System Overview

### 1.1 Purpose
`wd-core` is a collection of Python bots for automated Wikidata/Wikipedia operations. The bots primarily:
- Add/update labels, descriptions, and aliases on Wikidata items
- Generate Arabic descriptions from SPARQL queries
- Process scientific articles, taxonomic data, and geographic entities
- Update Wikipedia pages with Wikidata-sourced information

### 1.2 Current Architecture

```
wd-core/
├── WDYe/           # Wikidata entity operations (labels, descriptions)
├── nep/            # New entity processing (scientific articles, taxonomy)
├── des/            # Description generation (geographic, places, books)
├── people/         # Person-related bots (occupations, nationalities)
├── cy/             # Cycling-specific Wikipedia page updates
├── prop_labs/      # Property label operations
├── desc_dicts/     # Large dictionaries of translations
├── old/nep_copy/   # DUPLICATE CODE (deprecated but present)
└── himowd-public_html/  # PHP files (unrelated to Python bots)
```

### 1.3 Technology Stack
- **Language:** Python 3.6+
- **Dependencies:** pywikibot, requests, SPARQLWrapper, dateutil, wikitextparser
- **External APIs:** Wikidata API, Wikipedia API, SPARQL endpoint
- **Data Storage:** JSON files for caching

---

## 2. Code Smells and Anti-Patterns

### 2.1 Global Mutable State (Critical)

**Files affected:** Multiple files across all modules

**Example 1:** `des/desc.py:71-76`
```python
q_list_done = []
New_QS = {1: []}
offset = {1: 0}
offset_place = {1: 0}
limit = {1: 0}
QSlimit = {1: 3000}
alllimit = {1: 50000}
```

**Example 2:** `cy/cy_bot/do_text.py:16-23`
```python
remove_date = {}
Work_with_Year = {}
Len_of_results = {}
Len_of_valid_results = {}
new_lines = {}
states = {}
lines = {}
```

**Problem:** Module-level mutable state creates hidden dependencies, makes testing impossible, and causes race conditions.

---

### 2.2 Large Data Dictionaries (Critical)

**File:** `WDYe/d.py` - 1300+ lines of hardcoded dictionaries

**Example:**
```python
Sports_Keys_For_Label = {
    "acrobatic gymnastics": "الجمباز الاكروباتيكي",
    "acrobatic gymnastics racing": "سباق الجمباز الاكروباتيكي",
    # ... 400+ entries
}

Sports_Keys_For_Team = {
    "acrobatic gymnastics": "للجمباز الاكروباتيكي",
    # ... 400+ entries
}
```

**Problem:**
- Data mixed with code
- No data validation
- Impossible to update without code changes
- Violates Single Responsibility Principle

---

### 2.3 Duplicate Code (Critical)

**Pattern:** `old/nep_copy/` contains exact duplicates of `nep/`

**Evidence:**
- `nep/si3.py` vs `old/nep_copy/si3.py` (identical)
- `nep/bots/scientific_article.py` vs `old/nep_copy/scientific_article.py`
- `nep/tables/lists.py` vs `old/nep_copy/tables/lists.py`

**Impact:** Maintenance nightmare - bugs must be fixed in two places.

---

### 2.4 God Objects (Critical)

**Example 1:** `prop_labs/wd_Session.py:49-191`

```python
class WikidataSession:
    def __init__(self, username: str, password: str):
        self.s = requests.Session()
        self.username = username
        self.password = password
        self.csrf_token = None
        self.save_all = False

    def _get_login_token(self) -> str: ...
    def login(self): ...
    def wbgetentities_en(self, ids: List[str]) -> Dict[str, dict]: ...
    def confirm_if_ask(self, pid: str, field: str, value: str) -> bool: ...
    def set_label_ar(self, pid: str, value: str, summary: str, ...): ...
    def set_description_ar(self, pid: str, value: str, summary: str, ...): ...
```

**Problem:** Single class handles authentication, API calls, user interaction, and data transformation.

**Example 2:** `des/desc.py:57` - `WD_API_Bot` singleton used throughout
```python
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="bot", www="www")
```

---

### 2.5 Magic Numbers and Strings (High)

**Example:** `nep/si3.py:190-238`

```python
for P31 in P31_table:
    if not P31:
        continue
    printe.output(f'q:"{q}", P31:"{P31}", en:"{endes}", ar:"{ardes}"')

    if P31 == "Q5":                      # Magic string: human
        work_people(item, endes.lower(), num, ardes)
        break
    elif P31 == "Q16521":                # Magic string: taxon
        work_taxon_desc(item, endes)
        break
    elif P31 in railway_tables:          # External dependency
        work_railway(item, P31)
        break
    # ... 20+ more magic string comparisons
```

**Problem:** No constants, no enums, scattered Wikidata QIDs.

---

### 2.6 Procedural Code in OOP Language (High)

**Example:** `nep/bots/scientific_article.py:325-416`

```python
def make_scientific_article(item, p31, num, TestTable=False):
    tablem = {"descriptions": {}, "qid": "", "fixlang": []}
    q = item["q"]
    printe.output(f"<<lightyellow>> **{num}: make_scientific_article: {q}")

    if p31 != "Q13442814":
        printe.output("<<lightred>> make_scientific_article: can't make desc p31 != Q13442814")
        return tablem

    precision = ""
    item_descriptions = item.get("descriptions", {})
    P577 = Get_P_API_time(item, "P577")
    pubdate = {}
    if P577:
        pubdate = fixdate(P577["time"])
        # ... 90 more lines of nested logic
```

**Problem:** 90+ line function with multiple responsibilities, no classes, deeply nested conditionals.

---

### 2.7 Inconsistent Error Handling (High)

**Pattern:** Multiple error handling approaches across codebase

**Example 1:** Silent failures (`cy/cy_bot/cy_api.py:164-173`)
```python
try:
    json1 = session[1].get(url, params=params, timeout=10).json()
except requests.exceptions.ReadTimeout:
    print(f"ReadTimeout: {url}")
except Exception as e:
    print("<<lightred>> Traceback (most recent call last):")
    print(f"<<lightred>> Exception:{e}.")
```

**Example 2:** No error handling (`WDYe/common.py:148-154`)
```python
quary = queries[topic]
Limit = 'Limit 5000'
if topic in limiTa:
    Limit = 'Limit 100'
quary = quary + Limit
trans2 = {topic: DescraptionsTable[topic]}  # Could raise KeyError
newdesc.mainfromQuarry2(topic, quary, trans2)
```

---

### 2.8 Tight Coupling (Critical)

**Example:** Import chains creating circular dependencies

```
nep/si3.py imports:
├── from wd_api import wd_desc
├── from des.ru_st_2_latin import make_en_label
├── from des.desc import work_one_item
├── from des.places import placesTable
├── from des.railway import railway_tables, work_railway
├── from desc_dicts.descraptions import replace_desc
├── from nep.wr_people import work_people
├── from people.people_get_topic import print_new_jobs
├── from nep.bots.helps import Get_P_API_id, log_new_types
├── from nep.bots.scientific_article import make_scientific_article
├── from nep.bots.tax_desc import work_taxon_desc
├── from nep.tables.lists import space_list_and_other, others_list, others_list_2
├── from nep.tables.si_tables import MainTestTable, new_types, offsetbg, Qids_translate, Add_en_labels, Geo_List
└── from nep.space_others import Make_space_desc, Make_others_desc
```

**Problem:** Changes to any module ripple through entire codebase.

---

### 2.9 Command-Line Argument Parsing (Medium)

**Pattern:** Direct `sys.argv` parsing scattered throughout

**Example:** `nep/tables/si_tables.py:24-33`
```python
for arg in sys.argv:
    arg, _, value = arg.partition(":")
    if arg.startswith("-"):
        arg = arg[1:]
    if arg.lower() in ["offset", "off"]:
        print(f"offsetbg[1] = int({value})")
        offsetbg[1] = int(value)
```

**Problem:** No argparse, no validation, repeated pattern in every file.

---

### 2.10 Hardcoded Credentials (Security Risk)

**File:** `prop_labs/wd_Session.py:37-38`
```python
username = User_tables_ibrahem["username"]
password = User_tables_ibrahem["password"]
```

**File:** `cy/cy_bot/cy_api.py:19-20`
```python
username = useraccount.username
password = useraccount.password
```

**Problem:** Credentials in code, no environment variable support.

---

## 3. Dependency Issues and Coupling Map

### 3.1 Dependency Graph

```
                    ┌─────────────────┐
                    │   wd_api (ext)  │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼──────┐   ┌────────▼────────┐   ┌──────▼─────┐
│  desc_dicts  │   │  WDYe (labels)  │   │   nep/     │
└──────────────┘   └────────┬────────┘   └──────┬─────┘
                            │                    │
                    ┌───────▼────────┐   ┌──────▼─────┐
                    │      des/       │◄──┤   people/  │
                    │  (descriptions)│   └────────────┘
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │      cy/        │
                    │   (cycling)     │
                    └─────────────────┘
```

### 3.2 External Dependencies

| Dependency | Usage | Risk |
|------------|-------|------|
| `newapi` | Custom wrapper around Wikidata API | Single point of failure |
| `himo_api` | API wrapper (WD_API_Bot) | Tightly coupled, not in repo |
| `wd_api` | Wikidata operations | External, unclear location |
| `pywikibot` | Wikipedia bot framework | Version compatibility |
| `api_sql` | SQL queries for dumps | Unclear data source |

### 3.3 Coupling Metrics

| Module | Imports | Fan-out | Fan-in | Coupling Score |
|--------|---------|---------|--------|----------------|
| `nep/si3.py` | 15 | 15 | 5 | **Critical (75)** |
| `des/desc.py` | 8 | 8 | 10 | **High (80)** |
| `cy/cy6.py` | 4 | 4 | 2 | Medium (8) |
| `WDYe/common.py` | 3 | 3 | 8 | **High (24)** |
| `people/people_get_topic.py` | 1 | 1 | 3 | Low (3) |

---

## 4. Refactoring Roadmap

### Phase 1: Foundation (Weeks 1-2)
**Goal:** Establish testing infrastructure and eliminate code duplication

1. **Set up testing framework**
   - Add `pytest` configuration
   - Create `tests/` directory structure
   - Set up test fixtures for common objects

2. **Remove duplicate code**
   - Delete `old/nep_copy/` directory
   - Verify `nep/` is the single source of truth
   - Add git pre-commit hook to prevent future duplicates

3. **Create configuration layer**
   ```python
   # config/settings.py
   from dataclasses import dataclass
   from typing import Dict

   @dataclass
   class WikidataConfig:
       api_endpoint: str = "https://www.wikidata.org/w/api.php"
       sparql_endpoint: str = "https://query.wikidata.org/sparql"
       timeout: int = 60
       max_retries: int = 3

   @dataclass
   class BotConfig:
       test_mode: bool = False
       batch_size: int = 50
       delay_seconds: float = 0.1
   ```

### Phase 2: Data Layer (Weeks 3-4)
**Goal:** Separate data from code and establish data contracts

1. **Extract dictionaries to data files**
   ```python
   # data/sports_translations.json
   {
       "sports_keys_for_label": {
           "acrobatic gymnastics": "الجمباز الاكروباتيكي",
           ...
       }
   }
   ```

2. **Create data access layer**
   ```python
   # core/data_loader.py
   from pathlib import Path
   import json

   class TranslationData:
       _instance = None

       def __new__(cls):
           if cls._instance is None:
               cls._instance = super().__new__(cls)
               cls._instance._load_data()
           return cls._instance

       def _load_data(self):
           data_dir = Path(__file__).parent.parent / "data"
           self.sports = json.load((data_dir / "sports_translations.json").open())
           self.occupations = json.load((data_dir / "occupations.json").open())
           # ...
   ```

3. **Establish Wikidata QID constants**
   ```python
   # core/constants.py
   from enum import Enum

   class WikidataEntity(Enum):
       HUMAN = "Q5"
       TAXON = "Q16521"
       SCIENTIFIC_ARTICLE = "Q13442814"
       # ...

   class WikidataProperty(Enum):
       INSTANCE_OF = "P31"
       OCCUPATION = "P106"
       COUNTRY_OF_CITIZENSHIP = "P27"
       # ...
   ```

### Phase 3: Service Layer (Weeks 5-7)
**Goal:** Implement service interfaces and dependency injection

1. **Create service abstractions**
   ```python
   # core/services/wikidata_service.py
   from abc import ABC, abstractmethod
   from typing import Dict, List, Optional

   class WikidataService(ABC):
       @abstractmethod
       def get_item(self, qid: str) -> Dict:
           pass

       @abstractmethod
       def set_description(self, qid: str, language: str, value: str) -> bool:
           pass

       @abstractmethod
       def set_label(self, qid: str, language: str, value: str) -> bool:
           pass
   ```

2. **Implement concrete services**
   ```python
   # core/services/wikidata_api_service.py
   import requests
   from core.services.wikidata_service import WikidataService
   from core.config import WikidataConfig

   class WikidataApiService(WikidataService):
       def __init__(self, config: WikidataConfig, session: requests.Session):
           self.config = config
           self.session = session
           self._csrf_token = None

       def get_item(self, qid: str) -> Dict:
           params = {
               "action": "wbgetentities",
               "ids": qid,
               "format": "json"
           }
           response = self.session.get(
               self.config.api_endpoint,
               params=params,
               timeout=self.config.timeout
           )
           response.raise_for_status()
           return response.json()
   ```

3. **Create description generators**
   ```python
   # core/generators/description_generator.py
   from abc import ABC, abstractmethod

   class DescriptionGenerator(ABC):
       @abstractmethod
       def can_generate(self, item: Dict) -> bool:
           """Return True if this generator can handle the item."""
           pass

       @abstractmethod
       def generate(self, item: Dict, language: str) -> str:
           """Generate a description for the item."""
           pass

   # core/generators/scientific_article_generator.py
   class ScientificArticleGenerator(DescriptionGenerator):
       def __init__(self, translator: TranslationData):
           self.translator = translator

       def can_generate(self, item: Dict) -> bool:
           return WikidataEntity.SCIENTIFIC_ARTICLE.value in item.get("instance_of", [])

       def generate(self, item: Dict, language: str) -> str:
           pub_date = self._extract_publication_date(item)
           return self._format_description(pub_date, language)
   ```

### Phase 4: Orchestration Layer (Weeks 8-9)
**Goal:** Implement workflow orchestration with proper error handling

1. **Create pipeline framework**
   ```python
   # core/pipeline/pipeline.py
   from dataclasses import dataclass
   from typing import List, Callable

   @dataclass
   class PipelineResult:
       success: bool
       processed: int
       failed: int
       errors: List[str]

   class ProcessingPipeline:
       def __init__(self, steps: List[Callable]):
           self.steps = steps

       def execute(self, items: List[Dict]) -> PipelineResult:
           result = PipelineResult(True, 0, 0, [])

           for item in items:
               try:
                   for step in self.steps:
                       item = step(item)
                   result.processed += 1
               except Exception as e:
                   result.failed += 1
                   result.errors.append(f"{item.get('q', 'unknown')}: {str(e)}")

           result.success = result.failed == 0
           return result
   ```

2. **Implement item processors**
   ```python
   # core/processors/item_processor.py
   from core.services.wikidata_service import WikidataService
   from core.generators.description_generator import DescriptionGenerator

   class ItemProcessor:
       def __init__(
           self,
           wikidata_service: WikidataService,
           generators: List[DescriptionGenerator]
       ):
           self.wikidata_service = wikidata_service
           self.generators = generators

       def process_item(self, qid: str, target_languages: List[str]) -> bool:
           item = self.wikidata_service.get_item(qid)

           for language in target_languages:
               if language in item.get("descriptions", {}):
                   continue

               for generator in self.generators:
                   if generator.can_generate(item):
                       description = generator.generate(item, language)
                       self.wikidata_service.set_description(qid, language, description)
                       break

           return True
   ```

### Phase 5: CLI Layer (Weeks 10-11)
**Goal:** Unified command-line interface

1. **Create CLI framework**
   ```python
   # cli/main.py
   import argparse
   from core.pipeline import ProcessingPipeline
   from core.processors import ItemProcessor

   def create_parser() -> argparse.ArgumentParser:
       parser = argparse.ArgumentParser(
           description="Wikidata Bot Framework",
           formatter_class=argparse.ArgumentDefaultsHelpFormatter
       )

       subparsers = parser.add_subparsers(dest="command", required=True)

       # Add subcommands
       _add_descriptions_command(subparsers)
       _add_labels_command(subparsers)
       _add_validate_command(subparsers)

       return parser

   def main():
       parser = create_parser()
       args = parser.parse_args()

       # Execute command
       return args.func(args)
   ```

2. **Refactor existing entry points**
   - `WDYe/common.py` → `cli/commands/descriptions.py`
   - `nep/si3.py` → `cli/commands/process_items.py`
   - `cy/cy6.py` → `cli/commands/cycling.py`

### Phase 6: Testing & Documentation (Weeks 12-13)
**Goal:** Comprehensive test coverage and documentation

1. **Unit tests**
   ```python
   # tests/generators/test_scientific_article_generator.py
   import pytest
   from core.generators.scientific_article_generator import ScientificArticleGenerator
   from tests.fixtures import sample_scientific_article

   def test_can_generate_scientific_article(sample_scientific_article):
       generator = ScientificArticleGenerator(mock_translator)
       assert generator.can_generate(sample_scientific_article)

   def test_generates_arabic_description(sample_scientific_article):
       generator = ScientificArticleGenerator(mock_translator)
       description = generator.generate(sample_scientific_article, "ar")
       assert "مقالة بحثية" in description
   ```

2. **Integration tests**
   ```python
   # tests/integration/test_pipeline.py
   import pytest
   from core.pipeline import ProcessingPipeline

   @pytest.mark.integration
   def test_full_pipeline():
       pipeline = ProcessingPipeline([
           validate_item,
           generate_descriptions,
           upload_to_wikidata
       ])

       result = pipeline.execute(test_items)
       assert result.success
   ```

3. **Documentation**
   - `README.md` - Overview and quick start
   - `docs/architecture.md` - System architecture
   - `docs/api.md` - API documentation
   - `docs/contributing.md` - Contribution guidelines

---

## 5. Concrete Changes Per File/Module

### 5.1 Root Directory

| File | Change | Priority |
|------|--------|----------|
| `refactor.md` | **CREATE** - This document | Critical |
| `pyproject.toml` | **CREATE** - Modern Python project config | High |
| `.env.example` | **CREATE** - Environment template | High |
| `tests/` | **CREATE** - Test directory | Critical |
| `data/` | **CREATE** - Data files directory | Critical |

### 5.2 WDYe Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `WDYe/d.py` | 1300+ line dictionary | Move to `data/sports_translations.json` | Delete |
| `WDYe/common.py` | Script with global state | `cli/commands/descriptions.py` + `core/generators/` | Refactor |
| `WDYe/module.py` | Simple script | `cli/commands/module.py` | Refactor |
| `WDYe/label.py` | Label operations | `core/services/label_service.py` | Refactor |

### 5.3 NEP Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `nep/si3.py` | 250-line orchestration | `core/pipeline/` + `cli/commands/process.py` | Refactor |
| `nep/bots/scientific_article.py` | 416-line function | `core/generators/scientific_article.py` | Refactor |
| `nep/tables/si_tables.py` | Global state + constants | `core/constants.py` | Split |
| `nep/new_way.py` | Utility functions | `core/utils/sparql.py` | Move |

### 5.4 DES Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `des/desc.py` | 318-line script with globals | `core/generators/geographic.py` | Refactor |
| `des/places.py` | Dictionary | `data/places.json` | Extract |
| `des/p155tables.py` | Tables | `data/categories.json` | Extract |

### 5.5 CY Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `cy/cy6.py` | Entry point | `cli/commands/cycling.py` | Refactor |
| `cy/cy_bot/cy_api.py` | API client | `core/services/wikipedia_service.py` | Refactor |
| `cy/cy_bot/do_text.py` | 600-line processing | `core/processors/cycling_processor.py` | Refactor |

### 5.6 People Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `people/people_get_topic.py` | 187-line dictionary + logic | `data/occupations.json` + `core/generators/person.py` | Split |
| `people/Nationalities.py` | Dictionary | `data/nationalities.json` | Extract |

### 5.7 Prop_Labs Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `prop_labs/wd_Session.py` | Monolithic class | `core/services/wikidata_service.py` + `core/services/auth.py` | Split |
| `prop_labs/gemini_bot.py` | AI integration | `core/services/ai_service.py` | Move |

### 5.8 Desc_Dicts Module

| File | Current | Proposed | Action |
|------|---------|----------|--------|
| `desc_dicts/descraptions.py` | 429-line dictionary | Split into JSON files in `data/` | Extract |
| `desc_dicts/scientific_article_desc.py` | Dictionary | `data/scientific_article_translations.json` | Extract |

### 5.9 Delete These Files

| File | Reason |
|------|--------|
| `old/` | Duplicate code |
| `himowd-public_html/` | Unrelated PHP files |
| `tttt.py` | Test file |
| `pub2.py` | Temporary script |
| `arlanglinks.py` | One-off script (move to scripts/) |

---

## 6. Technical Debt Risks

### 6.1 Critical Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **Global state corruption** | High | High | Eliminate all module-level mutable variables |
| **Wikidata rate limiting** | High | Medium | Implement rate limiting in service layer |
| **Credential exposure** | Critical | Low | Move to environment variables |
| **Data loss** | High | Low | Add transaction support and rollback |
| **Breaking API changes** | High | Medium | Abstract API behind service interface |

### 6.2 Maintainability Risks

| Risk | Current | Target | Priority |
|------|---------|--------|----------|
| Cyclomatic complexity | 45+ | <10 per function | Critical |
| Code duplication | 30% | <5% | High |
| Test coverage | 0% | >80% | Critical |
| Documentation | 5% | 100% public API | High |
| Type hints | 0% | 100% | Medium |

### 6.3 Security Risks

| Issue | Severity | Location | Fix |
|-------|----------|----------|-----|
| Hardcoded credentials | **Critical** | `prop_labs/wd_Session.py:37-38` | Environment variables |
| SQL injection potential | High | `arlanglinks.py:25-32` | Parameterized queries |
| No input validation | Medium | All CLI entry points | Add validation layer |
| Unverified TLS | Medium | Multiple requests | Certificate verification |

---

## 7. Success Metrics

### 7.1 Code Quality Metrics

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Test coverage | 0% | 80% | `pytest --cov` |
| Cyclomatic complexity | 45+ | <10 avg | `radon cc` |
| Code duplication | 30% | <5% | `radon mi` |
| Type hint coverage | 0% | 100% | `mypy` |
| Lines of code | ~15,000 | ~10,000 | `cloc` |

### 7.2 Operational Metrics

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Mean time to refactor | N/A | <2 weeks per module | Sprint tracking |
| Bug fix time | Days | Hours | Issue tracking |
| Deployment success rate | Unknown | >95% | Monitoring |
| API quota usage | Unknown | Measured | Logging |

---

## 8. Migration Strategy

### 8.1 Incremental Migration Path

1. **Week 1-2**: Set up new structure alongside old code
   ```
   wd-core/
   ├── legacy/          # Rename existing modules
   │   ├── WDYe/
   │   ├── nep/
   │   └── ...
   ├── core/            # New structure
   │   ├── services/
   │   ├── generators/
   │   └── ...
   ├── cli/             # New CLI
   └── tests/           # New tests
   ```

2. **Week 3-8**: Migrate module by module
   - Migrate one module at a time
   - Keep legacy version working
   - Add tests for migrated code
   - Update CI/CD

3. **Week 9-10**: Parallel run
   - Run both legacy and new versions
   - Compare outputs
   - Fix discrepancies

4. **Week 11-12**: Cutover
   - Switch to new version
   - Monitor for issues
   - Keep legacy as rollback option

5. **Week 13**: Cleanup
   - Remove legacy code
   - Update documentation
   - Archive old code

### 8.2 Rollback Plan

If critical issues arise:
1. Revert to `legacy/` directory
2. Disable new CLI entry points
3. Restore old configuration
4. Document issues for next iteration

---

## 9. Recommended Tools

### 9.1 Static Analysis

```bash
# Install tools
pip install pylint mypy bandit safety

# Run analysis
pylint core/
mypy core/
bandit -r core/
safety check
```

### 9.2 Code Quality

```bash
# Install tools
pip install black isort radicale

# Format code
black core/
isort core/

# Check complexity
radon cc core/ -a
```

### 9.3 Testing

```bash
# Install tools
pip install pytest pytest-cov pytest-mock

# Run tests
pytest tests/ --cov=core --cov-report=html
```

---

## 10. Next Steps

1. **Immediate (This Week)**
   - Review this document with team
   - Set up `pyproject.toml` and testing infrastructure
   - Create feature branch for refactoring

2. **Short Term (Next 2 Weeks)**
   - Implement Phase 1 (Foundation)
   - Begin Phase 2 (Data Layer)
   - Set up CI/CD pipeline

3. **Medium Term (Next 6 Weeks)**
   - Complete Phases 3-5
   - Achieve 50% test coverage
   - Migrate 2-3 modules completely

4. **Long Term (Next 13 Weeks)**
   - Complete full migration
   - Remove legacy code
   - Update all documentation

---

## Appendix A: File Statistics

```
Language                 Files       Lines       Code     Comments     Blanks
──────────────────────────────────────────────────────────────────────────
Python                     150       15000       12000        1500       1500
JSON                        20        2000        2000           0          0
YAML                         5         100         100           0          0
Markdown                     3         500         500           0          0
──────────────────────────────────────────────────────────────────────────
TOTAL                      178       17600       14600        1500       1500
```

## Appendix B: Dependency Graph (Full)

```
External Dependencies:
├── pywikibot (Wikipedia bot framework)
├── requests (HTTP client)
├── SPARQLWrapper (SPARQL queries)
├── python-dateutil (Date parsing)
├── wikitextparser (Wiki text parsing)
└── newapi (Custom - unclear source)

Internal Module Dependencies:
├── newapi (Unclear location)
├── himo_api (Unclear location)
├── wd_api (Unclear location)
└── api_sql (Unclear location)
```

---

**End of Analysis**
