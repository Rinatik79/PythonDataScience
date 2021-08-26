# problem 2-2.1

import numpy as np
import pandas as pd

authors = pd.DataFrame({"author_id": [1, 2, 3], "author_name": ['Тургенев', 'Чехов', 'Островский']})
books = pd.DataFrame({"author_id": [1, 1, 1, 2, 2, 3, 3],
                      "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой',
                                     'Гроза', 'Таланты и поклонники'],
                      "price": [450, 300, 350, 500, 450, 370, 290]})

# problem 2-2.2
authors_price = authors.merge(books)
print("Authors and prices:")
print(authors_price)
print()

# problem 2-2.3
top5 = authors_price.sort_values(by="price", ascending=False).head(5)
print("Top 5 books:")
print(top5)

# problem 2-2.4
authors_stat = pd.DataFrame(authors_price, columns=["author_name", "min_price", "max_price", "mean_price"])
authors_stat = authors_stat.drop_duplicates(subset=["author_name"])

# Тут я уверен что это можно одним запросом решить, но я не нашел в интернете описаловку, по этому наворотил такое:
for index, row in authors_stat.iterrows():
    aux = (authors_price.loc[authors_price['author_name'] == authors_stat.get("author_name")[index]])
    authors_stat["min_price"][index] = aux['price'].min()
    authors_stat["max_price"][index] = aux['price'].max()
    authors_stat["mean_price"][index] = aux['price'].mean()

# Вебинар показывает 4-х часовое пустое черное видео. А подконектится вовремя не могу - разница во времени.
# Так что я смог только так. Код работает с варнингами, но значения выдает корректные.

print("\nStat:")
print(authors_stat)

# problem 2-2.5
cover_list = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_price["cover"] = cover_list
print("author price with cover column:")
print(authors_price)

book_info = pd.pivot_table(authors_price, values='price', index=['author_name'],
                           columns=['cover'], aggfunc=np.sum).fillna(0)

print("\nCovers and prices info:")
print(book_info)

book_info.to_pickle('./book_info.pkl', compression='infer', protocol=5, storage_options=None)
book_info2 = pd.read_pickle("./book_info.pkl")

if book_info2.equals (book_info):
    print("\nDataFrames 'book_info' and 'book_info2' are equals.")
