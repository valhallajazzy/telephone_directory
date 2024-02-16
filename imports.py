from settings import path
from math import ceil
import pandas as pd



def get_entry_by_values(characteristics, path=path):
    if characteristics["personal_phone_number"] != "":
        characteristics["personal_phone_number"] = int(characteristics["personal_phone_number"][1:])
    if characteristics["organization_phone_number"] != "":
        characteristics["organization_phone_number"] = int(characteristics["organization_phone_number"])
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    for key, value in characteristics.items():
        if value != '':
            phone_book_df = phone_book_df[phone_book_df[key] == value]
    return phone_book_df


def get_count_pages(path=path):
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    cont_positions = phone_book_df.index[-1] + 1
    count_pages = ceil(cont_positions/10)
    return count_pages


def get_page(page_number, path=path):
    low_limit = int(page_number)*10-10
    up_limit = low_limit+11
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv').sort_values('surname')
    phone_book_df_by_page = phone_book_df.iloc[low_limit : up_limit]
    return phone_book_df_by_page