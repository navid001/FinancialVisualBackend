import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

instance_path = os.path.join(basedir, 'instance')
os.makedirs(instance_path, exist_ok=True)

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(instance_path, 'financial_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    
    INSTANCE_PATH = instance_path