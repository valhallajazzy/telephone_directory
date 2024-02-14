from handlers import check_valid_new_entry
from export import create_new_entry
from imports import get_entry_by_values

def get_information_interaction():
    get_action = input('Получить информацию из справочника: \n'
                         ' - Получить информацию общего количества страниц: Введите "count" \n'
                         ' - Получить инфромацию по одной или нескольким характеристикам: Введите "values" \n'
                         ' - Получить информацию по номеру страницы: Введите "<номер страницы>" \n'
                         ' - Выйти из программы: Введите "exit" \n')

    if get_action.isdigit():
        pass
    else:
        if get_action not in ["count", "characteristics", "exit"]:
            print("Введенные вами данные должны быть в соответствии с запрашиваемым контекстом")
        else:
            if get_action == "values":
                print("Для получения информации по характеристикам введите их значения \n"
                      "(если данная характеристика не интересует нажимте ENTER и переходите к седующей): ")
                surname = input("Фамилия: ")
                name = input("Имя: ")
                middle_name = input("Отчество: ")
                organization = input("Организация: ")
                organization_phone_number = input(
                    "Рабочий номер телефона в формате цифр без '+'. Пример: '2461843': \n")
                personal_phone_number = input("Личный номер телефона в формате +7XXXXXXXXXX: ")
                characteristics = {
                    "surname": surname,
                    "name": name,
                    "middle_name": middle_name,
                    "organization": organization,
                    "organization_phone_number": organization_phone_number,
                    "personal_phone_number": personal_phone_number}
                valid_characteristics = check_valid_new_entry(characteristics)
                if valid_characteristics is True:
                    get_entry_by_values(characteristics)

                else:
                    print("Ошибка ввода данных")



def post_information_interaction():
    print("Для внесения новой позиции в справочник введите запрашиваемые обязательные поля: ")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    middle_name = input("Отчество: ")
    organization = input("Организация: ")
    organization_phone_number = input("Рабочий номер телефона в формате цифр без '+'. Пример: '2461843': \n")
    personal_phone_number = input("Личный номер телефона в формате +7XXXXXXXXXX: ")
    new_entry = {
            "surname": surname,
            "name": name,
            "middle_name": middle_name,
            "organization": organization,
            "organization_phone_number": organization_phone_number,
            "personal_phone_number": personal_phone_number }
    valid_new_entry = check_valid_new_entry(new_entry)
    if valid_new_entry is True:
        create_new_entry(new_entry)
        print("Ваша запись успешно добавлена")
    else:
        print("Ошибка ввода данных")






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

        # elif io_action == "1":
        #     one()
        # elif io_action == "2":
        #     print("2")
        #     break
        # elif io_action == "3":
        #     print("3")
        #     break
        # else:
        #     print("Пока")
        #     break


main_interaction()