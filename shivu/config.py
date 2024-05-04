class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6352061770"
    sudo_users = "6352061770", "6176582997"
    GROUP_ID = -1001916618183
    TOKEN = "7159220855:AAF8SMfMDgI3IQU0i1vObY5-mCNu42v_CGY"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "+oJoTUUJzem80ZTFl"
    UPDATE_CHAT = "animetubeworld"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1001916618183"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
