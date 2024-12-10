from util.util import read_configs
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)


class PGDatabase():
    def __init__(self):
        self.configs = read_configs(filename='configs.json')
        self.__db = None
    

    def connect_db(self):
        conf = self.configs['database']
        try:
            logging.info('trying to connect to database...')
            self.__db = psycopg2.connect(
                database = conf['database_name'],
                user = conf['user'],
                password = conf['password'],
                host = conf['host'],
                port = conf['port']
            )
            
            logging.info('Successfully connected to database.')
            return self.__db

        except Exception as e:
            logging.error(f'Failed to connect to database. Error: {e}')
            return None

    @property
    def db(self):
        if not self.__db:
            return self.connect_db()

        return self.__db