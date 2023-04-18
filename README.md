## Project: Argument Retrieval and Ranking

This repository contains a collection of Python functions and Jupyter notebooks for searching, retrieving, and ranking arguments from various data sources using learning-to-rank techniques.

## Functions

### Function to Search API and Save Top Arguments to Files

This function searches for the top arguments for each topic in a query topics XML file using an API and saves the top arguments for each topic to a separate file. See the [corresponding Jupyter notebook](Function_to_Search_API_and_Save_Top_Arguments_to_Files.ipynb) for more details.

### Function to Extract Features from CSV Files

This function extracts features from CSV files in a given directory, such as coherence, spelling and grammar, polarity, and subjectivity. See the [corresponding Jupyter notebook](Function_to_Extract_Features_from_CSV_Files.ipynb) for more details.

### Function to Add Relevance Scores to Feature Files

This function adds relevance scores to feature files based on matching topic number and argument ID. See the [corresponding Jupyter notebook](Function_to_Add_Relevance_Scores_to_Feature_Files.ipynb) for more details.

### Function to Extract All Features and Create SVMrank-Formatted Vectors

This function extracts features from CSV files, concatenates them into a single dataframe, converts them to SVMrank-style feature representation, and saves them as a file without headers. See the [corresponding Jupyter notebook](Function_to_Extract_All_Features_and_Create_SVMrank-Formatted_Vectors.ipynb) for more details.

## RankLib Commands

### Train, Test, and Save Learning-to-Rank Models

Commands for training learning-to-rank models using RankNet algorithm with cross entropy loss, evaluating the models using NDCG@10 for the training data and ERR@10 for the test data, and saving the trained models. See the [corresponding Jupyter notebook](Train_Test_Save_Learning_to_Rank_Models.ipynb) for more details.

### Rank and Retrieve Documents Using Pre-Trained Models

Commands for ranking and retrieving documents based on relevance using pre-trained learning-to-rank models loaded from `argument2020.txt` and `argument2021.txt`. The resulting scores for each document will be written to the `argument2021_scorefile.txt` and `argument2020_scorefile.txt` output files, respectively. See the [corresponding Jupyter notebook](Rank_and_Retrieve_Documents_Using_Pre-Trained_Models.ipynb) for more details.

## Required Libraries

- os
- requests
- xml.etree.ElementTree
- pandas
- numpy
- nltk
- textblob
- language_tool_python