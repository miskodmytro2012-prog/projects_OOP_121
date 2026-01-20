def login(username, password):
    # Правильні дані користувачів
    users = {
        "admin": "12345",
        "user1": "password1",
        "user2": "password2",
        "guest": "guest123"
    }

    # Перевіряємо, чи існує користувач
    assert username in users, "Невірне ім'я користувача або пароль"

    # Перевіряємо пароль
    assert users[username] == password, "Невірне ім'я користувача або пароль"

    print(f"Вхід виконано успішно для {username}")


# Виклики функції для тестування
login("admin", "12345")
login("user1", "password1")
login("user2", "password2")
login("guest", "guest123")

# Спроби з неправильними даними
try:
    login("admin", "wrongpass")
except AssertionError as e:
    print(e)

try:
    login("unknown", "123")
except AssertionError as e:
    print(e)

try:
    login("user1", "pass")
except AssertionError as e:
    print(e)

try:
    login("user2", "Password2")
except AssertionError as e:
    print(e)

try:
    login("guest", "123guest")
except AssertionError as e:
    print(e)

# Додаткові тести для різних комбінацій
try:
    login("", "")
except AssertionError as e:
    print(e)

try:
    login("Admin", "12345")
except AssertionError as e:
    print(e)

try:
    login("USER1", "password1")
except AssertionError as e:
    print(e)

try:
    login("user2", "")
except AssertionError as e:
    print(e)

try:
    login("guest", "Guest123")
except AssertionError as e:
    print(e)

# Тести для відсутніх користувачів
try:
    login("root", "toor")
except AssertionError as e:
    print(e)

try:
    login("test", "test123")
except AssertionError as e:
    print(e)

try:
    login("newuser", "newpass")
except AssertionError as e:
    print(e)

try:
    login("admin123", "12345")
except AssertionError as e:
    print(e)

try:
    login("user3", "password3")
except AssertionError as e:
    print(e)

# Тести для пробілів
try:
    login(" ", " ")
except AssertionError as e:
    print(e)

try:
    login("admin ", "12345")
except AssertionError as e:
    print(e)

try:
    login("user1", " password1")
except AssertionError as e:
    print(e)

try:
    login("guest", " guest123")
except AssertionError as e:
    print(e)

# Додаткові тестові виклики
try:
    login("admin", "12345 ")
except AssertionError as e:
    print(e)

try:
    login("user1", "Password1")
except AssertionError as e:
    print(e)

try:
    login("user2", "password2 ")
except AssertionError as e:
    print(e)

try:
    login("guest", "Guest123")
except AssertionError as e:
    print(e)

# Ще декілька тестів
try:
    login("ADMIN", "12345")
except AssertionError as e:
    print(e)

try:
    login("user1", "Password1")
except AssertionError as e:
    print(e)

try:
    login("user2", "Password2")
except AssertionError as e:
    print(e)

try:
    login("guest", "guest1234")
except AssertionError as e:
    print(e)

try:
    login("admin", "")
except AssertionError as e:
    print(e)

try:
    login("user1", "")
except AssertionError as e:
    print(e)

try:
    login("user2", "")
except AssertionError as e:
    print(e)

try:
    login("guest", "")
except AssertionError as e:
    print(e)

try:
    login("", "12345")
except AssertionError as e:
    print(e)

try:
    login("", "password1")
except AssertionError as e:
    print(e)

try:
    login("", "password2")
except AssertionError as e:
    print(e)

try:
    login("", "guest123")
except AssertionError as e:
    print(e)

try:
    login("ADMIN", "12345")
except AssertionError as e:
    print(e)

try:
    login("User1", "password1")
except AssertionError as e:
    print(e)

try:
    login("User2", "password2")
except AssertionError as e:
    print(e)

try:
    login("Guest", "guest123")
except AssertionError as e:
    print(e)