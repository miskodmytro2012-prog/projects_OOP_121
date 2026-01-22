import requests
from datetime import datetime

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
USD_CODE = "USD"
EUR_CODE = "EUR"

def get_currency_data(url):
    """
    Функція отримує дані з API НБУ
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("Помилка під час запиту:", error)
        return None

def find_currency_rate(data, code):
    """
    Пошук курсу валюти за кодом
    """
    for currency in data:
        if currency.get("cc") == code:
            return currency.get("rate")
    return None

def print_currency_rate(name, code, rate):
    """
    Вивід курсу валюти
    """
    if rate is not None:
        print(f"{name} ({code}): {rate} грн")
    else:
        print(f"{name} ({code}): дані відсутні")

def print_header():
    print("Офіційні курси валют НБУ")
    print("------------------------")

def print_date():
    today = datetime.now().strftime("%d.%m.%Y")
    print("Дата:", today)

def main():
    print_header()
    print_date()

    currency_data = get_currency_data(NBU_API_URL)

    if currency_data is None:
        print("Не вдалося отримати дані")
        return

    usd_rate = find_currency_rate(currency_data, USD_CODE)
    eur_rate = find_currency_rate(currency_data, EUR_CODE)

    print_currency_rate("Долар США", USD_CODE, usd_rate)
    print_currency_rate("Євро", EUR_CODE, eur_rate)

    print("Кількість валют у відповіді:", len(currency_data))

    if usd_rate is not None and eur_rate is not None:
        print("Курси валют успішно отримані")
    else:
        print("Не всі курси знайдені")

if __name__ == "__main__":
    main()