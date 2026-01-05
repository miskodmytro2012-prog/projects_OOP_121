import os
import datetime

def format_size(size):
    for unit in ['Б', 'КБ', 'МБ', 'ГБ']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} ТБ"


def print_line():
    print("-" * 80)


def file_info(path):
    try:
        size = os.path.getsize(path)
        created = os.path.getctime(path)
        modified = os.path.getmtime(path)

        print(f"Файл: {os.path.basename(path)}")
        print(f"Розмір: {format_size(size)}")
        print(f"Створено: {datetime.datetime.fromtimestamp(created)}")
        print(f"Змінено: {datetime.datetime.fromtimestamp(modified)}")

    except Exception as error:
        print(f"Помилка при читанні файлу: {error}")


def directory_info(path):
    try:
        print(f"Директорія: {path}")
        items = os.listdir(path)
        print(f"Елементів: {len(items)}")
    except Exception as error:
        print(f"Помилка доступу: {error}")


def scan_path(path):
    if not os.path.exists(path):
        print("Шлях не існує")
        return

    for root, dirs, files in os.walk(path):
        print_line()
        directory_info(root)

        if not dirs and not files:
            print("Порожня директорія")

        for directory in dirs:
            print(f"Папка: {directory}")

        for file in files:
            full_path = os.path.join(root, file)
            file_info(full_path)


def main():
    print_line()
    print("Аналіз файлової системи")
    print_line()

    user_path = input("Введіть шлях для аналізу: ").strip()

    print_line()
    scan_path(user_path)
    print_line()

    print("Завершено")


main()