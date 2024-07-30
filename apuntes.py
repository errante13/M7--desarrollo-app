# PRIMERO: crear un entorno virtual en la consola

""" python -m venv Nombre_del_entorno """

# SEGUNDO: iniciar script activate 

""" .\ nombre_del_entorno \Scripts\activate.bat"""

# TERCERO: instalar django en el entorno virtual

""" pip install django"""

# CUARTO: iniciar un proyecto con django-admin  

""" django-admin startproject (nombre_del_proyecto)"""

# ingresar al directorio: cd proyecto_capitulo_1

# QUINTO: iniciamos una app con django-admin 

""" python manage.py startapp Nombre_app """

# SEXTO: Crear superUsuario

""" python manage.py createsuperuser """ 

# ------ GENERAR MIGRACIONES ------

#PRIMERO Crear archivo de migraciones en django
""" python manage.py makemigrations """

# después aplicar las migraciones creadas o pendientes 
 
""" python manage.py migrate """

# ------  ----------------  ------

# ingresar a la shell de python 
 
""" python manage.py shell """

# para mysql utilizamos el conector mysqlclient
""" pip install mysqlclient """
# para postgresql utilizamos el conector psycopg2
""" pip install psycopg2 """

# revertir migraciones de una app

""" python manage.py migrate nombreapp zero """ 

#dumpdata para crear un archivo con los datos de un modelo 
# debe posicionarse en el lugar donde quedará guardado el archivo  
""" python manage.py dumpdata --indent 2 nombreapp.nombredelmodelo > nombre_archivo """

#loaddata para cargar archivos desde un json a la base de datos

""" python manage.py loaddata nombre_archivo """