# from decouple import config
# import os
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# class Config:
#     SECRET_KEY=config('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)


# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI="sqlite:///"+ os.path.join(BASE_DIR, 'dev.db')
#     DEBUG=True
#     Sqlachemy_ECHO=True


# class ProdConfig(Config):
#     pass
# class TestConfig(Config):
#     pass






# #new
# from decouple import config
# import os

# BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# class Config:
#     SECRET_KEY = config('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)

# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'dev.db')
#     DEBUG = True
#     SQLALCHEMY_ECHO = True  # Fixed typo

# class ProdConfig(Config):
#     # Use the DATABASE_URL provided by Render for PostgreSQL
#     SQLALCHEMY_DATABASE_URI = config('postgresql://backend_o39f_user:b8YD1GFSbSe3GNi53qnJOcLI52g9ukDB@dpg-cudn230gph6c73ff3o8g-a.oregon-postgres.render.com/dev')  # Render will provide this
#     DEBUG = False
#     SQLALCHEMY_ECHO = False

# class TestConfig(Config):
#     pass

#new 2
from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY', default="mysecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool, default=False)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'dev.db')
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Fixed typo

class ProdConfig(Config):
    # Use the DATABASE_URL environment variable from Render
    SQLALCHEMY_DATABASE_URI = config('postgresql://backend_o39f_user:b8YD1GFSbSe3GNi53qnJOcLI52g9ukDB@dpg-cudn230gph6c73ff3o8g-a.oregon-postgres.render.com/dev', default="")
    DEBUG = False
    SQLALCHEMY_ECHO = False

class TestConfig(Config):
    pass
