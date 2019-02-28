def goto():
    dirgo = input('Введите полный путь до директории в которую хотите перейти: ')
    try:
        os.chdir(dirgo)
        print('Вы успешно перешли в нужную диреткорию.')
        action()
    except:
        print('Что то пошло не так... Не удалось изменит директорию.')
        action()

def listdir():
    print('Содержание текущей директории:')
    print(os.listdir())
    action()

def makedir():
    dirmake = input('Введите название директории которую хотите создать: ')
    try:
        os.mkdir(dirmake)
        print('Вы успешно создали нужную диреткорию.')
        action()
    except:
        print('Что то пошло не так... Не удалось создать директорию.')
        action()

def removedir():
    dirremove = input('Введите название директории которую хотите создать: ')
    try:
        os.rmdir(dirremove)
        print('Вы успешно удалили нужную диреткорию.')
        action()
    except:
        print('Что то пошло не так... Не удалось удалить директорию.')
        action()

def exitprog():
    pass

def action():
    actiondo = input('Введите цифру, которая соответсвует нужному действию: ')
    if  bool(whattodo.get(actiondo)) == True:
        whattodo(actiondo)
    else:
        print('Такого действия пока нет... Повторите попытку!')
        action()
