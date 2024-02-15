from pathlib import Path
import pandas as pd

PATH_TO_FOLDER = Path.cwd() / 'database'


def create_new_entry(new_entry, path=PATH_TO_FOLDER):
    path.mkdir(parents=True, exist_ok=True)
    new_entry_df = pd.DataFrame([new_entry], columns=[
        "surname", "name", "middle_name", "organization",
        "organization_phone_number", "personal_phone_number"])
    if Path(f'{path}/phone_book_db.csv').exists():
        new_entry_df.to_csv(f'{path}/phone_book_db.csv', mode='a', header=False, index=False)
    else:
        new_entry_df.to_csv(f'{path}/phone_book_db.csv', mode='a', index=False)


def change_entry_data(phone_number, path=PATH_TO_FOLDER):
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    phone_book_df = phone_book_df[phone_book_df["personal_phone_number"] == int(phone_number[1:])]
