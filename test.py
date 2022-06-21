"""
Есть у нас список учеников которые сдавали тест
Нужно вывести средний балл всех стужентов ,
этот результат надо сравнить со своим баллом
Если ваш балл ниже среднего значит надо вернуть "Провал"
Если ваше балл выше надо вернуть "Прошел"
"""

#
# def average(class_points, your_points):
#     return "Passed" if (sum(class_points) / len(class_points)) < your_points else "Fail"
#     # if (sum(class_points) / len(class_points)) < your_points:
#     #     return "Passed"
#     # return "Fail"
#
#
# class_points = [21, 43, 54, 23, 54]
# print((sum(class_points) / len(class_points)))
# my_points = 30
#
# print(average(class_points, my_points))


"""
Вы решили отправиться на отдых 
Там понадобилось вам арендовать машину
Арендатель говорит , аренда авто в день стоит 40$
Если вы будете арендовать больше или равно 7 дней, дает скидку 50$
Если вы арендуете меньше 7 дней но больше 3 дней , он все равно дает скидку 20$
"""


def arenda(days):
    return days * 40 if days <= 3 else (days * 40) - 20 if 3 < days < 7 else (days * 40) - 50


print(arenda(4))
