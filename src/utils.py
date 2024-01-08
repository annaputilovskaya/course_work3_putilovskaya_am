import datetime


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


def show_operation(operation):
    """
    Выводит информацию об операции в формате:

    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>

    :param operation: dictionary
    :return: f-string
    """
    operation_date = modify_date(operation['date'])
    direction_to = modify_account_number(operation['to'])
    if 'from' in operation:
        direction = modify_account_number(operation['from']) + ' -> ' + direction_to
    else:
        direction = direction_to
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    return f"{operation_date} {operation['description']}\n{direction}\n{amount} {currency}"
