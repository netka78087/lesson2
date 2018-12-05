# def ask_user():
#     while True:
#         answer = input('Как дела? ')
#         if answer == "хорошо":
#             break
# ask_user()
def ask_user():
    while True:
        dict = {"Как дела?": "Хорошо!", "Столица России": "Москва", "На чем летят в Египет?":"На самолете"}
        question = input("Введите вопрос: ")
        # for key in dict: 
        # if question == key:
        # print(dict[question])
        # else:  
        try: 
            print(dict[question])
        except KeyError:
            print("Вопрос отсутствует в словаре")
        # print("Вопрос отсутствует в словаре.")
ask_user()