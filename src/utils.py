import datetime
import json


def modify_account_number(account):
    """
    Преобразует по маске номера счетов  в формат **ХХХХ и карт в формат ХХХХ ХХ** **** ХХХХ
    :param account: str
    :return: str
    """
    account_number = account.split()[-1]
    account_name = ' '.join(account.split()[:-1])
    if account_name == 'Счет':
        return f"Счет **{account_number[-4:]}"
    return f"{account_name} {account_number[:4]} {account_number[4:6]}** **** {account_number[12:]}"


def modify_date(line):
    """
    Преобразует формат даты в ДД.ММ.ГГГГ
    :param line: str (Y-m-dTHH:MM:SS.ms)
    :return: date (d.m.Y)
    """
    operation_date = datetime.date(int(line[:4]), int(line[5:7]), int(line[8:10]))
    return operation_date.strftime('%d.%m.%Y')


def show_operation(operation_):
    """
    Выводит информацию об операции в формате:

    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>

    :param operation_: dictionary
    :return: f-string
    """
    operation_date = modify_date(operation_['date'])
    direction_to = modify_account_number(operation_['to'])
    if 'from' in operation_:
        direction = modify_account_number(operation_['from']) + ' -> ' + direction_to
    else:
        direction = direction_to
    amount = operation_['operationAmount']['amount']
    currency = operation_['operationAmount']['currency']['name']

    return f"{operation_date} {operation_['description']}\n{direction}\n{amount} {currency}"


def convert_json_to_list_of_dictionaries(input_file):
    """
    Преобразует файл .json в список словарей
    :param input_file: json-file
    :return: list_of_dictionaries
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        all_operations_ = json.load(file)
    return all_operations_


def select_executed_operations(all_operations):
    """
    Выбирает из списка только выполненные клиентом операций
    и создает из них новый список
    :param all_operations: list of dictionaries
    :return: list of dictionaries
    """
    executed_operations_ = []
    for operation_ in all_operations:
        if operation_.get('state') == 'EXECUTED':
            executed_operations_.append(operation_)
    return executed_operations_


def sort_operations_by_date(operations):
    """
    Сортирует список операций по дате от последней к первой
    :param operations: list of dictionaries
    :return: list of dictionaries
    """
    sorted_operations_ = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations_
