import pandas as pd

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def search_item(self, query, by='name'):
        if by == 'barcode':
            result = self.df[self.df['codigo_barra'] == query]
        else:
            result = self.df[self.df['nombre'] == query]
        return result

    def modify_item(self, code, new_price, new_stock):
        self.df.loc[self.df['codigo_barra'] == code, ['precio', 'stock']] = [new_price, new_stock]
        self.df.to_csv(self.file_path, index=False)
