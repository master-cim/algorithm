## Гордость университета
# У студентов-программистов шел последний год обучения,
# и близилась выдача дипломов. К этой знаменательной дате
# было решено подготовить символические подарки трем студентам,
# которые имеют максимальный средний балл по итогам обучения.
# Но задача осложнялась тем, что нужно предоставить эти данные в бухгалтерию,
# причем так, чтобы главный бухгалтер Ольга Петровна,
# списывающая деньги на подарки, смогла открыть это в своём любимом Excel.

# Впрочем, для Вас, человека который работает
# не первый год в данном учреждении, это не казалось невыполнимой задачей.

# Функция make_report_about_top3 принимает словарь (students_avg_scores)
# , в котором ключами являются имена студентов,
# а значениями — средний балл за всю учебу.
# Функция находит ТОП-3 студентов, чей средний балл выше, чем у других.
# Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента
# и который потом будет передан в бухгалтерию. Сам файл необходимо создать внутри функции.
# Важно сохранить совместимость с Excel, чтобы Ольга Петровна
# смогла без проблем получить всю нужную информацию.

import pyexcel

students_avg_scores = {'Max': 4.964,
                       'Eric': 4.962,
                       'Peter': 4.923,
                       'Mark': 4.957,
                       'Julie': 4.95,
                       'Jimmy': 4.973,
                       'Felix': 4.937,
                       'Vasya': 4.911,
                       'Don': 4.936,
                       'Zoi': 4.937
                       }


def make_report_about_top3(students_avg_scores):
    pride_list = sorted( students_avg_scores.items(), key=lambda pair: pair[1], reverse=True )[:3]
    pyexcel.save_as(array=pride_list, dest_file_name="pride_list.xls")


if __name__ == '__main__':
    make_report_about_top3(students_avg_scores)
