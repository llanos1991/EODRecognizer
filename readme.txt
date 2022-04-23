#################DESARROLLO DEL PROYECTO SIDE#############

#instalar version de python
    $ sudo apt install python3.6 python3.7 python3.8

# Agregar las versiones en prioridad
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 0
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

# seleccionar la versión a utilizar
    $ sudo update-alternatives --config python

# instalar pip3 gestor de paquetes de python3
    $ sudo apt install python3-pip 

# instalar virtualenv
    $ pip3 install virtualenv

# crear un virtualenv 
    $ virtualenv <carpeta>

# activar el virtual env
    $ source nombre_entorno_virtual/bin/activate

# actualizar modulos
    $ python3 -m pip install --upgrade requests

# agregar requirements.txt con pip3 
    $ pip3 freeze > requirements.txt

# instalar paquetes
    $ pip3 install <module>
 
# instalar dependencias
    $ pip3 install -r requirements.txt

NOTA:  instalar modulos de una fuente en git:  $ pip install -r requirements.txt

# Desactivar el virtualenv
    $ deactivate

