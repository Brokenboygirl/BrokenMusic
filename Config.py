import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "9885470"))
    API_HASH = os.environ.get("API_HASH", "84ff6bdb8eeb6e8bedf8a8192e3da3dd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5303890134:AAHhOWza_Eq1XF-gOVbGxTWR7Nn4Yr2RN3s")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCFIWJ2h4c_po63UfOJNP1Krgb0UPUl6CXbbdd1dl7HXjbXRGZBOgqOrWVzaRQFEq4kXi8r9YOoiY_LGG-GV4fYdtksMk_0X2Cyh2LqpFQvGyu2_bc2K8Pkr8a7qVwag4zAX9mnli8-PcvFIP6rYnKP_vL8Wuzq5Zk_xbcPXMcW8WOF7QBY0IZoE0xPU7AkDKRJp76ogDoF3SF4yhGAkW2fGfP4OFIJFapqg1LeC44g5Qo9qQgA5mO6EtGt5CUGr_trJt3ub45lbsUFJcGLbVLLlBhCSfMh1HzuHL6wyD4ECT6thIhKmJlX2LSH0de-FgnzQKJfvmZCgAdHF6PQISxXAAAAAVN3_pUA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Lovely_Music_Assistant_bot")
    SUPPORT = os.environ.get("SUPPORT", "Lovelyfriends0000")
    CHANNEL = os.environ.get("CHANNEL", "Lovelyfriends0000")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "9885470"))
