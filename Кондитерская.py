# Задача № 5
a = {"Торт": ['мука,яйца,сахар',5.20,500],
     "Пироженое": ['творог,фруктоза,яйца',2.50,250],
     "Маффин": ['белок,творог,сахарозаменитель',3.45,300]} # состав, цена за 100 гр., количество грамм
for key, value in a.items():
    print(key,'-',value[0],'-',value[1],'-',value[2])
w = 0
while True:
    b = input('Введите название товара или n для выхода: ')
    if b == 'n' or b not in a:
        break
    f = input('Введите название товара: + посмотреть описание: ')
    if f in a:
        print(a[f][0])
    g = input('Введите название товара: + узнать стоимость: ')
    if g in a:
        print(a[g][1])
    q = input('Введите название товара: + узнать количество: ')
    if q in a:
        print(a[q][2])
    e = input('Введите название товара: = узнать описание, цену, количество: ')
    if e in a:
        print(a[e][0:3])

    i = int(input('Введите количество товара: '))
    if i > a[b][2]:
        print('Столько товара нет')
        continue
    w = w + (i * a[b][1])
    a[b][2] -= i
    print('Стоимость покупки: ', w)
    for key, value in a.items():
        print(key,'-',value[0],'-',value[1],'-',value[2])