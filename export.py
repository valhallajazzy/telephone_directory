import csv
from pathlib import Path
import numpy as np
import pandas as pd

PATH_TO_FOLDER = Path.cwd() / 'database'


def create_new_entry(new_entry, path=PATH_TO_FOLDER):
    # path.mkdir(parents=True, exist_ok=True)
    # with open (f'{path}/phone_book_db.csv', 'a', encoding='UTF-8') as file:
    #     data = csv.writer(file)
    #     data.writerow(new_entry)
    path.mkdir(parents=True, exist_ok=True)
    if Path(f'{path}/phone_book_db.csv').exists():
        new_entry_df = pd.DataFrame([new_entry], columns=[
            "surname", "name", "middle_name", "organization",
            "organization_phone_number", "personal_phone_number"])
        new_entry_df.to_csv(f'{path}/phone_book_db.csv', mode='a', header=False, index=False)
    else:
        new_entry_df = pd.DataFrame([new_entry], columns=[
            "surname", "name", "middle_name", "organization",
            "organization_phone_number", "personal_phone_number"])
        new_entry_df.to_csv(f'{path}/phone_book_db.csv', mode='a', index=False)
