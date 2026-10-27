secret_number = 7
guessed = False
while not guessed:
    user_input = int(input("Угадай число от 1 до 10: "))
    if user_input == secret_number:
       print("Поздравляю! Вы угадали число.")
       guessed = True
    else:
       print("Попробуйте еще раз.") 