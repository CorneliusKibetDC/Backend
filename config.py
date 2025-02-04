# # from decouple import config
# # import os
# # BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# # class Config:
# #     SECRET_KEY=config('SECRET_KEY')
# #     SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)


# # class DevConfig(Config):
# #     SQLALCHEMY_DATABASE_URI="sqlite:///"+ os.path.join(BASE_DIR, 'dev.db')
# #     DEBUG=True
# #     Sqlachemy_ECHO=True


# # class ProdConfig(Config):
# #     pass
# # class TestConfig(Config):
# #     pass






# # #new
# # from decouple import config
# # import os

# # BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# # class Config:
# #     SECRET_KEY = config('SECRET_KEY')
# #     SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)

# # class DevConfig(Config):
# #     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'dev.db')
# #     DEBUG = True
# #     SQLALCHEMY_ECHO = True  # Fixed typo

# # class ProdConfig(Config):
# #     # Use the DATABASE_URL provided by Render for PostgreSQL
# #     SQLALCHEMY_DATABASE_URI = config('postgresql://backend_o39f_user:b8YD1GFSbSe3GNi53qnJOcLI52g9ukDB@dpg-cudn230gph6c73ff3o8g-a.oregon-postgres.render.com/dev')  # Render will provide this
# #     DEBUG = False
# #     SQLALCHEMY_ECHO = False

# # class TestConfig(Config):
# #     pass

# #new 2
# from decouple import config
# import os

# BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# class Config:
#     SECRET_KEY = config('SECRET_KEY', default="mysecretkey")
#     SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool, default=False)

# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'dev.db')
#     DEBUG = True
#     SQLALCHEMY_ECHO = True  # Fixed typo

# class ProdConfig(Config):
#     # Use the DATABASE_URL environment variable from Render
#     SQLALCHEMY_DATABASE_URI = config('postgresql://backend_o39f_user:b8YD1GFSbSe3GNi53qnJOcLI52g9ukDB@dpg-cudn230gph6c73ff3o8g-a.oregon-postgres.render.com/dev', default="")
#     DEBUG = False
#     SQLALCHEMY_ECHO = False

# class TestConfig(Config):
#     pass

#latest
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'dev.db')}"
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProdConfig(Config):
    # Get database credentials
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST', 'localhost')  # Default to localhost
    DB_PORT = os.getenv('DB_PORT', '5432')  # Default to 5432
    DB_NAME = os.getenv('DB_NAME')
    # Ensure all required environment variables are set
    if not DB_USER or not DB_PASSWORD or not DB_NAME:
        raise ValueError("Missing required database credentials (DB_USER, DB_PASSWORD, DB_NAME).")

    # Construct the DATABASE_URL correctly
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DEBUG = False
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_ECHO = False
    TESTING = True
    