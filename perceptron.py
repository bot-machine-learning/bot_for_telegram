from random import choice
from numpy import array, dot, random


unit_step = lambda x: 0 if x < 0 else 1

training_data = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
] #СЕТ ДЛЯ ТРЕНИ ИЛИ

w = random.rand(3)
errors = []
a = []
eta = 0.2
n = 100

for i in range(n):
    x, expected = choice(training_data)
    result = dot(w, x)                    #ПРОИЗВЕДЕНИЕ ВЕКТОРОВ
    error = expected - unit_step(result)  #НАХОЖДЕНИЕ ОШИБКИ
    errors.append(error)                  #ПОПОЛНЕНИЕ ОШИБОК
    w += eta * error * x                  #ПОВЫШЕНИЕ ИЛИ ПОНИЖЕНИЕ ВЕСОВ В ЗАВИСИМОСТИ ОТ РЕЗУЛЬТАТА ЮНИТ СТЕП


for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

for i in range(2):
    d = input()
    a.append(int(d))

a.append(1)
print ('see your values accuracy')
result = dot(a, w)
print("{}: {} -> {}".format(a[:2], result, unit_step(result)))






