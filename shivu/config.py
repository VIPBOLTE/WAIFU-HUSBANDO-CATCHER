class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7089408502"
    sudo_users = "7089408502"
    GROUP_ID = -1001529779762
    TOKEN = "7063220368:AAEty7C6Z0MrlmUpmPH81J-AhM7Jyum4oOI"
    mongo_url = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL =["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "NAMIKAZECPAN"
    UPDATE_CHAT = "NAMIKAZECPAN"
    BOT_USERNAME = "GUESSEM_ALL_ROBOT"
    CHARA_CHANNEL_ID = "-1002004197830"
    api_id = 24074986
    api_hash = "f4f6272a85d0e50e39a24cb378be118d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
