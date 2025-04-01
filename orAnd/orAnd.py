#виконав студент групи ІН-401, Уманський Дмитро

from random import uniform #імпортуємо функцію uniform з пакету random
import matplotlib.pyplot as plt


def OR(x1, x2):
    """
    Функція для обчислення результату логічного АБО над двома даними точками(парою точок).
    Синаптичні ваги та поріг задані наперед.
    W1 та W2 - ваги. Дорівнюють 1.
    W0 - поріг. Дорівнює -(1/2). Відповідно до розподільчої лінії.
    Спершу обчислюється значення дискримінантної функції.
    В залежності від знаку функції повертаємо значення функції активації. (1/0)
    """
    #ініціалузуємо змінні для синаптичних ваг
    W1 = 1
    W2 = 1

    #ініціалузуємо змінну для порогу
    W0 = -(1/2)

    #обчислюємо значення дискримінантної функції, відповідно до формули
    sum = (W1 * x1) + (W2 * x2) + W0
    
    #в залежності від знаку функції повертаємо значення функції активації
    if sum > 0:     #якщо результат функції більше 0 (додатній)
        return 1    #повертаємо 1
    else:           #в іншому випадку (від'ємний)
        return 0    #повертаємо 0
    
def AND(x1, x2):
    """
    Функція для обчислення результату логічного ТА над двома даними точками(парою точок).
    Синаптичні ваги та поріг задані наперед.
    W1 та W2 - ваги. Дорівнюють 1.
    W0 - поріг. Дорівнює -(3/2). Відповідно до розподільчої лінії.
    Спершу обчислюється значення дискримінантної функції.
    В залежності від знаку функції повертаємо значення функції активації. (1/0)
    """
    #ініціалузуємо змінні для синаптичних ваг
    W1 = 1
    W2 = 1

    #ініціалузуємо змінну для порогу
    W0 = -(3/2)

    #обчислюємо значення дискримінантної функції, відповідно до формули
    sum = (W1 * x1) + (W2 * x2) + W0
    
    #в залежності від знаку функції повертаємо значення функції активації
    if sum > 0:     #якщо результат функції більше 0 (додатній)
        return 1    #повертаємо 1
    else:           #в іншому випадку (від'ємний)
        return 0    #повертаємо 0
    
def NOT(x):
    """
    Функція для обчислення результату логічного НЕ (інверсія вхідного значення).
    Функція повертає 1, якщо вхідним значення був 0, 0 - якщо 1.
    """
    return 1 if x == 0 else 0
    
def XOR(x1, x2):
    """
    Функція для обчислення результату логічного виключного АБО над двома даними точками(парою точок).
    Використовуються ініціалізовані раніше функції OR та AND.
    Функція повертає 1 або 0.
    """
    return AND(OR(x1, x2), NOT(AND(x1, x2)))

def XNOR(x1, x2):
    """
    Функція для обчислення результату логічного виключного АБО-НЕ над двома даними точками(парою точок).
    Використовуються ініціалізовані раніше функції XOR та NOT.
    Функція повертає 1 або 0.
    """
    return NOT(XOR(x1, x2)) #повертаємо інверсивне значення функції XOR

#створюємо масив з 500 рандомними точками, відповідно до рівномірного закону розподілу
#функція uniform(a, b) з пакету random дозволяє це зробити
points = [[uniform(0, 1), uniform(0, 1)] for _ in range(500)]    

class1OR = 'class 1 (OR = 1)'        
class2OR = 'class 2 (OR = 0)'

class1AND = 'class 1 (AND = 1)'        
class2AND = 'class 2 (AND = 0)'

class1XOR = 'class 1 (XOR = 1)'        #ініціалузуємо перший клас (XOR = 1)
class2XOR = 'class 2 (XOR = 0)'        #ініціалузуємо другий клас (XOR = 0)

classificationsOR = {}
classificationsAND = {}
classificationsXOR = {}                #ініціалізуємо словник для зберігання результатів класифікації

for point in points:                #перераховуємо кожну точку
    #призначаємо словнику ключ-слово у вигляді точки
    #а також відповідний клас на основі значення XOR даної точки
    classificationsOR[str(point)] = class1OR if OR(*point) == 1 else class2OR
    classificationsAND[str(point)] = class1AND if AND(*point) == 1 else class2AND
    classificationsXOR[str(point)] = class1XOR if XOR(*point) == 1 else class2XOR   

print(classificationsOR)
print(classificationsAND)    
print(classificationsXOR)              #виводимо результати на екран

plt.figure('Графік для OR')
xValues1OR = [point[0] for point in points if classificationsOR[str(point)] == class1OR]
yValues1OR = [point[1] for point in points if classificationsOR[str(point)] == class1OR]

xValues2OR = [point[0] for point in points if classificationsOR[str(point)] == class2OR]
yValues2OR = [point[1] for point in points if classificationsOR[str(point)] == class2OR]

plt.plot([0, 0.5], [0.5, 0], color='blue', label='OR')

plt.scatter(xValues1OR, yValues1OR, color='black', label='Class 1')
plt.scatter(xValues2OR, yValues2OR, color='red', label='Class 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('OR plot')

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.legend()
plt.grid(True)
plt.show()

plt.figure('Графік для AND')
xValues1AND = [point[0] for point in points if classificationsAND[str(point)] == class1AND]
yValues1AND = [point[1] for point in points if classificationsAND[str(point)] == class1AND]

xValues2AND = [point[0] for point in points if classificationsAND[str(point)] == class2AND]
yValues2AND = [point[1] for point in points if classificationsAND[str(point)] == class2AND]

plt.plot([0, 1.5], [1.5, 0], color='blue', label='AND')

plt.scatter(xValues1AND, yValues1AND, color='black', label='Class 1')
plt.scatter(xValues2AND, yValues2AND, color='red', label='Class 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('AND plot')

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.legend()
plt.grid(True)
plt.show()

plt.figure('Графік для XOR')
xValues1XOR = [point[0] for point in points if classificationsXOR[str(point)] == class1XOR]
yValues1XOR = [point[1] for point in points if classificationsXOR[str(point)] == class1XOR]

xValues2XOR = [point[0] for point in points if classificationsXOR[str(point)] == class2XOR]
yValues2XOR = [point[1] for point in points if classificationsXOR[str(point)] == class2XOR]

plt.plot([0, 0.5], [0.5, 0], color='green', label='OR')
plt.plot([0, 1.5], [1.5, 0], color='blue', label='AND')

plt.scatter(xValues1XOR, yValues1XOR, color='black', label='Class 1')
plt.scatter(xValues2XOR, yValues2XOR, color='red', label='Class 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('XOR plot')

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.legend()
plt.grid(True)
plt.show()