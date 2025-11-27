David Norberto Ruiz Suasnavar 202108070 Para correrlo se necesita una imagen de python y una de Mysql 9

Comando para correr: docker-compose up

Crear Super Usuario para el login: docker-compose run web python manage.py createsuperuser

Ingreso de datos: docker-compose run web python manage.py load_movies

Crear migraciones: docker-compose run web python manage.py migrate
