from pathlib import Path
from math import ceil
import pandas as pd



PATH_TO_FOLDER = Path.cwd() / 'database'


def get_entry_by_values(characteristics, path=PATH_TO_FOLDER):
    if characteristics["personal_phone_number"] != "":
        characteristics["personal_phone_number"] = int(characteristics["personal_phone_number"][1:])
    if characteristics["organization_phone_number"] != "":
        characteristics["organization_phone_number"] = int(characteristics["organization_phone_number"])
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    for key, value in characteristics.items():
        if value != '':
            phone_book_df = phone_book_df[phone_book_df[key] == value]
    return phone_book_df


def get_count_pages(path = PATH_TO_FOLDER):
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    cont_positions = phone_book_df.index[-1] + 1
    count_pages = ceil(cont_positions/2)
    return count_pages


def get_page(page_number, path = PATH_TO_FOLDER):
    low_limit = int(page_number)*2-2
    up_limit = low_limit+1
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    phone_book_df_by_page = phone_book_df.loc[low_limit : up_limit]
    return phone_book_df_by_page




# get_entry_by_values({
#                     "surname": 'vale',
#                     "name": '',
#                     "middle_name": '',
#                     "organization": '',
#                     "organization_phone_number": '',
#                     "personal_phone_number": ''})