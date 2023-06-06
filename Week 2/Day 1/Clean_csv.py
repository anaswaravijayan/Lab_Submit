import numpy as np
import pandas as pd
def clean_csv(csv):
    df=pd.read_csv("file1.csv")
    df
    
    def lower_case_columns(df):
        df.columns=[i.lower() for i in df.columns]
        return df
    df=lower_case_columns(df)
    df
    
    def change_column_names(df):
        df.rename(columns={'st':'state'},inplace=True)
        return df
    
    df=change_column_names(df)
    df
    
    a=df['gender'].unique()
    a
    def clean_gender(x):
        if x in ['F','Femal','female']:
            return 'Female'
        elif x in ['M','Male']:
            return 'Male'
        else:
            return np.nan
        
    df['gender']=list(map(clean_gender,df['gender']))
    df['gender'].unique()
    
    df['gender'].value_counts(dropna=False)
    df.info()
    
    df['customer lifetime value']=df['customer lifetime value'].str.replace("%","").astype(float)
    df
    df.info()
    
    null_columns=df.columns[df.isnull().any()]
    null_columns
    counts_column_nulls=df[null_columns].isnull().sum()
    counts_column_nulls
    
    def drop_columns(df):
        df.drop(columns={"customer","number of open complaints","education","gender"},inplace=True)
        return df
    df=drop_columns(df)
    df
    
    mean_customer=np.mean(df['customer lifetime value'])
    mean_customer
    df['customer lifetime value']=df['customer lifetime value'].fillna(mean_customer)
    df
    df['customer lifetime value'].isnull().sum()
    
    df=df.drop_duplicates()
    df.reset_index(drop=True)
    
    return df