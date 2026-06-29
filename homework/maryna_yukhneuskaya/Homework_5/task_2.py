# Option 1 - Longer

result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

operation_index = result_1.index(":")
program_index = result_3.index(":")

number_1 = result_1[operation_index + 2:]
number_2 = result_2[operation_index + 2:]
number_3 = result_3[program_index + 2:]

new_result_1 = int(number_1) + 10
new_result_2 = int(number_2) + 10
new_result_3 = int(number_3) + 10

print(new_result_1)
print(new_result_2)
print(new_result_3)

# Option 2 - Shorter

result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

operation_index = result_1.index(":")
program_index = result_3.index(":")

print(int(result_1[operation_index + 2:]) + 10)
print(int(result_2[operation_index + 2:]) + 10)
print(int(result_3[program_index + 2:]) + 10)
