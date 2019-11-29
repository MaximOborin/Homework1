def discounted(price, discount, max_discount=20):
    try :
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except TypeError:
        return "Не правильное значение"


print(discounted(100, 22))
print(discounted(1000, 2))
print(discounted(500, "привет"))