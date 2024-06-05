import sys
import site
import logging

# Путь к каталогу с вашим приложением
application_path = 'C:/Users/sumarn/MyFlaskApp'

# Если ваше приложение использует виртуальное окружение, добавьте путь к site-packages
site.addsitedir(application_path + '/venv/Lib/site-packages')

# Активация виртуального окружения
#activate_this = application_path + '/venv/Scripts/activate_this.py'
#with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

#sys.path.insert(0, application_path)
sys.path.insert(0, "C:/Users/sumarn/MyFlaskApp")  # Путь к вашему приложению Flask

# Настройка логирования
logging.basicConfig(stream=sys.stderr)
logging.getLogger("my_flask_app").setLevel(logging.DEBUG)

from app import app as application  # Импортируем экземпляр Flask из вашего приложения

 

# Этот код гарантирует, что ваше приложение Flask будет запущено через модуль WSGI
#if __name__ == "__main__":
#    application.run()