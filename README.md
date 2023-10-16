# wd-core

wikidata core

## Unit Tests for sweep.yaml

We have added a new unit test file `sweep_test.yaml` to test the functionality implemented in `sweep.yaml`. This unit test file ensures that the `sweep.yaml` file is correctly formatted and contains the expected keys and values. It tests the following:

- The presence and type of expected keys in the `sweep.yaml` file.
- The type of values associated with each key in the `sweep.yaml` file.

These tests are important to ensure the integrity and correctness of the `sweep.yaml` file, which is crucial for the proper functioning of the wd-core project.

To run the tests in `sweep_test.yaml`, use the following command:

```bash
python -m unittest tests/sweep_test.yaml
```
