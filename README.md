# stallmanenjujuy.org

## Descripción

Este sitio fue desarrollado en marco de la visita del Dr. Richard Matew Stallman a la Provincia de Jujuy y te invitamos a colaborar en el. Lo construimos con [Pelican](https://blog.getpelican.com/) utilizando para mejor visualización pelican-bluidea. Pelican es desarrollado con tecnologías Python y Jinja2. Puede ser accedido por cualquier navegador web sin necesidad de activar la ejecución de Javascript. Los motivos se explican en [gnu.org/philosophy/javascript-trap.html](http://gnu.org/philosophy/javascript-trap.html).
Si querés crear tu entorno de desarrollo para trabajar con este proyecto, necesitás seguir los siguientes pasos.

## Instalación del entorno de desarrollo

El primer paso es instalar el paquete `virtaulenv` en tu computadora. Este te permitirá crear *entornos virtuales* para la aplicación, es decir, permite crear un directorio independiente que contenga una copia del binario de Python y directorio de paquetes, además de instalar/actualizar paquetes requeridos por tu aplicacion sin necesidad de modificar la instancia global de paquetes Python. Para más detalles, te recomendamos consultar [virtuaenv site](https://virtualenv.pypa.io/en/stable/)
La instalación la podés realizar desde línea de comando a través del gestor de paquetes de Python llamado `pip`:
```
# pip install virtualenv
```
> Te sugerimos realizar un `Fork` de este repositorio a fin de que puedas realizar los cambios con total libertad y, si luego tenés mejoras para el mismo, solicitá un `Pull Request`.

Una vez realizado el `Fork`, debés clonar el repositorio (ejemplo desde la consola):
```
git clone https://github.com/jorgex9/stallmanpelican
```
A partir de ese momento, podés acceder al directorio del proyecto y activar el `virtual evironment`:
```
cd stallmanpelican
virtualenv venv
source venv/bin/activate
```
Luego, instalás los paquetes Pelican y Markdown:
```
pip install pelican
pip install Markdown
```
## Instalación de Pelican Theme
Para ello tenés que clonar el theme que usamos desde el repositorio:
```
git clone https://github.com/jorgex9/pelican-blueidea.git
```
Para instalar el theme, empleás la herramienta pelican-theme que, además, permite listar los themes instalados:
```
pelican-themes --install /path/pelican-blueidea --verbose
pelican-themes -l
```
## Crear entradas
Las entradas se escriben en el directorio  `content`, con formato Markdown.
Para que Pelican genere el html del sitio estático con las nuevas entradas o cambios realizados, ejecutá:

```
make html
```
## Ejecutar el servidor de pruebas
Con el fin de obtener una vista preva del sitio, una buena práctica es ejecutar el servidor HTTP integrado de Pelican:

```
cd output
python -m pelican.server
```
Con ese comando se inicia un servidor web básico para poder previsualizar los cambios que realizás. Desde tu navegador preferido, ingresá la siguiente dirección web:
[http://localhost:8000](http://localhost:8000)


### Enlaces de interés
- Documentacion oficial [http://docs.getpelican.com/en/3.6.3/index.html](http://docs.getpelican.com/en/3.6.3/index.html)
- How to setup Pelican blog  [http://igbt6.github.io/blog/how-to-setup-pelican-blog.html](http://igbt6.github.io/blog/how-to-setup-pelican-blog.html)
- Pelican Themes [http://www.pelicanthemes.com/](http://www.pelicanthemes.com/)