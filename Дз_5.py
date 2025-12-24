import colorama
from colorama import Fore, Back, Style

# Ініціалізація бібліотеки
colorama.init()

# Інтроспекція модуля
print("Атрибути модуля colorama:")
print(dir(colorama))

print("\nАтрибути Fore:")
print(dir(Fore))

print("\nАтрибути Back:")
print(dir(Back))

print("\nАтрибути Style:")
print(dir(Style))

print("\n" + "-" * 40)

# Перевірка кольорів тексту
print("Перевірка кольорів тексту:")
print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Fore.BLUE + "Синій текст")
print(Fore.YELLOW + "Жовтий текст")
print(Fore.CYAN + "Бірюзовий текст")
print(Fore.MAGENTA + "Пурпуровий текст")

print(Style.RESET_ALL)

print("-" * 40)

# Перевірка кольорів фону
print("Перевірка кольорів фону:")
print(Back.RED + "Фон червоний")
print(Back.GREEN + "Фон зелений")
print(Back.BLUE + "Фон синій")
print(Back.YELLOW + "Фон жовтий")

print(Style.RESET_ALL)

print("-" * 40)

# Перевірка стилів тексту
print("Перевірка стилів тексту:")
print(Style.BRIGHT + "Яскравий текст")
print(Style.DIM + "Тьмяний текст")
print(Style.NORMAL + "Звичайний текст")

print(Style.RESET_ALL)

print("-" * 40)

# Комбінування стилів
print("Комбінування стилів:")
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "Білий текст на синьому фоні")
print(Fore.YELLOW + Back.RED + "Жовтий текст на червоному фоні")
print(Fore.BLACK + Back.WHITE + "Чорний текст на білому фоні")

print(Style.RESET_ALL)

print("-" * 40)

# Перевірка скидання стилів
print(Fore.RED + "Текст зі стилем")
print("Після скидання стиль стандартний")

print(Style.RESET_ALL)

print("\nПрограма завершена")