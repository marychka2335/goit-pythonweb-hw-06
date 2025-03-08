from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from database_config import url_to_db
from colorama import Fore, Style, init

# Ініціалізація colorama
init()

# Створення підключення до бази даних
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    # Перевірка підключення
    try:
        connection = engine.connect()
        print(Fore.GREEN + "Підключення до бази даних успішне!" + Style.RESET_ALL)
        connection.close()
    except Exception as e:
        print(Fore.RED + "Помилка підключення до бази даних:" + Style.RESET_ALL, e)
