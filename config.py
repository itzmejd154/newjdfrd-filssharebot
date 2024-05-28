#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6734478443:AAFJyqExvUDEvv57ki1GtV1p6gSwTBNzu8c")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20652787"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5dea928561e4d2eb77a371edf8b2eb2a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002066420558"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1357978966"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://evamusicbot:mrwaris04@cluster0.5ad8zuj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "DP_BOTZ")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001828719686"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ 👋 {first} ɪ ᴄᴀɴ ꜱᴛᴏʀᴇ Anime Toon Xyz ꜰɪʟᴇꜱ ✨ & ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ɪᴛ ꜰʀᴏᴍ ꜱᴩᴇᴄɪᴀʟ ʟɪɴᴋ 🔗")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1357978966 1242556540").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝗵𝗲𝗹𝗹𝗼 - {username} 𝗷𝗼𝗶𝗻 𝗺𝘆 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 👍 𝗡𝗲𝘅𝘁 𝗖𝗹𝗶𝗰𝗸 , 𝗧𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 ✅")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! You Need Own Bot Contact Developer @dp_botz"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
