import os


class Config:
    #Security
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    #Debug mode
    DEBUG = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1", "t")
    #Permitted origins for CORS
    CORS_ORIGINS = os.environ.get("CORS_ORIGIN", "*")

    #Chat rooms
    CHAT_ROOMS = [
        "General",
        "El liseo",
        "Code with"
    ]