import os

class Config:
    # ===== RexBots Original Config =====

    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    USER_ID = int(os.getenv("USER_ID", "5770911041"))
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    DB_NAME = os.getenv("DB_NAME", "manga")
    DB_URL = os.getenv("DB_URL", "")
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "300"))
    MAX_CHAPTERS_PER_CHECK = int(os.getenv("MAX_CHAPTERS", "5"))
    DOWNLOAD_DIR = "downloads"
    STATE_FILE = "bot_state.json"
    CACHE_FILE = "manga_ids_cache.json"
    API_BASE = "https://api.mangadex.org"
    WEB_BASE = "https://mangadex.org"
    LOOKBACK_HOURS = 24
    MAX_IMAGE_SIZE = 10 * 1024 * 1024
    MAX_PDF_SIZE = 50 * 1024 * 1024
    USE_DATABASE = os.getenv("USE_DATABASE", "True").lower() == "true"

    PORT = int(os.getenv("PORT", "8080"))
    TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

    PICS = [
        "https://ibb.co/VYSPzSDH",
        "https://ibb.co/rGTqCwBV",
        "https://ibb.co/r2QZ0T0q",
        "https://ibb.co/67kGFzC5",
        "https://ibb.co/gZh6qysN",
        "https://ibb.co/0ysjvb0t",
        "https://ibb.co/7dGbyPvk"
    ]

    DEFAULT_FILENAME_FORMAT = "{manga_name} [Ch-{chapter}]"


    # ===== Added From AutoAnime Repo =====

    __version__ = os.getenv("VERSION", "v0.1@stable.july")

    # Telegram Session
    SESSION = os.getenv("SESSION", None)

    # Mongo Database (if needed separately)
    MONGO_SRV = os.getenv("MONGO_SRV", None)

    # Channel / Admin IDs
    BACKUP_CHANNEL = int(os.getenv("BACKUP_CHANNEL", "0"))
    MAIN_CHANNEL = int(os.getenv("MAIN_CHANNEL", "0"))
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
    CLOUD_CHANNEL = int(os.getenv("CLOUD_CHANNEL", "0"))
    FORCESUB_CHANNEL = int(os.getenv("FORCESUB_CHANNEL", "0"))
    OWNER = int(os.getenv("OWNER", "0"))

    # Other Configs
    THUMB = os.getenv(
        "THUMBNAIL",
        "https://graph.org/file/ad1b25807b81cdf1dff65.jpg"
    )

    FFMPEG = os.getenv("FFMPEG", "ffmpeg")
    CRF = os.getenv("CRF", "27")

    SEND_SCHEDULE = os.getenv("SEND_SCHEDULE", "False").lower() == "true"
    RESTART_EVERDAY = os.getenv("RESTART_EVERDAY", "True").lower() == "true"
    LOG_ON_MAIN = os.getenv("LOG_ON_MAIN", "False").lower() == "true"

    FORCESUB_CHANNEL_LINK = os.getenv("FORCESUB_CHANNEL_LINK", "")

    # Dev Config
    DEV_MODE = os.getenv("DEV_MODE", "False").lower() == "true"
