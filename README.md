# Калугин Алексей Викторович
04.02.2024
Группа: Разработчик | выходные | 4717
## Операционные системы и виртуализация Linux
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

## Объектно-ориентированное программирование
### Диаграмма классов
1. Создать диаграмму классов с родительским классом Животные
- Решение в файле UML.drawio


### Работа с MySQL
1. Создаем базу данных
~~~
CREATE DATABASE human_friends;
~~~
2. Создаем таблицы, соответствующие иерархии из диаграммы классов
~~~
DROP DATABASE IF EXISTS human_friends;
CREATE DATABASE human_friends;

USE human_friends;

CREATE TABLE animals
(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	subclass_name VARCHAR(20)
);

INSERT INTO animals (subclass_name)
VALUES ('pets'), ('pack_animals');

CREATE TABLE pets
(
	id INT AUTO_INCREMENT PRIMARY KEY, 
    class_id INT,
    type_of_pet VARCHAR(20),
    FOREIGN KEY (class_id) REFERENCES animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO pets (class_id, type_of_pet)
	 VALUES
			(1, 'dogs'),
            (1, 'cats'),
            (1, 'hamsters');

CREATE TABLE pack_animals
(
	id INT AUTO_INCREMENT PRIMARY KEY, 
    class_id INT,
    type_of_animal VARCHAR(20),
    FOREIGN KEY (class_id) REFERENCES animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO pack_animals (class_id, type_of_animal)
	 VALUES
			(2, 'horse'),
            (2, 'camal'),
            (2, 'donkey');
            
CREATE TABLE dogs (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    type_id INT, 
    birthday DATE,
    commands VARCHAR(50),
    Foreign KEY (type_id) REFERENCES pets (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cats (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    type_id INT, 
    birthday DATE,
    commands VARCHAR(50),
    Foreign KEY (type_id) REFERENCES pets (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE hamsters (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    type_id INT, 
    birthday DATE,
    commands VARCHAR(50),
    Foreign KEY (type_id) REFERENCES pets (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE horse (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    type_id INT, 
    birthday DATE,
    commands VARCHAR(50),
    Foreign KEY (type_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE camal (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    type_id INT, 
    birthday DATE,
    commands VARCHAR(50),
    Foreign KEY (type_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE donkey (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    type_id INT, 
    birthday DATE,
    commands VARCHAR(50),
    Foreign KEY (type_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

~~~
2. Заполняем значениями
~~~

INSERT INTO dogs (pet_name, type_id, birthday, commands)
VALUES
		('Max', 1, '2021-01-18', 'sit, down, stand'),
        ('Rex', 1, '2022-02-01', 'bark, come, stay'),
        ('Tiger', 1, '2019-10-10', 'hee, wait, take');

INSERT INTO cats (pet_name, type_id, birthday, commands)
VALUES
		('Aron', 1, '2023-01-15', 'sleep, put, spin'),
        ('Casper', 1, '2018-05-01', 'jump, belly, roll'),
        ('Colin', 1, '2020-09-07', 'go back, roll, down');
        
INSERT INTO hamsters (pet_name, type_id, birthday, commands)
VALUES
		('Alvin', 1, '2022-02-13', 'roll, jump, spin'),
        ('Chip', 1, '2023-04-07', 'roll, sleep, eat'),
        ('Dail', 1, '2023-05-04', 'roll, sleep, eat');
        
--------------------------------------------------------------------------------------------

INSERT INTO horse (pet_name, type_id, birthday, commands)
VALUES
		('Amori', 2, '2017-01-15', 'gait, walk, gallop'),
        ('Darkangel', 2, '2020-05-05', 'pace, walk, canter'),
        ('Amber', 2, '2018-03-12', 'jump, pull, halt');
        
INSERT INTO camal (pet_name, type_id, birthday, commands)
VALUES
		('Lila', 2, '2016-08-13', 'gait, walk, gallop'),
        ('Blum', 2, '2018-11-08', 'gait, walk, gallop');

INSERT INTO donkey (pet_name, type_id, birthday, commands)
VALUES
		('Wookey', 2, '2014-10-12', 'gait, walk, pull'),
        ('Dookey', 2, '2018-06-11', 'gait, walk, pull'),
        ('Jubilee', 2, '2017-02-10', 'gait, walk, pull');   
~~~
3. Удалить таблицу с верблюдами, объединить ослов и лошадей

~~~
DELETE FROM camal WHERE type_id = 2;

CREATE TABLE equidae
SELECT * FROM horse
		UNION 
SELECT * FROM donkey;
~~~

4.  - Создать новую таблицу для животных в возрасте от 1 до 3 лет и 
вычислить их возраст с точностью до месяца.

~~~
CREATE TEMPORARY TABLE temp_animals AS
SELECT * FROM dogs
		UNION
SELECT * FROM cats
		UNION
SELECT * FROM hamsters
		UNION
SELECT * FROM horse
		UNION
SELECT * FROM donkey;

CREATE TABLE young_animals
SELECT
	pet_name, type_id, birthday, commands, TIMESTAMPDIFF(MONTH, birthday, CURDATE()) AS age_in_month
FROM 
	temp_animals
WHERE birthday BETWEEN ADDDATE(CURDATE(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
~~~
5. Объединить все созданные таблицы в одну, 
сохраняя информацию о принадлежности к исходным таблицам.

~~~
CREATE TABLE friends

SELECT 
	dg.pet_name,
	p.type_of_pet as type_of_animal, 
	dg.birthday, 
	dg.commands,
	a.subclass_name
FROM dogs dg
LEFT JOIN pets p ON p.id = dg.type_id
LEFT JOIN animals a ON a.id = p.class_id
UNION
SELECT 
	ct.pet_name,
	p.type_of_pet as type_of_animal, 
	ct.birthday, 
	ct.commands,
	a.subclass_name
FROM cats ct
LEFT JOIN pets p ON p.id = ct.type_id
LEFT JOIN animals a ON a.id = p.class_id
UNION
SELECT 
	hm.pet_name,
	p.type_of_pet as type_of_animal, 
	hm.birthday, 
	hm.commands,
	a.subclass_name
FROM hamsters hm
LEFT JOIN pets p ON p.id = hm.type_id
LEFT JOIN animals a ON a.id = p.class_id
UNION
SELECT 
	hr.pet_name,
	pa.type_of_animal, 
	hr.birthday, 
	hr.commands,
	a.subclass_name
FROM horse hr
LEFT JOIN pack_animals pa ON pa.id = hr.type_id
LEFT JOIN animals a ON a.id = pa.class_id
UNION
SELECT 
	dk.pet_name,
	pa.type_of_animal, 
	dk.birthday, 
	dk.commands,
	a.subclass_name
FROM donkey dk
LEFT JOIN pack_animals pa ON pa.id = dk.type_id
LEFT JOIN animals a ON a.id = pa.class_id
UNION
SELECT 
	cm.pet_name,
	pa.type_of_animal, 
	cm.birthday, 
	cm.commands,
	a.subclass_name
FROM camal cm
LEFT JOIN pack_animals pa ON pa.id = cm.type_id
LEFT JOIN animals a ON a.id = pa.class_id
~~~

## Объектно-ориентированное программирование написание ПО
### Программа-реестр домашних животных