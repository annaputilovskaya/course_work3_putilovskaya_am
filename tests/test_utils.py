import unittest
from src.utils import modify_account_number, modify_date, show_operation


class TestUtils(unittest.TestCase):
    def test_modify_account_number(self):
        self.assertEqual(modify_account_number("Счет 72731966109147704472"), "Счет **4472")
        self.assertEqual(modify_account_number("Maestro 3928549031574026"), "Maestro 3928 54** **** 4026")
        self.assertEqual(modify_account_number("Visa Platinum 1246377376343588"), "Visa Platinum 1246 37** **** 3588")

    def test_modify_date(self):
        self.assertEqual(modify_date("2018-01-26T15:40:13.413061"), "26.01.2018")

    def test_show_operation(self):
        operation1 = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
        operation2 = {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }

        self.assertEqual(show_operation(operation1), "26.08.2019 Перевод организации\n"
                                                     "Maestro 1596 83** **** 5199 -> Счет **9589\n"
                                                     "31957.58 руб.")
        self.assertEqual(show_operation(operation2), "23.03.2018 Открытие вклада\n"
                                                     "Счет **2431\n"
                                                     "48223.05 руб.")
