1.- instalar modulos de una fuente en git 
    $ pip install -r requirements.txt
2.- instalar virtualenv
    $ pip install virtualenv
3.- crear un virtualenv 
    $ virtualenv <carpeta>
4.- activar el virtual env
    $ source nombre_entorno_virtual/bin/activate
5.- Desactivar el virtualenv
    $ deactivate
6.- actualizar modulos
    $ python3 -m pip install --upgrade requests
7.- instalar paquetes
    $ python3 -m pip install <paquete>



#instalar version de python
sudo apt install python3.6 python3.7 python3.8
# Agregar las versiones en prioridad
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 0
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
# seleccionar la versión a utilizar
sudo update-alternatives --config python


sudo apt install python3-pip

# instalar el paquete venv para cada versión específica.
# sudo apt install pythonX.x-venv
# instalar el paquete venv para 3.6
sudo apt install python3.6.venv
# instalar el paquete venv para 3.7
sudo apt install python3.7.venv
# instalar el paquete venv para 3.8
sudo apt install python3.8.venv
# suponiendo que esta activa 3.6, instalar venv con el nombre env
python -m venv env
# entrar al entorno
source env/bin/activate
# revisar la versión de python dentro del entorno
python --version