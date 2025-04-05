# Foodgram: запуск

Клонируйте репозиторий

git clone git@github.com:Anfisa-Avdeeva/foodgram-st.git

Перейдите в директорию infra, создайте файл .env и заполните его на примере .env.example

cd foodgram-st/infra/
touch .env

Запустите проект

docker compose up

Выполните миграции

docker exec foodgram-backend python manage.py migrate.py

Загрузите ингредиенты в базу данных

docker exec foodgram-backend python manage.py load_inredients ingredients.json
