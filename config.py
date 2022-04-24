from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool('DEBUG')
TEMPLATE_FOLDER = env.str('TEMPLATE_FOLDER')
STATIC_FOLDER = env.str('STATIC_FOLDER')
SAVE_FOLDER = "/download"

