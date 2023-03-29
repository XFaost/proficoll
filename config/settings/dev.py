from config.settings.base import *

try:
    from config.settings.local import *
except ModuleNotFoundError:
    pass
