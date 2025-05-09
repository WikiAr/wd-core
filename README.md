[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/WikiAr/wd-core)
  
# wd-core

wikidata core

## New Feature: Dump File Reader and Descriptions Adder

This new feature involves reading a dump file and adding descriptions to new Wikidata items.

### Dependencies

## Labels, Descriptions, and Aliases Statistics

This feature generates a table that displays the number of labels, descriptions, and aliases for items per language. The data is retrieved from a JSON file that stores old data. If the JSON file does not exist, it is created and updated with the current data.

### Commands

- `python3 core8/pwb.py dump/labels/do_text`: This command runs the feature.
- `python3 core8/pwb.py dump/labels/do_text test`: This command runs the feature in test mode.

### Files

- `dump/labels/do_text.py`: This file contains the main code for the feature.
- `dump/labels/labels_old_values.py`: This file contains the code for handling the JSON file that stores old data.

- Python 3.6 or higher
- cython
- numpy

### New Commands

- `read_dump`: This command reads a dump file.
- `add_descriptions`: This command adds descriptions to new Wikidata items.

### How to Use

1. Run the `read_dump` command to read a dump file.
2. Run the `add_descriptions` command to add descriptions to new Wikidata items.

### Known Issues

- The `read_dump` command may take a long time to run for large dump files.
- The `add_descriptions` command may not add descriptions to all new Wikidata items if there are too many new items.
