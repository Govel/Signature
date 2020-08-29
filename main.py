import os


# Функция переходит в папку с введенным путем,
# и запускает поиск по сигнатуре
def search(arg):
    try:
        os.chdir(arg)
        files = os.listdir(arg)
        cwd = os.getcwd()
        print('Текущий путь: ' + cwd)
        signature(files)
    except IOError:
        print('Неверно указан путь, повторите ввод')
        arg = input()
        search(arg)


# Search signature
def signature(files):
    print("!!!")
    signatures = os.listdir(".\\signature")
    for j in range(len(files)):
        for i in range(len(signatures)):
            try:
                file = open(files[i], "rb")
                sign = open(signatures[i], "rb")
                if file.read() == sign.read():
                    print("Найден опасный файл - " + files[j])
                    file.close()
                    sign.close()
                    print("Что желаете сделать с файлом?")
                    print('1 - удалить, 2 - вылечить, 3 - закрыть программу')
                    command = input()
                    if command == "1":
                        delete(files[j])
                    elif command == "2":
                        print('В разработке')
                        # treatment(files[j], signatures[i])
                    elif command == "3":
                        raise SystemExit(1)
            except IOError:
                print('111', files[i])


# Delete file
def delete(file):
    path = os.path.join(os.path.abspath(os.path.dirname(r'%s' % __file__)), file)
    os.remove(path)
    print("Файл " + file + " удален")


# Quarantine
def quarantine(file):
    path = os.path.join(os.path.abspath(os.path.dirname(r'%s' % __file__)), file)
    os.chmod(path, 000)
    with open('./quarantine/quarantine', 'a', encoding='utf-8') as quarantines:
        quarantines.write(file + ' - ' + path + '\n')
        quarantines.close()
    print('Файл был помещен на карантин')


# Interface
def interface():
    print("Доступные команды: 1 - сканирование, 2 - файлы на карантине")
    print("Введите команду:")
    command = input()
    if command == '1':
        print('Введите путь до папки')
        arg = input()
        search(arg)
    elif command == '2':
        print("Файлы на карантине")
        try:
            rq = open('.\\quarantine\\quarantine', encoding='utf-8')
            print(rq.read())
            rq.close()
        except IOError:
            print("Карантин пуст")
        command = input("1 - назад")
        if command == 1:
            interface()


# Run program
interface()
print('\nНажмите Enter для выхода из программы.')
input()
