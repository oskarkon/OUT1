import pandas as pd
import openpyxl

def extract():
    df=pd.read_csv('D:\\prog\\Python\\jupyter\\input\\pokemon.csv')
    print(df.info())
    return df

def transform(df):
    df['X'] = df['Attack']*3
    print(df.info())
    df.to_excel('d:\\x.xlsx')
    return df

def main():
    df = extract()
    transform(df)

if __name__ == '__main__':
    main()