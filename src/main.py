import os
from utils import select_executed_operations, sort_operations_by_date, show_operation, \
    convert_json_to_list_of_dictionaries

PATH = os.path.join('..', 'operations.json')
all_operations = convert_json_to_list_of_dictionaries(PATH)
executed_operations = select_executed_operations(all_operations)
sorted_operations = sort_operations_by_date(executed_operations)

for i in range(5):  # Вывод на печать 5 операций через пустую строку
    print(show_operation(sorted_operations[i]))
    print()
