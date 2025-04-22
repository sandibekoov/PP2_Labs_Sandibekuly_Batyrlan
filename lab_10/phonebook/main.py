import psycopg2
from config import load_config
from insert import insert_data
from update import update_person
from delete import get_vendors
from query import get_people


def print_menu():
    print("""
    1. Добавить контакт вручную
    2. Добавить контакты из CSV
    3. Обновить данные (имя, отчество, фамилию или номер)
    4. Удалить контакт по имени
    5. Найти контакт (по имени, фамилии, телефону и т.д.)
    6. Выйти
    """)


def main():
    while True:
        print_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            name = input("Имя: ")
            second_name = input("Отчество: ")
            last_name = input("Фамилия: ")
            phone = input("Телефон: ")
            insert_data(name, second_name, last_name, phone)

        elif choice == "2":
            from csv import DictReader
            with open("contacts.csv", mode="r", newline="") as data:
                contacts = DictReader(data)
                for contact in contacts:
                    insert_data(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"])

        elif choice == "3":
            try:
                person_id = int(input("ID пользователя: "))
                field = input("Что изменить? (name, second_name, last_name, phone_number): ")
                new_value = input("Новое значение: ")
                update_person(person_id, field, new_value)
            except:
                print("Ошибка! Убедитесь, что ID — число.")

        elif choice == "4":
            get_vendors()
            print("Контакт с именем 'Alice' удалён (можно изменить в delete.py)")

        elif choice == "5":
            column = input("Введите категорию поиска (name, phone_number и т.д.): ")
            value = input("Введите значение: ")
            get_people(column, value)

        elif choice == "6":
            print("Выход...")
            break


if __name__ == '__main__':
    main()
1