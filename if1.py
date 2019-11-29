age = int(input("Сколько Вам лет? "))
answer = age 

def what_do(age):
     if 3 <= age <= 6:
        return 'Вам пора в детский сад!'
     elif 7 <= age <= 17:
        return 'Бегом в школу'
     elif 18 <= age <= 25:
        return 'Оооо, брат студент!'
     elif 25 <= age <= 65:
        return 'Прости, но пора на работу!'
     else:
        return 'Отдыхай!)'

p = what_do(answer)
print(p)