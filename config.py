# Bot configuration
# Prefer environment variables (Railway / Docker). Fallbacks are for local only.
# NEVER commit real tokens to a public repository.

import os

def _int_list(val: str) -> list[int]:
    if not val:
        return []
    out = []
    for part in val.replace(" ", "").split(","):
        if part.isdigit():
            out.append(int(part))
    return out

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
API_ID = int(os.getenv("API_ID", "0") or "0")
API_HASH = os.getenv("API_HASH", "")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "sessionbot")
OWNER_IDS = _int_list(os.getenv("OWNER_IDS", ""))

# Optional tuning
VERSION = os.getenv("VERSION", "2.2")
ALLOW_LOGIN_SECONDS = int(os.getenv("ALLOW_LOGIN_SECONDS", "60") or "60")
GUARD_INTERVAL = int(os.getenv("GUARD_INTERVAL", "5") or "5")
IMAP_TIMEOUT_SECONDS = int(os.getenv("IMAP_TIMEOUT_SECONDS", "15") or "15")
