import pandas as pd

'''
Recognize whether a column is numerical or categorical.
:parameter
    :param dtf: dataframe - input data
    :param col: str - name of the column to analyze
    :param max_cat: num - max number of unique values to recognize a column as categorical
:return
    "cat" if the column is categorical or "num" otherwise
'''
def utils_recognize_type(dataframe, col, max_cat=20):
    if (dataframe[col].dtype == "O") | (dataframe[col].nunique() < max_cat):
        return "cat"
    else:
        return "num"

Dataframe = pd.read_csv("Statcast Batter Stats.csv")
x = utils_recognize_type(Dataframe,[2],3)

print(x)