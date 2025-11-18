from . import LOGGER, bot_loop


async def main():
    """Main entry point for the bot."""
    LOGGER.info("Starting Mirror-Leech Telegram Bot MVP...")
    LOGGER.info("Bot initialization complete!")
    LOGGER.info("""\n
    ╔══════════════════════════════════════════════════╗
    ║  Mirror-Leech Telegram Bot MVP                  ║
    ║  Features: Mirror, Leech, Torrent, YT-DLP       ║
    ║  GDrive, Rclone, MongoDB, RSS, Search & More    ║
    ╚══════════════════════════════════════════════════╝

    """)
    LOGGER.info("Bot is ready to accept commands!")
    LOGGER.info("Please configure config.py before running.")
    LOGGER.info("Read README.md for detailed setup instructions.")


bot_loop.run_until_complete(main())

LOGGER.info("Bot Started!")
bot_loop.run_forever()