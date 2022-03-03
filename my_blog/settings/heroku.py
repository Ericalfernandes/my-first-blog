import environ
from my_blog.settings.base import * # trazendo tudo do base para esse arquivo

env = environ.Env()

DEBUG = env.bool("DEBUG", False) # (variável de ambiente, valor default)

SECRET_KEY = env("SECRET_KEY") 

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
#'myfirstblog-ericalfernandes.herokuapp.com/'

DATABASES = {
    "default": env.db(),
}