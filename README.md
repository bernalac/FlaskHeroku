# FlaskHeroku
Aplicación escrita en python con la funcionalidad de enseñar diferentes textos en pantalla, usando GET.
Desplegada en Heroku.

### URL Heroku
https://flaskhero.herokuapp.com/

### Funcionamiento hello.py
-----       
*URL 1*: URL/person/mary     
*URL 2*: URL/login?username=paolo&password=thehidden      
*URL 3*: URL/person/robert/edad/36              
*URL 4*: URL/advices    


### Pasos seguidos para desplegar en Heroku
```
    Fichero Procfile
    Fichero requirements.txt
    $ git init (raíz proyecto)
    $ git add .
    $ git commit -m "first commit"
    $ heroku login
    $ heroku create
    $ heroku rename nuevoNombreProy
    $ git push heroku master
```

### Fichero Procfile y requirements.txt
Las aplicaciones de Heroku incluyen un Procfile que especifica los comandos que ejecuta la aplicación al inicio. Puede utilizar un Procfile para declarar una variedad de tipos de procesos, que incluyen:

    El servidor web de su aplicación
    Múltiples tipos de procesos de trabajo
    Un proceso singleton, como un reloj
    Tareas para ejecutar antes de implementar una nueva versión

El archivo requirements. txt permite automatizar la instalación de paquetes y así se consigue:
```
    $ pip3 freeze > requiremets.txt
```

## Authors

* **Javier Bernal** - *Initial work* 
