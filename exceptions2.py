def get_summ(num_one, num_two):
    try: 
        summ = int(num_one) + int(num_two)
    except ValueError:
        return "Приведение типов не сработало!"
    return summ
num_one = input("Введите число: a = ")
num_two = input("Введите число: b = ")
print(get_summ(num_one, num_two))