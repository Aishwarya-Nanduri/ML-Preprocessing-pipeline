import pandas as pd
def handle_missing_values(df):
    print("\nMissing values before cleaning")
    print(df.isnull().sum())
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
    df["Age"]=df["Age"].fillna(df["Age"].mean())
    df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    return df
def encode_categorical(df): #label encoding and one hot encoding
    #label encoding has logic, one hot does not
    print("\nDataset before encoding")
    print(df.head())
    if "Gender" in df.columns:
        df["Gender"]=df["Gender"].map({"Male":0, "Female":1})
    if "City" in df.columns:
        df=pd.get_dummies(df, columns=["City"], drop_first=False)
    print("\nDataset after encoding:")
    print(df.head())
    return df
import numpy as np #normalization and standardization
def scale_feature(df):
    print("\nDataset before scaling:")
    print(df[["Age","Marks"]].head())
    df["Marks"]=(df["Marks"]-df["Marks"].min()) / \
                  (df["Marks"].max() - df["Marks"].min())
    df["Age"]=(df["Age"]-df["Age"].mean())/df["Age"].std()
    print("\nDataset after scaling:")
    print(df[["Age","Marks"]].head())
    return df
