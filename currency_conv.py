import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")

def start_menu():
    while True:
        start = input('\nType 1 for viewing exchange rates and 2 for converting a specific amount. Press Q to quit: ')

        if start == '1':
            view_ex_rates()
        if start == '2':
            convert()
        if start == 'q':
            break
    

def view_ex_rates():
    code_1 = input('What country do you want to convert FROM (3 letter currency code): ')
    code_2 = input('What country do you want to convert TO (3 letter currency code): ')
    try:
        response = requests.get(f'https://v6.exchangerate-api.com/v6/{key}/pair/{code_1.upper()}/{code_2.upper()}')
        result = json.loads(response.text)
        rate = result["conversion_rate"]
        print(f'1 {code_1.upper()} is equal to {rate} {code_2.upper()}')
    except:
        print("An error occurred, please check to see if country codes are valid")

    
def convert():
    code_1 = input('What country do you want to convert FROM (3 letter currency code): ')
    code_2 = input('What country do you want to convert TO (3 letter currency code): ')
    start_amount = int(input("How much money do you want to convert (Number only): "))
    try:
        response = requests.get(f'https://v6.exchangerate-api.com/v6/{key}/pair/{code_1.upper()}/{code_2.upper()}/{start_amount}')
        result = json.loads(response.text)
        end_amount = result["conversion_result"]
        print(f' {start_amount} {code_1.upper()} is equal to {end_amount} {code_2.upper()}')
    except:
        print("An error occurred, please check to see if country codes or amount is valid")



start_menu()