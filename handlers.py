import os

import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from terminaltables import AsciiTable
from settings import path
import pandas as pd


def check_valid_number(phone_number):
    try:
        if phone_number[1:].isdigit() is False:
            print(phone_number[1:])
            return False
        number = phonenumbers.parse(phone_number, "RU")
        return phonenumbers.is_valid_number(number)
    except NumberParseException:
        print('Непроавильно введен код страны')
        return False


def check_valid_new_entry(new_entry):
    for key, value in new_entry.items():
        if value == '':
            return False
    if check_valid_number(new_entry["personal_phone_number"]) is False:
        return False
    if not check_availability_phone_in_db(new_entry["personal_phone_number"]).empty:
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


def check_availability_phone_in_db(phone_number, path=path):
    os.makedirs(f'{path}', exist_ok=True)
    if not os.path.exists(f'{path}/phone_book_db.csv'):
        with open(f'{path}/phone_book_db.csv', 'w+') as file:
            file.write("surname,name,middle_name,organization,organization_phone_number,personal_phone_number\n")
    phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
    phone_book_df = phone_book_df[phone_book_df["personal_phone_number"] == int(phone_number[1:])]
    return phone_book_df


def check_valid_patch_entry(patch_entry, path=path):
    if patch_entry["personal_phone_number"] != "":
        if check_valid_number(patch_entry["personal_phone_number"]) is False:
            return False
        phone_book_df = pd.read_csv(f'{path}/phone_book_db.csv')
        phone_book_df = phone_book_df[
            phone_book_df["personal_phone_number"] == int(patch_entry["personal_phone_number"][1:])
        ]
        if not phone_book_df.empty:
            return False
    if patch_entry["organization_phone_number"] != "":
        if len(patch_entry["organization_phone_number"]) < 3 or patch_entry["organization_phone_number"].isdigit() is False:
            return False
    return True