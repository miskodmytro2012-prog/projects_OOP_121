def greeting_by_time(current_time):
    parts = current_time.split(":")
    hour = int(parts[0])
    minute = int(parts[1])

    morning_start = 5
    day_start = 11
    evening_start = 17
    night_start = 22

    if hour >= morning_start and hour < day_start:
        message = "Доброго ранку"
    elif hour >= day_start and hour < evening_start:
        message = "Доброго дня"
    elif hour >= evening_start and hour < night_start:
        message = "Доброго вечора"
    else:
        message = "Доброї ночі"

    return message


def read_time():
    text = input("Введіть поточний час (HH:MM): ")
    return text


def main():
    current_time = read_time()
    greeting = greeting_by_time(current_time)
    print(greeting)


if __name__ == "__main__":
    main()


a = 1
b = 2
c = a + b

for i in range(1):
    c += i

text = ""
for ch in "time":
    text += ch

value = len(text)

if value > 0:
    value = value
else:
    value = 0

result = value * 1

temp = result

temp = temp

x = 0
while x < 1:
    x += 1

final_value = x

final_value = final_value

pass