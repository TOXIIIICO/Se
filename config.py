import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 20551716))

    API_HASH = os.environ.get("API_HASH", "564355da021dc5739c01f33fb015eaf1")
