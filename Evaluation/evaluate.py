import pandas as pd
import numpy as np
import argparse

#TREC USAGE

#NDCG@10 and Precision@10:
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg_cut.5 -m P.5 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/linguistic_sentiment_runfiles/runfile_2021_LambdaMart.txt
##/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg_cut.5 -m P.5 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sbert_runfiles/runfile_2021_LambdaMart.txt
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg_cut.5 -m P.5 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sentiment_sarcasm_runfiles/runfile_2021_LambdaMart.txt

#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg_cut.5 -m P.5 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/linguistic_sentiment_runfiles/runfile_2020_LambdaMart.txt
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg_cut.5 -m P.5 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sbert_runfiles/runfile_2020_LambdaMart.txt
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg_cut.5 -m P.5 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sentiment_sarcasm_runfiles/runfile_2020_LambdaMart.txt

##MAP
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m map /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/runfile_2021.txt
#NDCG@10 and Precision@10:
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m ndcg -m P.10 /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/runfile_2020.txt

#MAP
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q -m map /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/runfile_2020.txt
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/runfile_2021.txt
#/Users/balazs/Desktop/trec_eval-9.0.7/trec_eval -q /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels /Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/runfile_2020.txt


"""
evaluate.py Usage:

-- Baseline
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/baseline_runfiles/baseline_runfile_2021.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/baseline_runfiles/baseline_runfile_2020.txt --depth=5


-- RanomForest

Linguistic & Sentiment
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/linguistic_sentiment_runfiles/runfile_2021.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/linguistic_sentiment_runfiles/runfile_2020.txt --depth=5

SBERT
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sbert_runfiles/runfile_2021.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sbert_runfiles/runfile_2020.txt --depth=5

Sentiment & Sarcasm
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sentiment_sarcasm_runfiles/runfile_2021.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sentiment_sarcasm_runfiles/runfile_2020.txt --depth=5

----

-- LambdaMART

Linguistic & Sentiment
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/linguistic_sentiment_runfiles/runfile_2021_LambdaMart.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/linguistic_sentiment_runfiles/runfile_2020_LambdaMart.txt --depth=5

SBERT
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sbert_runfiles/runfile_2021_LambdaMart.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sbert_runfiles/runfile_2020_LambdaMart.txt --depth=5

Sentiment & Sarcasm
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_21/touche-task1-51-100-relevance.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sentiment_sarcasm_runfiles/runfile_2021_LambdaMart.txt --depth=5
python3 evaluate.py --qrel_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Evaluation/ev_files_20/touche2020-task1-relevance-args-me-corpus-version-2020-04-01.qrels --run_path=/Users/balazs/Desktop/dissertationProjectCode/dissertationCodeBase/Data/runfiles_2020_2021/sentiment_sarcasm_runfiles/runfile_2020_LambdaMart.txt --depth=5

+---------------------------------------+------------------+------------+
| Run Tag                               | Year             | nDCG@5     |
+---------------------------------------+------------------+------------+
| **baseline_runfile_2020**             | **2020**         | **0.371**  |
| **baseline_runfile_2021**             | **2021**         | **0.408**  |
+---------------------------------------+------------------+------------+
| linguistic_sentiment_2020_RandomForest| 2020             | 0.687      |
| linguistic_sentiment_2021_RandomForest| 2021             | 0.508      |
| sarcasm_sentiment_2020_RandomForest   | 2020             | 0.616      |
| sarcasm_sentiment_2021_RandomForest   | 2021             | 0.503      |
| SBERT_2020_RandomForest               | 2020             | 0.563      |
| SBERT_2021_RandomForest               | 2021             | 0.458      |
| linguistic_sentiment_2021_LambdaMart  | 2021             | 0.473      |
| linguistic_sentiment_2020_LambdaMart  | 2020             | 0.616      |
| SBERT_2021_LambdaMart                 | 2021             | 0.386      |
| SBERT_2020_LambdaMart                 | 2020             | 0.567      |
| sarcasm_sentiment_2021_LambdaMart     | 2021             | 0.455      |
| sarcasm_sentiment_2020_LambdaMart     | 2020             | 0.507      |
+---------------------------------------+------------------+------------+

"""

def load_qrels(path):
    qrels = (
        pd.read_csv(path, header=None, sep=" ")
        .rename({0: "Topic", 1: "Q0", 2: "ID", 3: "Score"}, axis=1)
        .drop("Q0", axis=1)
    )
    qrels["Score"] = qrels["Score"].replace({-2: 0})
    return qrels

def load_runs(path, depth):
    try:
        # If space as separator
        df = (
            pd.read_csv(path, header=None, sep=" ")
            .rename({0: "Topic", 1: "Q0", 2: "ID", 3: "Rank", 4: "Score", 5: "Tag"}, axis=1)
            .sort_values(["Topic", "Rank"], ascending=[False, True])
            .groupby("Topic")
            .head(depth)
            .drop(["Q0", "Score"], axis=1)
        )
    except:
        # tab as as separator
        df = (
            pd.read_csv(path, header=None, sep="\t")
            .rename({0: "Topic", 1: "Q0", 2: "ID", 3: "Rank", 4: "Score", 5: "Tag"}, axis=1)
            .sort_values(["Topic", "Rank"], ascending=[False, True])
            .groupby("Topic")
            .head(depth)
            .drop(["Q0", "Score"], axis=1)
        )

    return df

def calculate_scores(runs, qrels, depth):
    def dcg(data, k):
        ranking = data.Score.astype(int).head(k).tolist()
        return sum(list(map(lambda entry: entry[1] / np.log2(2 + entry[0]), enumerate(ranking, start=0))))

    def normalize(v, min_v, max_v):
        return np.float64(v - min_v) / np.float64(max_v - min_v)

    scores = runs.merge(
        qrels,
        on=["Topic", "ID"],
        how="left"
    )
    scores = scores[~scores.Score.isna()]
    scores = scores.merge(
        scores
        .sort_values('Rank', ascending=True)
        .groupby(['Topic', 'Tag'])
        .apply(dcg, depth)
        .reset_index(name='DCG'),
        on=['Topic', 'Tag'],
        how='left'
    )
    scores = scores.merge(
        qrels
        .sort_values('Score', ascending=False)
        .groupby('Topic')
        .apply(dcg, depth)
        .reset_index(name='IDCG'),
        on=['Topic'],
        how='left'
    )
    scores['NDCG'] = scores.apply(lambda row: normalize(row['DCG'], 0, row['IDCG']), axis=1)
    return (
        scores
        .loc[:, ["Tag", "Topic", "NDCG"]]
        .drop_duplicates()
        .rename({"NDCG": "nDCG@" + str(depth)}, axis=1)
        .reset_index(drop=True)
    )


def calculate_mean(scores, depth):
    return (
        scores
        .groupby("Tag")
        .mean()
        .reset_index()
        .sort_values("nDCG@" + str(depth), ascending=False)
        .drop("Topic", axis=1)
    )


def main(qrel_path, run_path, depth):
    qrels = load_qrels(qrel_path)
    runs = load_runs(run_path, depth)
    scores = calculate_scores(runs, qrels, depth)
    mean_scores = calculate_mean(scores, depth)
    print(mean_scores.round(3))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--qrel_path', type=str, required=True)
    parser.add_argument('--run_path', type=str, required=True)
    parser.add_argument('--depth', type=int, required=True)
    args = parser.parse_args()

    main(args.qrel_path, args.run_path, args.depth)
