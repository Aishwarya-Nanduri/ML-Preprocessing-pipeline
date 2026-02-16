from src.data_loader import load_data
from src.preprocess import (
    handle_missing_values, 
    encode_categorical,
    scale_feature
)
def main():
    df=load_data("data/students.csv")
    if df is not None:
        df=handle_missing_values(df)
        df=encode_categorical(df)
        df=scale_feature(df)
        print("\nFinal dataset after encoding:")
        print(df)
        df.to_csv("Outputs/processed_students.csv", index=False)
if __name__=="__main__":
    main()