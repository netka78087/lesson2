# def ask_user():
#     while True:
#         answer = input('Как дела? ')
#         if answer == "хорошо":
#             break
# ask_user()
# {"Как дела?": "Хорошо!", "Столица России": "Москва", "На чем летят в Египет?":"На самолете"}
def ask_user():
    while True:
        dict = {"Как дела?": "Хорошо!", "Столица России": "Москва", "На чем летят в Египет?":"На самолете"}
        question = input("Введите вопрос: ")
        for key in dict: 
            if question == key:
                print(dict[key])
            else: 
                print("Вопрос отсутствует в словаре.")
ask_user()