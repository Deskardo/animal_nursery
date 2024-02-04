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

