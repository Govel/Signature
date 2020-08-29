from __future__ import print_function
import time
from typing import BinaryIO

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import re
import os
import shutil
import fileinput

class Watcher:
    DIRECTORY_TO_WATCH = "D:\\test"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event, a=int):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print (event)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print(event)
            with open("D://test/Signaturs/Sig1.txt", 'rb') as z:
                with open("D://test/Signaturs/Sig2.txt", 'rb') as k:
                    with open(event.src_path, 'rb') as f:
                        match = re.search(z.read(), f.read())
                        if match:
                            f.close()
                            z.close()
                            k.close()
                            print('Обнаружена вредоносная сигнатура что вы желаете сделать с файлом?[1/2/3/4]')
                            print("1.Удалить файл")
                            print("2.Попытаться вылечить файл")
                            print("3.Пропустить")
                            n = input("Введите команду: ")
                            if n == '1':
                                f.close()
                                z.close()
                                k.close()
                                os.remove(event.src_path)
                            elif n == "2":
                                replaceAll(event.src_path, "pervyi virusnyi fail", "")
                                replaceAll(event.src_path, "virus = 1", "")
                                print("Лечение выполнено!")
                            else:
                                print("Программа продолжает свою работу")
                        else:
                            f.close()
                            z.close()
                            k.close()
                            with open("D://test/Signaturs/Sig2.txt", 'rb') as k:
                                with open(event.src_path, 'rb') as f:
                                    match1 = re.search(k.read(), f.read())
                                    if match1:
                                        f.close()
                                        z.close()
                                        k.close()
                                        print('Обнаружена вредоносная сигнатура что вы желаете сделать с файлом?[1/2/3/4]')
                                        print("1.Удалить файл")
                                        print("2.Попытаться вылечить файл")
                                        print("3.Пропустить")
                                        n=input("Введите команду: ")
                                        if n == '1':
                                            f.close()
                                            z.close()
                                            k.close()
                                            os.remove(event.src_path)
                                        elif n == "2":
                                                replaceAll(event.src_path,"ya virus nomer 2","")
                                                replaceAll(event.src_path, "virus = 2", "")
                                                print("Лечение выполнено!")
                                        else:
                                            print("Программа продолжает свою работу")
        elif event.event_type == 'deleted':
            print("Received deleted event - %s." % event.src_path)
        elif event.event_type == 'renamed':
            # Taken any action here when a file is modified.
            print("Received renamed event - %s." % event.src_path)
class Revizor():
    print("1.Создать бэкап файлов")
    print("2.Восстановление файлов")
    print("3.Запустить сканирование файловой системы")
    print("4.Выход")
    inp = input("Введите команду [1/2/3/4]: ")
    if inp == "1":
        folder_from = 'D://test'
        nomer=input("Введите название папки куда будет сделана копия (папка будет создана, т.е. имя не должно существовать на момент создания): ")
        new_path = "D:\\%s" % (nomer)
        os.makedirs(new_path)
        for f in os.listdir(folder_from):
            if os.path.isfile(os.path.join(folder_from, f)):
                shutil.copy(os.path.join(folder_from, f), os.path.join(new_path, f))
            if os.path.isdir(os.path.join(folder_from, f)):
                shutil.copytree(os.path.join(folder_from, f), os.path.join(new_path, f))
        print("Бэкап создан")
        print("1.Создать бэкап файлов")
        print("2.Восстановление файлов")
        print("3.Запустить сканирование файловой системы")
        print("4.Выход")
        inp = input("Введите команду [1/2/3/4]: ")
        if inp == "1":
            folder_from = 'D://test'
            nomer = input("Введите название папки куда будет сделана копия (папка будет создана, т.е. имя не должно существовать на момент создания): ")
            new_path = "D:\\%s" % (nomer)
            os.makedirs(new_path)
            for f in os.listdir(folder_from):
                if os.path.isfile(os.path.join(folder_from, f)):
                    shutil.copy(os.path.join(folder_from, f), os.path.join(new_path, f))
                if os.path.isdir(os.path.join(folder_from, f)):
                    shutil.copytree(os.path.join(folder_from, f), os.path.join(new_path, f))
        elif inp == "2":
            inp2 = input("Введите имя папки бекапа из которой будет производиться восстановление: ")
            folder_from = "D:\\%s" % (inp2)
            new_path = "D://test"
            f = input("Введите название файла, который хотите восстановить: ")
            if os.path.isfile(os.path.join(folder_from, f)):
                shutil.copy(os.path.join(folder_from, f), os.path.join(new_path, f))
            if os.path.isdir(os.path.join(folder_from, f)):
                shutil.copytree(os.path.join(folder_from, f), os.path.join(new_path, f))
            print("Файл восстановлен")
        elif inp == "3":
            print("Программа ожидает какие-либо изменения в файловой системе")
            if __name__ == '__main__':
                print("Введите exit для выхода к выбору функциональности")
                w = Watcher()
                w.run()
        elif inp == "4":
            print("Выполнение завершенно!")
            exit(0)
            sys.exit
            os.abort()
    elif inp=="2":
        inp2=input("Введите имя папки бекапа из которой будет производиться восстановление: ")
        folder_from = "D:\\%s" % (inp2)
        new_path = "D://test"
        f=input("Введите название файла, который хотите восстановить: ")
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(new_path, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            shutil.copytree(os.path.join(folder_from, f), os.path.join(new_path, f))
        print("Файл восстановлен")
        print("1.Создать бэкап файлов")
        print("2.Восстановление файлов")
        print("3.Запустить сканирование файловой системы")
        print("4.Выход")
        inp = input("Введите команду [1/2/3/4]: ")
        if inp == "1":
            folder_from = 'D://test'
            nomer = input(
                "Введите название папки куда будет сделана копия (папка будет создана, т.е. имя не должно существовать на момент создания): ")
            new_path = "D:\\%s" % (nomer)
            os.makedirs(new_path)
            for f in os.listdir(folder_from):
                if os.path.isfile(os.path.join(folder_from, f)):
                    shutil.copy(os.path.join(folder_from, f), os.path.join(new_path, f))
                if os.path.isdir(os.path.join(folder_from, f)):
                    shutil.copytree(os.path.join(folder_from, f), os.path.join(new_path, f))
                print("Бэкап создан")
        elif inp == "2":
            inp2 = input("Введите имя папки бекапа из которой будет производиться восстановление: ")
            folder_from = "D:\\%s" % (inp2)
            new_path = "D://test"
            f = input("Введите название файла, который хотите восстановить: ")
            if os.path.isfile(os.path.join(folder_from, f)):
                shutil.copy(os.path.join(folder_from, f), os.path.join(new_path, f))
            if os.path.isdir(os.path.join(folder_from, f)):
                shutil.copytree(os.path.join(folder_from, f), os.path.join(new_path, f))
            print("Файл восстановлен")
        elif inp == "3":
            print("Программа ожидает какие-либо изменения в файловой системе")
            if __name__ == '__main__':
                w = Watcher()
                w.run()
        elif inp == "4":
            print("Выполнение завершенно!")
            exit(0)
            sys.exit
            os.abort()
    elif inp=="3":
        print("Программа ожидает какие-либо изменения в файловой системе")
        if __name__ == '__main__':
            w = Watcher()
            w.run()
    elif inp=="4":
        print("Выполнение завершенно!")
        exit(0)
        sys.exit
        os.abort()
Revizor