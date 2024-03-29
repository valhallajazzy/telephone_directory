import sys
from handlers import (check_valid_new_entry, check_valid_characteristics, get_table_views,
                      check_availability_phone_in_db, check_valid_patch_entry)
from export import create_new_entry, change_entry_data
from imports import get_entry_by_values, get_count_pages, get_page


def create_entry_data(surname, name, middle_name, organization,
                      organization_phone_number, personal_phone_number):
    return {"surname": surname,
            "name": name,
            "middle_name": middle_name,
            "organization": organization,
            "organization_phone_number": organization_phone_number,
            "personal_phone_number": personal_phone_number}


def get_information_interaction():
    get_action = input('Получить информацию из справочника: \n'
                         ' - Получить информацию общего количества страниц: Введите "count" \n'
                         ' - Получить инфромацию по одной или нескольким характеристикам: Введите "values" \n'
                         ' - Получить информацию по номеру страницы (кол-во контактов на одной странице - 10): Введите "<номер страницы>" \n'
                         ' - Выйти из программы: Введите "exit" \n')

    if get_action.isdigit():
        try:
            phone_book_by_page = get_page(get_action)
            if phone_book_by_page.empty:
                return print("Такой страницы не существует")
            return get_table_views(phone_book_by_page)
        except FileNotFoundError:
            print("В справочнике еще нет ни одной записи")

    else:
        if get_action not in ["count", "values", "exit"]:
            print("Введенные вами данные должны быть в соответствии с запрашиваемым контекстом")
        if get_action == "values":
            print("Для получения информации по характеристикам введите их значения \n"
                  "(если данная характеристика не интересует нажимте ENTER и переходите к седующей): ")
            surname = input("Фамилия: ")
            name = input("Имя: ")
            middle_name = input("Отчество: ")
            organization = input("Организация: ")
            organization_phone_number = input(
                "Рабочий номер телефона в формате цифр без '+'. Пример: '2461843': \n")
            personal_phone_number = input("Личный номер телефона в формате +7XXXXXXXXXX ('+' обязателен): ")
            characteristics = create_entry_data(surname, name, middle_name, organization,
                      organization_phone_number, personal_phone_number)
            valid_characteristics = check_valid_characteristics(characteristics)
            if valid_characteristics is False:
                return print("Ошибка ввода данных (Номер телефона)")
            try:
                phone_book_df_by_values = get_entry_by_values(characteristics)
                return get_table_views(phone_book_df_by_values)
            except FileNotFoundError:
                print("В справочнике еще нет ни одной записи")
        if get_action == "count":
            try:
                print(f"Количество страниц в справочнике: {get_count_pages()} \n")
            except FileNotFoundError:
                print("В справочнике еще нет ни одной записи")
        if get_action == 'exit':
            sys.exit()


def post_information_interaction():
    print("Для внесения новой позиции в справочник введите запрашиваемые обязательные поля: ")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    middle_name = input("Отчество: ")
    organization = input("Организация: ")
    organization_phone_number = input("Рабочий номер телефона в формате цифр без '+'. Пример: '2461843': \n")
    personal_phone_number = input("Личный номер телефона в формате +7XXXXXXXXXX ('+' обязателен): ")
    new_entry = create_entry_data(surname, name, middle_name, organization,
                      organization_phone_number, personal_phone_number)
    valid_new_entry = check_valid_new_entry(new_entry)
    if valid_new_entry is True:
        create_new_entry(new_entry)
        print("Ваша запись успешно добавлена")
    else:
        print("Ошибка ввода данных. Либо личный номер телефона уже сущетвует в справочнике у другого контакта.")


def patch_information_interaction():
    patch_phone_number = input("Введите личный номер телефона по которому "
                               "хотите изменить информацию, в формате +7XXXXXXXXXX ('+' обязателен): \n")
    try:
        df_with_personal_number = check_availability_phone_in_db(patch_phone_number)
        if df_with_personal_number.empty:
            return print("Такого номера в справочнике не существует")
        get_table_views(df_with_personal_number)
        print("Для изменения дaнных по позиции введите новые значения характеристик \n"
              "(если данная характеристика не будет изменяться нажимте ENTER и переходите к седующей): ")
        surname = input("Фамилия: ")
        name = input("Имя: ")
        middle_name = input("Отчество: ")
        organization = input("Организация: ")
        organization_phone_number = input(
            "Рабочий номер телефона в формате цифр без '+'. Пример: '2461843': \n")
        personal_phone_number = input("Личный номер телефона в формате +7XXXXXXXXXX ("+" обязателен): ")
        patch_entry = create_entry_data(surname, name, middle_name, organization,
                      organization_phone_number, personal_phone_number)
        check_valid_patch = check_valid_patch_entry(patch_entry)
        if check_valid_patch is False:
            return print("Ошибка ввода данных. Изменяемые номера телефонов либо не валидны, "
                         "либо изменяемый личный номер телефона уже сущетвует в справочнике у другого контакта.")
        return change_entry_data(patch_phone_number, patch_entry)
    except FileNotFoundError:
        print("В справочнике еще нет ни одной записи")


def main_interaction():
        io_action = input('Выберите действие в словаре: \n'
                          ' - Получить информацию из словаря: Введите "get" \n'
                          ' - Добавить информацию в словарь: Введите "post" \n'
                          ' - Редактировать информацию в словаре: Введите "patch" \n'
                          ' - Выйти из программы: Введите "exit" \n')
        if io_action not in ["get","post","patch","exit"]:
            print("Введенные вами данные должны быть в соответствии с запрашиваемым контекстом")

        if io_action == "get":
            get_information_interaction()

        if io_action == "post":
            post_information_interaction()

        if io_action == 'patch':
            patch_information_interaction()

        if io_action == 'exit':
            sys.exit()