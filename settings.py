import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# GOOGLE CLOUD CONFIGURATION
PROJECT_ID = os.environ.get('PROJECT_ID')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

# FLASK APP SECRET KEY
SECRET_KEY = os.environ.get('SECRET_KEY')

# MYSQL DATABASE CONFIGURATION
MYSQL_UNIX_SOCKET= os.environ.get('MYSQL_UNIX_SOCKET')
MYSQL_REGION = os.environ.get('MYSQL_REGION')
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_INSTANCE_NAME = os.environ.get('MYSQL_INSTANCE_NAME')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')