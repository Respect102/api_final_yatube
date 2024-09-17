# API для Yatube
## 1. Описание
Возможности API для социальной сети Yatube:
- Регистрация
- Создавать/редактировать/удалять свои посты
- Оставлять/редактировать/удалять комментарии
- Просматривать посты других пользователей
- Подписываться на других пользователей
## 2. Установка и запуск
### Клонируем проект
```
git clone git@github.com:Respect102/api_final_yatube.git
```
### Переходим в директорию cd api_final_yatube/
```
cd api_final_yatube/
```
### Создаем виртуальное окружение (Windows) и активируем
```
python -m venv env
```
```
.env/Scripts/activate
```
### Запускаем проект
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
python manage.py runserver
```
## 3. Примеры
