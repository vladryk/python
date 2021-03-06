# http://www.ibm.com/developerworks/ru/library/l-pycon/
# http://blog.swlogic.eu/2012/06/14/python-generators-cheatsheet/
# http://anandology.com/python-practice-book/iterators.html
# http://nvie.com/posts/iterators-vs-generators/

# Прежде всего, итератор - это объект (объект-итератор), у которого имеется метод .next().
# Это не совсем верно, но достаточно близко. На самом деле, большая
# часть контекстов требует объект, который сгенерирует итератор, когда к нему
# применяется новая встроенная функция iter(). Для того, чтобы определенный
# пользователем класс (который имеет необходимый метод .next()) возвращал
# итератор, нужно всего лишь обеспечить возврат self методом __iter__().
# Примеры ниже пояснят сказанное. Метод .next() может вызвать исключение
# StopIteration, если итерация логически завершилась.

# Чтобы получить объект-итератор, нужно создать объект, который будет иметь два
# метода со специальными именами:
#     __iter__() - метод, который возвращает сам объект.
#     next() - метод, который возвращает следующее значение итератора.


class SimpleIterator(object):

    def __init__(self,fname):
        self.fd = open(fname,'r')

    def __iter__(self):
        return self

    def next(self):
        l = self.fd.readline()
        if l != '':
            l = l.rstrip('\n')
            num = int(l)
            return num*2
        raise StopIteration

# Внутри все очень просто. Главная работа в методе next().
# В нем считывается следующая строка файла, обрабатывается
# (число умножается на 2) и возвращается в операторе return().
# Когда файл окончится будет вызвано исключение StopIteration.
# Еще один пример:

class Seq14:
   def __init__(self, x):
      self.x = x

   def next(self):
      self.x += 1
      if self.x > 14:
         raise StopIteration
      return self.x**self.x

   def __iter__(self):
      return self

x = 0
it = Seq14(x)

while True:
    try:
        value = it.next()
    except StopIteration:
        break
    print value



# Генераторы (функция-генератор) используются в основном для определения итераторов;
# поэтому не всегда стоит учитывать все тонкости их применения.
# Генератор является функцией, которая запоминает точку в теле функции,
# из которой происходил последний возврат. Второй (или n-ный) вызов
# генератора оказывается в середине функции, причем все локальные
# переменные оказываются неизмененными с момента последнего вызова.

# Генератор, это очень похоже на итератор, только это функция. При вызове этой
# функции в цикле, она при каждом новом цикле выдает следующее значение.
# Пишется эта функция с использованием оператора yield

# yield работает как return, с одной разницей, что между вызовами функций,
# все состояния и данные будут при следующем вызове функции такими, какими
# они были на момент предыдущего исполнения yield.

# По сути это ключевое слово создает итератор, просто создание итератора упрощается
# за счет того, что методы __iter__() и next() создаются автоматически. При выходе
# из функции не по оператору yield автоматически генерируется StopIteration.


import random

def randomwalk_generator():
    last, rand = 1, random.random() # инициализировать элементы-кандидаты
    while rand > 0.1:               # указатель предела
        print'*',                  # отобразить отклонение
        if abs(last-rand) >= 0.4:   # принять номер
            last = rand             # обновить предшествующее значение
            yield rand              # возвращение в конкретную точку (AT THIS POINT)
        rand = random.random()       # новый кандидат
    yield rand                      # возвратить последний небольшой элемент

# можно так:
gen = randomwalk_generator()
try:
    while 1: print gen.next(),
except StopIteration:
    pass

# но чаще и правильнее так:
for num in randomwalk_generator():
    print(num)




# >>> def a():
# ...   p=5
# ...   while p>0:
# ...     yield p
# ...     p=p-1
# ...
# >>> a=a()
# >>> for i in a:
# ...   print i
# ...
# 5
# 4
# 3
# 2
# 1




# xrange() и xreadlines() -- генераторы


# Знаменитая конструкция Python - for elem in lst: -
# фактически запрашивает lst для создания итератора.
# Цикл for будет затем последовательно вызывать метод .next()
# этого итератора, пока не достигнет исключения StopIteration.



# Генераторные выражения
# Выражение-генератор не загружает весь список в память сразу,
# а вместо этого создает объект генератора, поэтому за один раз можно получить только один элемент.

(x*x for x in [1,5,8])
