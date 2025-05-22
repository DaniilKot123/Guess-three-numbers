import os
import numpy as np
import random as rand

os.system("chcp 65001")

seed = rand.randint(1,1000000)
np.random.seed(seed)
rules = (
    "Добро пожаловать в игру \"Угадай три числа\"!\n\nПравила игры очень просты. " 
    "Требуется лишь за наименьшее число попыток отгадать все три числа "
    "в любом порядке, задавая вопросы: \"Сколько чисел меньше/равно/больше "
    "определенному числу (которое Вы вводите)?\". Для того, чтобы задать "
    "такой вопрос, требуется в консоль в одной строке написать "
    "сначала знак вопроса, затем через пробел "
    "либо знак меньше (\"<\"), либо знак равно (\"=\"), либо знак больше (\">\"), "
    "а после этого через пробел нужно указать число, "
    "для которого Вы задаётё вопрос. Пример: \"? < 5\". "
    "После корректной формы вопроса консоль Вам выдаст ответ на него, "
    "в ином случае Вам укажут на то, что требуется перезадать вопрос "
    "и напомнят о его корректной форме. В этой игре в качестве ответа "
    "можно указать только три числа сразу, "
    "причём обязательно от меньшего к большему. "
    "Для этого требуется написать в консоль сначала знак восклицания, "
    "а затем после пробела по требуемым правилам указать три числа через пробел. "
    "Пример: \"! 3 3 5\". После корректной формы вопроса консоль Вам выдаст, "
    "сколько чисел было угадано, в ином случае Вам укажут на то, "
    "что требуется переотправить ответ и напомнят о его корректной форме.\n\n"
    "В эту игру можно играть столько раз, сколько Вам захочется. "
    "Новую игру можно начать только после завершения игры. "
    "Для этого требуется написать команду \"Start <уровень сложности>\". "
    "В этой игре есть 4 уровня сложности, которые зависят от диапазона чисел, "
    "в котором загаданы все три числа: "
    "Easy (от 1 до 10), Normal (от 1 до 100), "
    "Hard (от 1 до 1000), Extreme (от 1 до 10000). "
    "Между игр Вы можете единожды посмотреть статистику игр, "
    "написав в строке команду \"Statistics\".\n\n" 
    "Желаем Вам удачи!\n"
)
print(rules)
keys = ['Games', 'Minimum requests']
values_easy = [0, None]
values_normal = [0, None]
values_hard = [0, None]
values_extreme = [0, None]
statistics_easy = dict(zip(keys, values_easy))
statistics_normal = dict(zip(keys, values_normal))
statistics_hard = dict(zip(keys, values_hard))
statistics_extreme = dict(zip(keys, values_extreme))
games_count = 0
while True:
    correct_input = False
    viewing_statistics = False
    while correct_input == False:
        start = input()
        if start == "Statistics" and games_count > 0:
            viewing_statistics = True
            string_easy = (
                f" Easy: Games - {statistics_easy['Games']}; "
                f"Minimum requests - {statistics_easy['Minimum requests']}\n"
            )
            string_normal = (
                f"Normal: Games - {statistics_normal['Games']}; "
                f"Minimum requests - {statistics_normal['Minimum requests']}\n"
            )
            string_hard = (
                f"Hard: Games - {statistics_hard['Games']}; "
                f"Minimum requests - {statistics_hard['Minimum requests']}\n"
            )
            string_extreme = (
                f"Extreme: Games - {statistics_extreme['Games']}; "
                f"Minimum requests - {statistics_extreme['Minimum requests']}\n"
            )
            print(string_easy, string_normal, string_hard, string_extreme)
        elif start == "Statistics" and games_count == 0:
            print("Вы не можете запросить статистику, так как сыграно 0 игр.\n")
        if viewing_statistics:
            start = input()
            viewing_statistics = False
        if start == "Start Easy":
            numbers = np.random.randint(1, 11, size=(1,3))
            correct_input = True
            games_on = True
        elif start == "Start Normal":
            numbers = np.random.randint(1, 101, size=(1,3))
            correct_input = True
            games_on = True
        elif start == "Start Hard":
            numbers = np.random.randint(1, 1001, size=(1,3))
            correct_input = True
            games_on = True
        elif start == "Start Extreme":
            numbers = np.random.randint(1, 10001, size=(1,3))
            correct_input = True
            games_on = True
        else:
            print("Некорректный ввод. Корректная форма: \"Start <уровень сложности>\".\n")
    sorted_numbers = np.sort(numbers)
    attempts = 0
    game_on = True
    while game_on == True:
        request = input()
        correct_request = False
        if request[0] == "?":
            number = request[4:]
            if request[1] == " " and request[3] == " " and number.isdigit() == True:
                if request[2] == "<" or request[2] == "=" or request[2] == ">":
                    correct_request = True
            if correct_request == False:
                print("Некорректный вопрос. Пример корректной формы: \"? < 5\".\n")
                continue
            attempts += 1
            number = int(number)
            if request[2] == "<":
                if sorted_numbers[0][0] >= number:
                    print("0\n")
                elif sorted_numbers[0][1] >= number:
                    print("1\n")
                elif sorted_numbers[0][2] >= number:
                    print("2\n")
                else:
                    print("3\n")
            elif request[2] == "=":
                answer = 0
                if sorted_numbers[0][0] == number:
                    answer += 1
                if sorted_numbers[0][1] == number:
                    answer += 1
                if sorted_numbers[0][2] == number:
                    answer += 1
                print(f"{answer}\n")
            else:
                if sorted_numbers[0][2] <= number:
                    print("0\n")
                elif sorted_numbers[0][1] <= number:
                    print("1\n")
                elif sorted_numbers[0][0] <= number:
                    print("2\n")
                else:
                    print("3\n")
        if request[0] == "!":
            string_numbers = request[2:]
            numbers_array = string_numbers.split(" ")
            if request[1] == " " and len(numbers_array) == 3:
                if numbers_array[0].isdigit() and numbers_array[1].isdigit() and numbers_array[2].isdigit():
                    numbers_array[0] = int(numbers_array[0])
                    numbers_array[1] = int(numbers_array[1])
                    numbers_array[2] = int(numbers_array[2])
                    if numbers_array[0] <= numbers_array[1] and numbers_array[1] <= numbers_array[2]:
                        correct_request = True
            if correct_request == False:
                print("Некорректный ответ. Пример корректной формы: \"! 3 3 5\" (Важно: 3 <= 3 <= 5).\n")
                continue
            attempts += 1
            answer = 0
            if numbers_array[0] == sorted_numbers[0][0]:
                answer += 1
            if numbers_array[1] == sorted_numbers[0][1]:
                answer += 1
            if numbers_array[2] == sorted_numbers[0][2]:
                answer += 1
            if answer <= 2:
                print(f"Угадано чисел: {answer}.\n")
            else:
                print(f"Вы угадали все три числа за столько ходов: {attempts}, поздравляем!\n")
                game_on = False
        if request[0] != "?" and request[0] != "!":
            print("Некорректный запрос. Требуется знак \"?\" при вопросе или знак \"!\" при ответе.\n")
            continue
    games_count += 1
    if start == "Start Easy":
        statistics_easy['Games'] = statistics_easy['Games'] + 1
        if statistics_easy['Minimum requests'] == None or attempts < statistics_easy['Minimum requests']:
            statistics_easy['Minimum requests'] = attempts
    elif start == "Start Normal":
        statistics_normal['Games'] = statistics_normal['Games'] + 1
        if statistics_normal['Minimum requests'] == None or attempts < statistics_normal['Minimum requests']:
            statistics_normal['Minimum requests'] = attempts
    elif start == "Start Hard":
        statistics_hard['Games'] = statistics_hard['Games'] + 1
        if statistics_hard['Minimum requests'] == None or attempts < statistics_hard['Minimum requests']:
            statistics_hard['Minimum requests'] = attempts
    elif start == "Start Extreme":
        statistics_extreme['Games'] = statistics_extreme['Games'] + 1
        if statistics_extreme['Minimum requests'] == None or attempts < statistics_extreme['Minimum requests']:
            statistics_extreme['Minimum requests'] = attempts

    

