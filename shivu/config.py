class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6257270528"
    sudo_users = "6257270528"
    GROUP_ID = -1002082803552
    TOKEN = "7051461986:AAHOAv-SN8-UQzWwEUrjS98Jmxrim1gDB0k"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "MUSIC_CHAT_GRP"
    UPDATE_CHAT = "MUSIC_CHAT_GRP"
    BOT_USERNAME = "Fancy_Waifu_Husbando_Bot"
    CHARA_CHANNEL_ID = "-1002082803552"
    api_id = 22792918
    api_hash = "ff10095d2bb96d43d6eb7a7d9fc85f81"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
