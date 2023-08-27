<p align="center">
  <img alt="License GPL" src="https://img.shields.io/github/license/srjimmy/autolocken" />
</p>

# 📄 AutoLocken

Esta aplicación tiene como objetivo automatizar el proceso de generación de
ficheros de informes de accesos para un grupo de usuarios en un rango de fechas
dadas sin necesidad de utilizar la aplicación web
[Locken Smart Access](https://locken.lockensmartaccess.com/).

## Uso

1. Clona el repositorio:

~~~sh
git clone https://github.com/srjimmy/autolocken.git
~~~

2. Configura el archivo `config.json` en la raíz del proyecto:

~~~sh
touch config.json
~~~

~~~json
{
  "base_url": "https://<organization>.lockensmartaccess.com/",
  "account": "<account>",
  "username": "<username>",
  "password": "<password>",
  "users": ["<id>", "<id>", "<id>"],
  "basename": "Access report"
}
~~~

3. Ejecuta el archivo `main.py`:

~~~sh
python3 main.py
~~~

## Autor

- [@srjimmy](https://www.github.com/srjimmy)

## Licencia

AutoLocken está sujeto a la licencia GNU General Public License v3.0
