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

2. Configura el archivo `config.py` en la raíz del proyecto:

~~~sh
touch config.py
~~~

~~~python
base_url: str = "https://<organization>.lockensmartaccess.com/"
account: str = "<account>"
username: str = "<username>"
password: str = "<password>"
users: list[str] = ["<id>" "<id>" "<id>"]
basename: str = "Access report"
# Optional, default previous week's Monday
start_date: str = "YYYY-MM-DD"
# Optional, default previous week's Friday
end_date: str = "YYYY-MM-DD"
~~~

3. Ejecuta el archivo `main.py`:

~~~sh
python3 main.py
~~~

## Autor

- [@srjimmy](https://www.github.com/srjimmy)

## Licencia

AutoLocken está sujeto a la licencia GNU General Public License v3.0
