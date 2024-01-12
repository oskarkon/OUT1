import pandas as pd
import openpyxl

class DataProcessor:
    def __init__(self, csv_path):
        self.csv_path = csv_path


    def extract(self):
        self.df = pd.read_csv(self.csv_path)
        print(self.df.info())

    def transform(self):
        self.df['X'] = self.df['Attack'] * 3
        print(self.df.info())
        self.df.to_excel('d:\\x.xlsx')

    def process_data(self):
        self.extract()
        self.transform()

if __name__ == '__main__':
    csv_path = 'D:\\prog\\Python\\jupyter\\input\\pokemon.csv'
    processor = DataProcessor(csv_path)
    processor.process_data()
