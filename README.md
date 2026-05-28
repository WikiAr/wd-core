[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/WikiAr/wd-core)

# wd_core

A Wikidata bot framework focused on programmatically enriching Wikidata items with Arabic-language (and multilingual) labels, descriptions, aliases, and claims. Queries Wikidata via SPARQL, identifies items needing Arabic metadata, generates translations through lookup tables and AI (Google Gemini), and writes results back via the Wikidata API.

Deployed to [Wikimedia Toolforge](https://toolforge.org/).

## New Feature: Dump File Reader and Descriptions Adder

This new feature involves reading a dump file and adding descriptions to new Wikidata items.

### Dependencies

## Labels, Descriptions, and Aliases Statistics

This feature generates a table that displays the number of labels, descriptions, and aliases for items per language. The data is retrieved from a JSON file that stores old data. If the JSON file does not exist, it is created and updated with the current data.

### Commands

-   `python3 core8/pwb.py dump/labels/do_text`: This command runs the feature.
-   `python3 core8/pwb.py dump/labels/do_text test`: This command runs the feature in test mode.

### Files

-   `dump/labels/do_text.py`: This file contains the main code for the feature.
-   `dump/labels/labels_old_values.py`: This file contains the code for handling the JSON file that stores old data.

-   Python 3.6 or higher
-   cython
-   numpy

### New Commands

-   `read_dump`: This command reads a dump file.
-   `add_descriptions`: This command adds descriptions to new Wikidata items.

### How to Use

1. Run the `read_dump` command to read a dump file.
2. Run the `add_descriptions` command to add descriptions to new Wikidata items.

### Known Issues

-   The `read_dump` command may take a long time to run for large dump files.
-   The `add_descriptions` command may not add descriptions to all new Wikidata items if there are too many new items.

## Shared Module Dependencies

This repo imports shared modules from `shared/`: `himo_api`, `wd_api`, `logging_config`, `new_all`, `gent`, `likeapi`.

Note: `wd_core` also has its own internal `bots_subs/hi_api/` and `bots_subs/wd_api/` layers. The `newapi` package (external) provides `WikiLoginClient` and `AllAPIS`.

## Entry Points

-   [src/alabel/labels.py](src/alabel/labels.py) -- Arabic labels from sitelinks
-   [src/cy/jsub.py](src/cy/jsub.py) -- Cycling race results bot
-   [src/des/fam.py](src/des/fam.py) -- Generic description adder
-   [src/nep/si3g.py](src/nep/si3g.py) -- Main description bot (new pages)
-   [src/nep/si3g_qua.py](src/nep/si3g_qua.py) -- SPARQL-based people descriptions
-   [src/neq/nldes3.py](src/neq/nldes3.py) -- Missing Arabic description finder
-   [src/people/new3.py](src/people/new3.py) -- People description bot
-   [src/prop_labs/fill_ar_props.py](src/prop_labs/fill_ar_props.py) -- AI-powered property translation
