def age_definition(age):
    if age <= 7:
        print('Ты в детском саду')
    elif age <= 17:
        print("ты учишься в школе")
    elif age <= 23:
        print("ты учишься в ВУЗе")
    else: 
        print("ты работаешь")
        
age = int(input("Введите ваш возраст: "))
age_definition(age)