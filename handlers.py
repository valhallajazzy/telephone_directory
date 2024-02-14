import phonenumbers


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

# print(check_valid_new_entry({'personal_phone_number': "+79857655443",
#                              'organization_phone_number': "32132"}))

def check_valid_characteristics(characteristics):
    if check_valid_number(characteristics["personal_phone_number"]) is False:
        return False
    if len(characteristics["organization_phone_number"]) < 3 or characteristics["organization_phone_number"].isdigit() is False:
        return False
    return True


# new_entry = {
#         "surname": surname,
#         "name": name,
#         "middle_name": middle_name,
#         "organization": organization,
#         "organization_phone_number": organization_phone_number,
#         "personal_phone_number": personal_phone_number }