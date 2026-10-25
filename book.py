import pandas as pd

class Buku:
    def __init__(self, title, author, category, price):
        self.title = str(title)
        self.author = str(author)
        self.category = str(category)
        self.price = float(price) if pd.notna(price) else 0.0
