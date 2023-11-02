
import random

def generate_array():
    array = []

    # Генеруємо від'ємні елементи (40-60%)
    num_negative = random.randint(18, 26)  # 44 * 0.4 та 44 * 0.6
    for _ in range(num_negative):
        array.append(-random.randint(1, 64))

    # Генеруємо решту парних додатніх елементів
    num_positive_even = 44 - num_negative

    # Генеруємо непарні елементи (до 25%)
    num_odd = min(num_positive_even, random.randint(11, 12))  # До 25%, але не більше, ніж залишилось для парних
    for _ in range(num_odd):
        array.append(random.choice([x for x in range(1, 65) if x % 2 != 0]))

    # Заповнюємо решту місць парними додатніми числами
    for _ in range(num_positive_even - num_odd):
        array.append(2 * random.randint(1, 32))  # Генеруємо парні додатні числа

    # Перемішуємо елементи у масиві, щоб вони були у випадковому порядку
    random.shuffle(array)

    return array

# Генеруємо масив
my_array = generate_array()

# Друкуємо результат
print(my_array)
