import os
import logging
from app import create_app, db
from app.database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_database():
    try:

        basedir = os.path.abspath(os.path.dirname(__file__))
        instance_path = os.path.join(basedir, 'instance')
        
        os.makedirs(instance_path, exist_ok=True)
        logger.info(f"Instance directory confirmed at: {instance_path}")
        
        app = create_app()
        
        logger.info(f"Using database at: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        with app.app_context():
            logger.info("Creating database tables...")
            db.create_all()
            
            logger.info("Populating database with initial data...")
            init_db()
            
            logger.info("Database initialization completed successfully!")
            
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        logger.error(f"Current working directory: {os.getcwd()}")
        raise

if __name__ == "__main__":
    initialize_database()