# prop_labs - Wikidata Property Arabic Translation Bot

## Project Overview

`prop_labs` is a Wikidata bot that finds properties missing Arabic labels/descriptions, translates the English text using AI (Google Gemini), and writes the Arabic text back to Wikidata. It implements a fetch -> translate -> save pipeline with multi-level caching for resumability.

### Main Modules and Components

| File | Purpose |
|------|---------|
| `fill_ar_props.py` | **Main orchestrator** - SPARQL query, translation loop, Wikidata writes |
| `wd_Session.py` | Wikidata API session class (login, label/description CRUD) |
| `gemini_bot.py` | Google Gemini AI client for English-to-Arabic translation |
| `translate_bot.py` | Higher-level translation wrapper with JSONL caching |
| `openrouter.py` | Standalone OpenRouter API translation script |
| `chutes.py` | Standalone Chutes.ai API test script |
| `gemini_bot copy.py` | Abandoned backup of `gemini_bot.py` |

### Data Files

| File | Purpose |
|------|---------|
| `.env` | Google Gemini API key (**plaintext - security risk**) |
| `cache_data.json` | Main cache (1.7MB) - per-property translations + save status |
| `cache_data_labels.json` | Label-only deduplication cache (168KB) |
| `cache_data_new.json` | Duplicate cache for `openrouter.py` (1.7MB) |
| `dump.jsonl` | JSONL cache of en/ar translation pairs (51KB) |

### Technologies and Dependencies

- **Python 3.10+**
- **google.generativeai** - Google Gemini AI SDK
- **requests** - HTTP client
- **aiohttp** - Async HTTP (for `chutes.py`)
- **SPARQLWrapper** - SPARQL queries
- **tqdm** - Progress bars
- **jsonlines** - JSONL file I/O

---

## Architecture & Code Quality Review

### Code Organization
Linear pipeline: `fill_ar_props.py` orchestrates, `translate_bot.py` handles translation with caching, `gemini_bot.py` is the AI backend, `wd_Session.py` is the Wikidata API layer. Experimental scripts (`openrouter.py`, `chutes.py`) exist alongside.

### Design Patterns
- **Pipeline pattern**: Fetch -> translate -> save
- **Multi-level caching**: Three independent caches for different purposes
- **Resumable execution**: `saved.label`/`saved.description` flags enable restart without re-work
- **Provider abstraction (informal)**: Three translation backends exist but with no shared interface

### Maintainability: 4/10
Significant code duplication across files. No shared abstractions. Abandoned backup file.

### Readability: 5/10
Clear pipeline structure. But duplicated prompts, inconsistent error handling, and cryptic variable names.

### Scalability: 5/10
Synchronous blocking in batch loop. No async support. Per-call session creation.

---

## Strengths

- **Resumable execution**: Cache flags track what's been saved, enabling restart
- **AI-powered translation**: Gemini provides high-quality English-to-Arabic translation
- **Exponential backoff**: `gemini_bot.py` retries with increasing sleep on rate limits
- **Dry-run mode**: `--dry-run` flag for preview without writes
- **Multiple provider experiments**: Gemini, OpenRouter, and Chutes backends available

---

## Weaknesses

- **Plaintext API key in `.env`**: Tracked in repository - credential leak
- **Abandoned backup file**: `gemini_bot copy.py` should be deleted
- **Duplicate data files**: `cache_data.json` and `cache_data_new.json` are identical
- **Missing `.env2`**: `chutes.py` and `openrouter.py` reference non-existent file
- **No formal provider interface**: Three translation backends with no shared abstraction
- **Translation prompt duplication**: Same prompt appears in 3 files with slight differences

---

## Critical Issues

1. **Credential leak** (`.env`): Google Gemini API key stored in plaintext and tracked in git. Should be rotated immediately.

2. **Missing `.env2`**: `chutes.py` and `openrouter.py` crash with `FileNotFoundError` if executed.

3. **No `if __name__ == "__main__"` guard** (`openrouter.py`): Importing triggers the entire translation loop.

4. **Unbounded chat history** (`gemini_bot.py`): Module-level `contents` list grows indefinitely, causing memory growth and potential context window overflow.

5. **Placeholder User-Agent** (`wd_Session.py`): `your-email@example.com` doesn't comply with Wikidata bot policy.

---

## Areas That Need Attention

- **Security**: Rotate leaked API key, add `.env` to `.gitignore`
- **Cleanup**: Delete `gemini_bot copy.py` and duplicate cache files
- **Testing**: Zero test files
- **Consolidation**: Merge three translation backends into one abstraction

---

## Improvement Plan

### Quick Wins
- Rotate leaked API key and add `.env` to `.gitignore`
- Delete `gemini_bot copy.py`
- Add `if __name__ == "__main__"` guard to `openrouter.py`
- Clear chat history periodically in `gemini_bot.py`
- Fix placeholder User-Agent email

### Medium-term Improvements
- Create abstract `TranslationProvider` interface
- Consolidate three caches into one
- Merge translation prompts into single source of truth
- Add proper `argparse` to all scripts

### Long-term Refactoring
- Add pytest test suite
- Implement async batch processing
- Create proper Python package with `pyproject.toml`
- Add rate-limit handling to OpenRouter integration

---

## Comprehensive Review

| Metric | Score |
|--------|-------|
| **Overall Rating** | 4/10 |
| **Production Readiness** | Low - credential leak, missing files, no tests |
| **Technical Debt** | High - 3 backends, 3 caches, duplicated prompts |
| **Risk Assessment** | High - leaked API key, unbounded memory, missing files crash |
| **Maintainability** | 4/10 - high duplication, no abstractions |
