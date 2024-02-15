import phonenumbers
from terminaltables import AsciiTable
from pathlib import Path
import pandas as pd

PATH_TO_FOLDER = Path.cwd() / 'database'


def check_valid_number(phonenumber):
    if phonenumber[1:].isdigit() is False:
        print(phonenumber[1:])
        return False
    number = phonenumbers.parse(phonenumber, "RU")
    return phonenumbers.is_valid_number(number)


def check_valid_new_entry(new_entry):
    for key, value in new_entry.items():
        if value == '':
            return False
    if check_valid_number(new_entry["personal_phone_number"]) is False:
        return False
    if len(new_entry["organization_phone_number"]) < 3 or new_entry["organization_phone_number"].isdigit() is False:
        return False
    return True


def check_valid_characteristics(characteristics):
    if characteristics["personal_phone_number"] != "":
        if check_valid_number(characteristics["personal_phone_number"]) is False:
            return False
    if characteristics["organization_phone_number"] != "":
        if len(characteristics["organization_phone_number"]) < 3 or characteristics["organization_phone_number"].isdigit() is False:
            return False
    return True


def get_table_views(dataframe):
    rows = dataframe.values
    table = [
        ['ФАМИЛИЯ', 'ИМЯ', 'ОТЧЕСТВО', 'ОРГАНИЗАЦИЯ', 'НОМЕР ОРГАНИЗАЦИИ', 'ЛИЧНЫЙ НОМЕР'],
        *rows]
    print(AsciiTable(table).table)


def check_availability_phone_in_db(phone_number, path=PATH_TO_FOLDER):
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    phone_book_df = phone_book_df[phone_book_df["personal_phone_number"] == int(phone_number[1:])]
    return phone_book_df











# new_entry = {
#         "surname": surname,
#         "name": name,
#         "middle_name": middle_name,
#         "organization": organization,
#         "organization_phone_number": organization_phone_number,
#         "personal_phone_number": personal_phone_number }