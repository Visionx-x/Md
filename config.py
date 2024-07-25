import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 26360430
API_HASH = "4f7076fc90ac313f59d935d4e421efed"
BOT_TOKEN = "7327221868:AAH5oJeZ9K054Vy8FvZ_STgTJFsghNv6ELo"
MONGO_DB_URI = "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -1001861619812
OWNER_ID = 5016109398

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Visionx-x/Md",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/learningbots79")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/learningbots79")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFH1B8AM1lHkzpb3V6NfxE-Ii_oD_Kq4iIiZsl9-wH7133sRMVGUFJUy0Nk9oE7kTAaLfS7d-99zLcnSKwyUHovYspxvAl8Gr5cjXtn_FaImvBS5SHvBHV-uXJ_k2GGYx3fpdDvSCDGs1EYlgDlD_iJNenPBJLdK1elrbFgA7PBeHWVnJbzibd3SO19Qlylr7AjEebUatKdNU-44hYjMwV1L9fiVZ-KsQgCMViVGQ1CFpT4JC2zz324dBNOV4X7g70IUnBgae-4Kj65A3FpFOvj_OeEjAPJiRcstHvIexf22bgYY0F3iEDVmEZvS49QlhIOBChjxGmoLuGf578c6r7cAVDmWwAAAAGRiZIIAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
STATS_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
STREAM_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/cc290ee58069d09a1ade7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
