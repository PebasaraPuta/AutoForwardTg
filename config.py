from os import getenv

class Config(object):
      API_HASH = "d2e0ba99f1b9cdb632b43633edb76f11"
      API_ID = "2192067"     
      BOT_TOKEN = "2065095673:AAFhGM05CuUeklSYIYvOA4I3IUiXemiNl4Q"
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001756560471:-1001462147666").replace("\n", " ").split(' '))
