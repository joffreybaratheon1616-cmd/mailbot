#!/usr/bin/env python3
"""
Telegram Session Manager Bot
─────────────────────────────
"""
import logging
import sys

from telegram.ext import ApplicationBuilder

from config import BOT_TOKEN, API_ID, API_HASH, VERSION, OWNER_IDS
from database.db import db
from handlers import start, manage, guard, my_accounts, admin, owner_access, auto_hex
from utils.guard import GuardManager

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def post_init(application):
    await db.connect()
    logger.info("✅ MongoDB connected")
    logger.info("✅ Bot started")


async def post_stop(application):
    # Stop all running guard loops and disconnect their clients cleanly.
    manager = GuardManager(application)
    await manager.stop_all()
    await db.close()
    logger.info("🛑 MongoDB closed")


async def error_handler(update, context):
    """Log unhandled exceptions and surface them to the user in chat."""
    logger.error(
        "Exception while handling an update %s:", update, exc_info=context.error
    )
    try:
        if update is not None and update.effective_chat is not None:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"⚠️ **Error:** `{context.error}`",
            )
    except Exception:
        pass


def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN is not set. Configure env vars or config.py")
        sys.exit(1)
    if not API_ID or not API_HASH:
        logger.error("API_ID / API_HASH missing")
        sys.exit(1)

    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .post_stop(post_stop)
        .build()
    )
    application.add_error_handler(error_handler)

    # Register handlers (order matters for ConversationHandlers vs global)
    manage.register(application)
    guard.register(application)
    my_accounts.register(application)
    admin.register(application)
    owner_access.register(application)
    auto_hex.register(application)
    start.register(application)  # /start and back_main last

    logger.info("🚀 SessionBot v%s starting", VERSION)
    logger.info("Owners: %s", OWNER_IDS)
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
