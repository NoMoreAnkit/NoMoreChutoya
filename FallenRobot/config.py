class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "27686987"
    API_HASH = "372ff3894497b52f59daeaa1d5f14a25"

    CASH_API_KEY = "1T4JPU6WMF1DG7EI"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://erirysrq:mINqoWcYIbmymJvTFipMeueoTHXXU2aI@snuffleupagus.db.elephantsql.com/erirysrq"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001813021140"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sastahacker:otpbypass@cluster0.ocj1y0u.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/3a654608a6bc159bf9d4b.jpg"

    SUPPORT_CHAT = "timepassxdman"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5825059025:AAFxLt4EUKbO9rUqspT2mSXJI6g1HsvuW6I"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "EK8JNZ13XPB8"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5672027235  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = "5672027235"  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
