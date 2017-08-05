from peewee import *
from config_reader import ConfigReader

config = ConfigReader('settings.ini').config
mydb = MySQLDatabase(
    config['db_name'],
    host=config['db_ip'],
    port=int(config['db_port']),
    user=config['db_user'],
    passwd=config['db_pw'])


class BaseModel(Model):
    """A base model that uses our MySQL db"""
    class Meta:
        database = mydb
