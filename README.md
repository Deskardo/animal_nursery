# Калугин Алексей Викторович
04.02.2024
Группа: Разработчик | выходные | 4717
### Использование команды cat в Linux
1. создам директорию с помощью команды mkdir
- mkdir /media/nursery
- cd /media/nursery
2. создание файлов с помощью команды cat
- cat Pets.txt

- dogs
- cats
- humsters

- CTRL + D
-----
- cat > Pack_animals.txt

- horses
- camels
- donkeys

- CTRL + D
---
3. Объединение файлов -> последующий просмотр
- cat Pets.txt>>Pack_animals.txt
- cat Pack_animals.txt
4. Переименовать файл
- mv Pack_animals.txt HumanFriends.txt
- ls -la
- /media/nursery# ls
HumanFriends.txt  Pets.txt

### Работа с директориями
1. Создать новую директорию переместить туда файл HumanFriends.txt
- mkdir /home/deskardo/PycharmProjects/pythonProject/animals
- mv HumanFriends.txt /home/deskardo/PycharmProjects/pythonProject/animals/HumanFriends.txt
- ls -la (проверить каталог)

### Работа с MySQL в Linux
1. Подключить дополнительный репозиторий и установить пакет
   (у меня возникли проблемы с этим пунктом, поэтому я поставил не из дополнительного репозитория)
- sudo apt update
- sudo apt install mysql-server mysql-client
- sudo mysql_secure_installation
- systemctl status mysql
- mysql

### Управление deb-пакетами
1. Уставновить и удалить deb-пакет использую команду dpkg
- sudo dpkg -i vivaldi-stable_6.5.3206.59-1_amd64.deb
- dpkg --get-selections (пришлось искать название установленного пакета)
- sudo dpkg -r vivaldi-stable


