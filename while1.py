user_questions = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
}

while True: 
    ask_user = input("Введите вопрос ... ")
    if ask_user == "Как дела?":
        print(user_questions["Как дела?"])
        break   

    elif ask_user == "Что делаешь?":
        print(user_questions["Что делаешь?"])
        break  
    else:
        print("Не хочу на это отвечать!!!")
