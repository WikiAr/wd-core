# wd-core

wikidata core

## New Feature: Dump File Reader and Descriptions Adder

This new feature involves reading a dump file and adding descriptions to new Wikidata items.

### Dependencies

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
