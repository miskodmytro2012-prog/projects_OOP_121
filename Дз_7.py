import random                                        # 1
import string                                        # 2

def random_letter_generator():                      # 3
    while True:                                     # 4
        yield random.choice(string.ascii_lowercase) # 5

def format_letter_output(letter, index):            # 6
    return f"{index}: {letter}"                     # 7

def uppercase_letters(letters):                     # 8
    result = []                                     # 9
    for l in letters:                               # 10
        result.append(l.upper())                    # 11
    return result                                   # 12

def filter_vowels(letters):                         # 13
    vowels = "aeiou"                                # 14
    result = []                                     # 15
    for l in letters:                               # 16
        if l in vowels:                             # 17
            result.append(l)                        # 18
    return result                                   # 19

def shuffle_letters(letters):                       # 20
    result = letters.copy()                         # 21
    random.shuffle(result)                          # 22
    return result                                   # 23

def count_unique(letters):                          # 24
    return len(set(letters))                        # 25

def generate_letters(n):                            # 26
    gen = random_letter_generator()                # 27
    letters = []                                    # 28
    for _ in range(n):                              # 29
        letters.append(next(gen))                  # 30
    return letters                                  # 31

def print_list(letters):                            # 32
    for i, l in enumerate(letters, 1):             # 33
        print(format_letter_output(l, i))          # 34

# Основний код                                      # 35
letters1 = generate_letters(20)                    # 36
print("Перші 20 букв:")                             # 37
print_list(letters1)                                # 38

letters2 = generate_letters(15)                    # 39
print("\nНаступні 15 букв:")                        # 40
print_list(letters2)                                # 41

all_letters = letters1 + letters2                  # 42
print("\nВсі букви разом:")                         # 43
print_list(all_letters)                             # 44

upper = uppercase_letters(all_letters)             # 45
print("\nВеликі букви:")                             # 46
print_list(upper)                                   # 47

vowels = filter_vowels(all_letters)                # 48
print("\nГолосні букви:")                           # 49
print_list(vowels)                                  # 50

shuffled = shuffle_letters(all_letters)            # 51
print("\nПеремішані букви:")                        # 52
print_list(shuffled)                                # 53

print(f"\nКількість унікальних букв: {count_unique(all_letters)}") # 54

letters3 = generate_letters(10)                    # 55
print("\nЩе 10 букв:")                              # 56
print_list(letters3)                                # 57

all_letters += letters3                             # 58
shuffled_all = shuffle_letters(all_letters)         # 59
print("\nВсі букви перемішані:")                     # 60
print_list(shuffled_all)                             # 61

vowels_all = filter_vowels(all_letters)             # 62
print("\nВсі голосні:")                              # 63
print_list(vowels_all)                               # 64

upper_vowels = uppercase_letters(vowels_all)       # 65
print("\nВеликі голосні:")                           # 66
print_list(upper_vowels)                              # 67

letters4 = generate_letters(5)                     # 68
print("\nЩе 5 букв:")                               # 69
print_list(letters4)                                 # 70

all_letters += letters4                              # 71
print("\nВсі букви після додавання 5:")             # 72
print_list(all_letters)                              # 73

shuffled_all = shuffle_letters(all_letters)         # 74
print("\nПеремішані всі букви після додавання:")     # 75
print_list(shuffled_all)                              # 76

print(f"\nЗагальна кількість букв: {len(all_letters)}") # 77
print(f"Унікальних букв: {count_unique(all_letters)}") # 78

letters5 = generate_letters(12)                    # 79
print("\nЩе 12 букв:")                              # 80
print_list(letters5)                                 # 81

all_letters += letters5                              # 82
print("\nВсі букви після додавання 12:")           # 83
print_list(all_letters)                              # 84

shuffled_all = shuffle_letters(all_letters)         # 85
print("\nПеремішані всі букви після додавання 12:") # 86
print_list(shuffled_all)                              # 87

vowels_all = filter_vowels(all_letters)             # 88
print("\nГолосні після додавання 12 букв:")         # 89
print_list(vowels_all)                               # 90

upper_all = uppercase_letters(all_letters)         # 91
print("\nВсі великі букви:")                        # 92
print_list(upper_all)                                # 93

shuffled_upper = shuffle_letters(upper_all)        # 94
print("\nПеремішані великі букви:")                 # 95
print_list(shuffled_upper)                           # 96

letters6 = generate_letters(8)                     # 97
print("\nЩе 8 букв:")                               # 98
print_list(letters6)                                 # 99

all_letters += letters6                              # 100