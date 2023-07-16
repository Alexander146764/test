def load_contacts(contacts):
    contacts = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                last_name, first_name, middle_name, phone_number = line.strip().split(',')
                contact = {
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number
                }
                contacts.append(contact)
        print("Данные успешно загружены.")
    except FileNotFoundError:
        print("Файл не найден.")
    return contacts

def save_contacts(contacts, file_name):
    try:
        with open(file_name, 'w') as file:
            for contact in contacts:
                line = f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n"
                file.write(line)
        print("Данные успешно сохранены.")
    except Exception as e:
        print("Ошибка при сохранении данных:", str(e))

def print_contacts(contacts):
    if not contacts:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for contact in contacts:
            print(f"Фамилия: {contact['last_name']}")
            print(f"Имя: {contact['first_name']}")
            print(f"Отчество: {contact['middle_name']}")
            print(f"Номер телефона: {contact['phone_number']}")
            print("--------------------")

def add_contact(contacts):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    contacts.append(contact)
    print("Контакт успешно добавлен.")

def update_contact(contacts, search_key):
    found_contacts = []
    for contact in contacts:
        if search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower():
            last_name = input("Введите новую фамилию: ")
            first_name = input("Введите новое имя: ")
            middle_name = input("Введите новое отчество: ")
            phone_number = input("Введите новый номер телефона: ")
            contact['last_name'] = last_name
            contact['first_name'] = first_name
            contact['middle_name'] = middle_name
            contact['phone_number'] = phone_number
            print("Контакт успешно обновлен.")

def delete_contact(contacts, search_key):
    found_contacts = []
    for contact in contacts:
        if search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower():
            found_contacts.append(contact)
    if found_contacts:
        for contact in found_contacts:
            contacts.remove(contact)
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")
