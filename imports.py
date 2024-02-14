from pathlib import Path
import numpy as np
import pandas as pd


PATH_TO_FOLDER = Path.cwd() / 'database'


def get_entry_by_values(characteristics, path = PATH_TO_FOLDER ):
    if Path(f'{path}/phone_book_db.csv').exists():
        phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
        for key, value in characteristics.items():
            if value != '':
                phone_book_df = phone_book_df[phone_book_df[key] == value]
        return phone_book_df
    else:
        return None





# get_entry_by_values({
#                     "surname": 'vale',
#                     "name": 'guziev',
#                     "middle_name": '',
#                     "organization": '',
#                     "organization_phone_number": '',
#                     "personal_phone_number": ''})