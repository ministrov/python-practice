""" Нужно написать программу, которая будет 
          принимать ввод трех чисел и выводить наибольшее из них. 
"""

input_first_num = float(input("Введите первое число: "))
input_second_num = float(input("Введите второе число: "))
input_third_num = float(input("Введите третье число: "))

max_value = 0

if input_first_num >= input_second_num and input_first_num >= input_third_num:
    max_value = input_first_num
elif input_second_num >= input_first_num and input_second_num >= input_third_num:
    max_value = input_second_num
else:
    max_value = input_third_num

print(int(max_value))

# print(input_first_num)
# print(input_second_num)
# print(input_third_num)

# print(type(input_first_num))
# print(type(input_second_num))
# print(type(input_third_num))

# Питоничное решение этой же задачи

prompts = ['Введите первое число: ',
           'Введите второе число: ', 'Введите третье число: ']
numbers = [float(input(prompt)) for prompt in prompts]
print(max(numbers))
