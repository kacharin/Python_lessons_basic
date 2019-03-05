# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# Не успеваю полностью проверить и доделать. Работает частично...
class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
 
    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname
 
    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())

class schoolchild(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class
  
class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
  
class Class:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}
 
 # Проверка
print('Не успеваю полностью проверить и доделать. Работает частично...')
print()
if __name__ == '__main__':
    teachers = [Teacher('Амиран', 'Сидорович', 'Убираев', 'Физкультура'),
                Teacher('Андрей', 'Олегович', 'Моль', 'Химия'),
                Teacher('Васген', 'Робертович', 'Бесконечный', 'Математика'),
                Teacher('Джон', 'Ашотович', 'Цукерман', 'Физика'),
                Teacher('Фёкла', 'Нурлановна', 'Поппинс', 'Английский')]
    classes = [Class('1А', [teachers[3], teachers[3], teachers[0]]),
               Class('2Б', [teachers[0], teachers[1], teachers[2]]),
               Class('3В', [teachers[1], teachers[3], teachers[4]])]
    parents = [People('Иван', 'Иванович', 'Иванов'),
               People('Ульяна', 'Ульяновна', 'Ульянова'),
               People('Тимур', 'Тимурович', 'Тимуров'),
               People('Наталья', 'Николаевна', 'Николаева'),
               People('Чингиз', 'Хасанович', 'Оглыев'),
               People('Мария', 'Иннокеньтьевна', 'Краснопресненская')]
    schoolchildren = [schoolchild('Газис', 'Бурханович', 'Волкодавов', parents[3], parents[2], classes[0]),
                schoolchild('Динара', 'Мухмаровна', 'Гульнарова', parents[0], parents[1], classes[1]),
                schoolchild('Арулон', 'Петрович', 'Абоев', parents[5], parents[4], classes[2])]
    print('Полный список всех классов в школе: ')
    for f in classes:
        print(f.class_room + '.')
    print() 
    for f in classes:
        print("Список всех учеников в классе {}:".format(f.class_room))
        for st in schoolchildren:
            print(st.get_short_name())
        print() 
    for f in classes:
        print('Список всех учителей, преподающих в {} классе:'.format(f.class_room))
        for teacher in classes[1].teachersdict.values():
            print(teacher.get_full_name() + '.')
        print()
