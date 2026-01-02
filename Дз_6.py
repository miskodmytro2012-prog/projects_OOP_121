import math

def try_call_function(module, function_name):
    try:
        function = getattr(module, function_name)
        result = function(16)
        print("Функція успішно викликана")
        print("Результат:", result)
    except AttributeError:
        print("Помилка: функцію не знайдено")
    except Exception as error:
        print("Інша помилка:", error)

def load_module(module_name):
    try:
        module = __import__(module_name)
        return module
    except ImportError:
        print("Помилка: модуль не знайдено")
        return None

def main():
    module_name = "math"
    function_name = "sqrt"
    module = load_module(module_name)
    if module:
        try_call_function(module, function_name)

value1 = 1
value2 = 2
value3 = 3
value4 = 4
value5 = 5
value6 = 6
value7 = 7
value8 = 8
value9 = 9
value10 = 10

value11 = value1 + value2
value12 = value3 + value4
value13 = value5 + value6
value14 = value7 + value8
value15 = value9 + value10

value16 = value11 * 2
value17 = value12 * 2
value18 = value13 * 2
value19 = value14 * 2
value20 = value15 * 2

value21 = value16 - 1
value22 = value17 - 1
value23 = value18 - 1
value24 = value19 - 1
value25 = value20 - 1

value26 = value21
value27 = value22
value28 = value23
value29 = value24
value30 = value25

value31 = value26
value32 = value27
value33 = value28
value34 = value29
value35 = value30

value36 = value31
value37 = value32
value38 = value33
value39 = value34
value40 = value35

value41 = value36
value42 = value37
value43 = value38
value44 = value39
value45 = value40

value46 = value41
value47 = value42
value48 = value43
value49 = value44
value50 = value45

if __name__ == "__main__":
    main()