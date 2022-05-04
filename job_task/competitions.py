## Соревнования
# Знакомые вам студенты-программисты уже пережили не одну сессию. 
# Кое-кто из них продемонстрировал потрясающие способности в учебном процессе.
# Другим только предстояло проявить себя во всей красе.
# Однажды в Ваш кабинет уверенно постучался и вошел физрук. 
# Начал он свою историю издалека, что, мол, университету нужны таланты,
# что некому представлять ваше учебное заведения на международных 
# соревнованиях по плаванию. И словно невзначай спросил
# - "А нет ли у Вас на примете подходящих кандидатур? 
# Да еще чтоб хотя бы немного знали английский. 
# Ах да, еще и возрастное ограничение — не младше 20 лет". 

# Немного порывшись в памяти вы вспомнили тройку широкоплечих
# студентов-программистов, которые могли бы быть хорошими кандидатами.
# Но вот имен их, как ни старались, припомнить не смогли. 

# Однако вы знали, что при поступлении будущие студенты заполняли анкету.
# Потом же на основании этих анкет были созданы списки для разделения по
# изучаемому языку (чтобы учитывать ранее приобретенные знания и не смешивать
# языковые группы в одну кучу) и списки, описывающие хобби студентов. 
# Дело оставалось за малым — взять тех, кто знает английский и одновременно имеет интерес к спорту.
# Ну и совместить это дело со списком тех, кто перешагнул черту 20-летия, который был получен загодя

# Функция find_athlets принимает 3 списка с именами студентов.
# В первом списке (know_english) — список тех, кто хорошо владеет английским языком.
# Второй (sportsmen) — содержит имена тех, кто увлекается спортом.
# Ну и третий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет.
# Функция возвращает список имен студентов, которые подходят под все три критерия.  

know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]


def find_athlets(know_english, sportsmen, more_than_20_years):
    list_athlets = list(set(know_english)
                        & set(sportsmen)
                        & set(more_than_20_years))
    print(list_athlets)


if __name__ == '__main__':
    find_athlets(know_english, sportsmen, more_than_20_years)
