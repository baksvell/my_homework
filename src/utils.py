import json


def load_operations():
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations_py = json.load(file)
        return operations_py


def data_convert(data):
    if data:
        proper_data = ".".join(data[0:10].split("-")[::-1])
    else:
        proper_data = "Дата не указана"
    return proper_data


def transaction_convert(data):
    bill_number = ""
    alpha_array = []
    data_spl = data.split(" ")
    for x in data_spl:
        if x.isdigit():
            bill_number = x
        else:
            alpha_array.append(x)
    if len(bill_number) == 16:
        card_masked = (f"{''.join(bill_number[0:4])} "
                       f"{''.join(bill_number[4:6])}** **** {''.join(bill_number[12:16])}")
    else:
        len_bill = int(len(bill_number)-4)
        card_masked = f'{"".join(len_bill*"*")}{"".join(bill_number[-4:])}'

    transaction = f"{' '.join(alpha_array)} {card_masked}"
    return transaction


def operation_amount(amount, currency):
    final_summ = f"{amount} {currency}"
    return final_summ


def operation_list():
    success_array = []
    for x in load_operations():
        if x.get('id') and x.get('state') != "CANCELED":
            success_array.append(x)
    success_array.sort(key=lambda k: k['date'], reverse=True)
    final_list = success_array[:5]
    return final_list


def presentation(transactions):
    for x in transactions:
        if not x.get('from'):
            final_show = (f"{data_convert(x['date'])} {x['description']}\n"
                          f"{transaction_convert(x['to'])}\n"
                          f"{operation_amount(x['operationAmount']['amount'], x['operationAmount']['currency']['name'])}\n")
        else:
            final_show = (f"{data_convert(x['date'])} {x['description']}\n"
                          f"{transaction_convert(x['from'])} -> {transaction_convert(x['to'])}\n"
                          f"{operation_amount(x['operationAmount']['amount'], x['operationAmount']['currency']['name'])}\n")

        print(final_show)