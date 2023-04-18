# Evaluation Script for Argument Retrieval

This script is designed to evaluate argument retrieval systems using the nDCG@k metric, where `k` represents the depth of the retrieved documents considered for evaluation.

## Usage

\```sh
$ python3 evaluate.py --qrel_path=/path/to/qrels_file --run_path=/path/to/runfile --depth=5
\```

Replace `/path/to/qrels_file` and `/path/to/runfile` with the appropriate paths to your qrels and run files, respectively. Modify the depth parameter as needed.

## Example Results

### Evaluation Result for 2021

| Tag                 | nDCG@5 |
|---------------------|--------|
| 40323335_Run_File_21 | 0.459  |

### Evaluation Result for 2020

| Tag                 | nDCG@5 |
|---------------------|--------|
| 40323335_Run_File_20 | 0.323  |

## Functions

### `load_qrels(path)`

This function reads the qrels file from the given `path` and returns a DataFrame with columns `Topic`, `ID`, and `Score`. The function replaces the `-2` value with `0` in the `Score` column.

### `load_runs(path, depth)`

This function reads the runs file from the given `path` and returns a DataFrame with columns `Topic`, `ID`, `Rank`, and `Tag`. The function only keeps the top `depth` rows for each `Topic`.

### `calculate_scores(runs, qrels, depth)`

This function takes the `runs` and `qrels` DataFrames, and the evaluation depth `depth`, and returns a DataFrame with columns `Tag`, `Topic`, and `NDCG`. The function computes the DCG and IDCG values for each topic and tag, and then calculates the normalized DCG (nDCG) for each topic and tag.

### `calculate_mean(scores, depth)`

This function takes the `scores` DataFrame and the evaluation depth `depth`, and returns a DataFrame with columns `Tag` and `nDCG@k`, where `k` is the depth. The function computes the mean nDCG for each tag.

### `main(qrel_path, run_path, depth)`

This is the main function of the script that calls other functions to load qrels and runs files, calculates nDCG scores, and prints the mean nDCG values.

## Execution

The script is executed by calling the `main()` function with the command-line arguments for qrels and runs file paths and the evaluation depth