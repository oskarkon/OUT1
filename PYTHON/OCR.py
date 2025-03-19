import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import os

# Define the image path
image_path = "D:/prog/Python/jupyter/input/plik.jpg"

# Open the image using PIL
img_pl = Image.open(image_path)

# Define tesseract configuration
special_config = '--psm 12 --oem 1'
languages_ = "eng"  # For multiple languages, use "eng+rus+swe" etc.

# Use pytesseract to extract data
data = pytesseract.image_to_data(
    img_pl,
    lang=languages_,
    output_type='data.frame',
    config=special_config
)

def optimizeDf(old_df: pd.DataFrame) -> pd.DataFrame:
    df = old_df[["left", "top", "width", "text"]].copy()
    df['left+width'] = df['left'] + df['width']
    df = df.sort_values(by=['top'], ascending=True)
    df = df.groupby(['top', 'left+width'], sort=False)['text'].sum().unstack('left+width')
    df = df.reindex(sorted(df.columns), axis=1).dropna(how='all').dropna(axis='columns', how='all')
    df = df.fillna('')
    return df

data_imp_sort = optimizeDf(data)

def mergeDfColumns(old_df: pd.DataFrame, threshold: int = 10, rotations: int = 5) -> pd.DataFrame:
    df = old_df.copy()
    for j in range(rotations):
        new_columns = {}
        old_columns = df.columns
        i = 0
        while i < len(old_columns):
            if i < len(old_columns) - 1:
                if any(old_columns[i + 1] == old_columns[i] + x for x in range(1, threshold)):
                    new_col = df[old_columns[i]].astype(str) + df[old_columns[i + 1]].astype(str)
                    new_columns[old_columns[i + 1]] = new_col
                    i += 1
                else:
                    new_columns[old_columns[i]] = df[old_columns[i]]
            else:
                new_columns[old_columns[i]] = df[old_columns[i]]
            i += 1
        df = pd.DataFrame.from_dict(new_columns)
        df = df.replace('', np.nan)
        df = df.dropna(axis='columns', how='all')
    return df

def mergeDfRows(old_df: pd.DataFrame, threshold: int = 10) -> pd.DataFrame:
    new_df = old_df.iloc[:1].copy()
    for i in range(1, len(old_df)):
        if abs(old_df.index[i] - old_df.index[i - 1]) < threshold:
            # Convert columns to string before concatenation
            new_df.iloc[-1] = new_df.iloc[-1].astype(str) + old_df.iloc[i].astype(str)
        else:
            new_df = pd.concat([new_df, old_df.iloc[[i]]])
    return new_df.reset_index(drop=True)

df_new_col = mergeDfColumns(data_imp_sort)
merged_row_df = mergeDfRows(df_new_col)

def clean_df(df):
    df = df.loc[:, (df != df.iloc[0]).any()]
    df = df[(df != '|') & (df != '') & (pd.notnull(df))]
    df = df.dropna(axis=1, how='all')
    return df.fillna('')

cleaned_df = clean_df(merged_row_df.copy())

# Save the cleaned DataFrame to an Excel file
output_path = "D:/prog/Python/jupyter/input/processed_image.xlsx"
cleaned_df.to_excel(output_path, index=False)

print(f"Processed data has been saved to {output_path}")
