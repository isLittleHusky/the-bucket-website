import os

basedir = os.path.abspath(os.path.dirname(__file__))


def get_env_variable(name):

	try:
	 	return os.environ[name]

	except KeyError:
		message = f'expected environemt variable \'{name}\' not set'
		raise Exception(message) 

class Config(object):
	SECRET_KEY = get_env_variable('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = 'postgresql://bucketadmin:Qwas12!@@localhost:5432/bucket'
'''
	POSTGRES_URL = get_env_variable('POSTGRES_URL')
	POSTGRES_USER = get_env_variable('POSTGRES_USER')
	POSTGRES_PW = get_env_variable('POSTGRES_PW')
	POSTGRES_DB = get_env_variable('POSTGRES_DB')
'''

