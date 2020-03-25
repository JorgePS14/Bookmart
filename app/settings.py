from os import environ

DB_CONNECTION = environ.get('DB_CONNECTION')
DB_HOST = environ.get('DB_HOST')
DB_PORT = environ.get('DB_PORT', 3306)
DB_DATABASE = environ.get('DB_DATABASE')
DB_USERNAME = environ.get('DB_USERNAME')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_NAME = environ.get('DB_NAME')
