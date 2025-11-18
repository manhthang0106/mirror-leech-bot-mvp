# Mirror-Leech Telegram Bot MVP

A simplified MVP version of [anasty17/mirror-leech-telegram-bot](https://github.com/anasty17/mirror-leech-telegram-bot) with all core features.

## Features Included

✅ **Basic Mirror/Download** - Download files from direct links using aria2c  
✅ **Torrent Mirroring (qBittorrent)** - Download torrents with web interface  
✅ **Telegram Leech** - Upload files directly to Telegram with splitting  
✅ **YouTube Download (yt-dlp)** - Download from YouTube and 1000+ sites  
✅ **Google Drive Integration** - Upload to GDrive with service accounts  
✅ **Rclone Cloud Upload** - Upload to any rclone-supported cloud  
✅ **Status & Progress Tracking** - Real-time download/upload status  
✅ **User Authorization System** - Control who can use the bot  
✅ **Task Management** - Cancel tasks, queue system  
✅ **MongoDB Database** - Persistent storage for settings  
✅ **RSS Feed Monitor** - Auto-download from RSS feeds  
✅ **Torrent Search** - Search torrents with API/plugins  
✅ **JDownloader Integration** - Premium links support  
✅ **Sabnzbd/NZB Support** - Usenet downloads  

## Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Telegram API ID & Hash from [my.telegram.org](https://my.telegram.org)
- MongoDB Database (optional but recommended)

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/manhthang0106/mirror-leech-bot-mvp.git
cd mirror-leech-bot-mvp
```

### 2. Configuration

```bash
cp config_sample.py config.py
```

Edit `config.py` and fill in required fields:

```python
# REQUIRED
BOT_TOKEN = "your_bot_token_from_botfather"
OWNER_ID = 123456789  # Your Telegram user ID
TELEGRAM_API = 12345678  # From my.telegram.org
TELEGRAM_HASH = "your_api_hash"  # From my.telegram.org

# RECOMMENDED
DATABASE_URL = "mongodb+srv://user:pass@cluster.mongodb.net/"  # MongoDB connection string
AUTHORIZED_CHATS = "123456789 -100123456789"  # Space-separated user/chat IDs
```

### 3. Deploy with Docker

#### Option A: Docker Compose (Recommended)

```bash
sudo docker compose up --build
```

#### Option B: Docker Commands

```bash
sudo docker build . -t mltb-mvp
sudo docker run --network host mltb-mvp
```

### 4. Stop the Bot

```bash
# Docker Compose
sudo docker compose stop

# Docker
sudo docker ps  # Get container ID
sudo docker stop <container_id>
```

## Configuration Guide

### Required Settings

| Variable | Description | How to Get |
|----------|-------------|------------|
| `BOT_TOKEN` | Telegram bot token | [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Your Telegram user ID | [@userinfobot](https://t.me/userinfobot) |
| `TELEGRAM_API` | Telegram API ID | [my.telegram.org](https://my.telegram.org) |
| `TELEGRAM_HASH` | Telegram API hash | [my.telegram.org](https://my.telegram.org) |

### Optional Settings

**Database**
- `DATABASE_URL` - MongoDB connection string for persistent storage

**Authorization**
- `AUTHORIZED_CHATS` - Space-separated chat/user IDs that can use the bot
- `SUDO_USERS` - Space-separated user IDs with admin privileges

**Google Drive**
- `GDRIVE_ID` - Google Drive folder ID or `root`
- `IS_TEAM_DRIVE` - Set `True` if using Team Drive
- `USE_SERVICE_ACCOUNTS` - Set `True` to use service accounts
- `INDEX_URL` - Your GDrive index URL

**Rclone**
- `RCLONE_PATH` - Default rclone remote path (e.g., `myremote:folder`)
- `RCLONE_FLAGS` - Additional rclone flags

**Leech Settings**
- `LEECH_SPLIT_SIZE` - File split size in bytes (default: 2GB)
- `AS_DOCUMENT` - Upload as document or media
- `LEECH_DUMP_CHAT` - Chat ID to upload files

**Torrent Settings**
- `BASE_URL` - Your server URL for torrent file selection
- `BASE_URL_PORT` - Port for web interface (default: 80)
- `TORRENT_TIMEOUT` - Timeout for dead torrents

**Queue System**
- `QUEUE_ALL` - Total parallel tasks
- `QUEUE_DOWNLOAD` - Parallel downloads
- `QUEUE_UPLOAD` - Parallel uploads

**RSS**
- `RSS_DELAY` - Refresh interval in seconds (default: 600)
- `RSS_CHAT` - Chat ID for RSS notifications

**Search**
- `SEARCH_API_LINK` - Torrent search API URL
- `SEARCH_PLUGINS` - List of qBittorrent search plugin URLs

## Generate Credentials

### Google Drive Token

1. Get `credentials.json` from [Google Cloud Console](https://console.developers.google.com/)
2. Run:
```bash
pip3 install -r requirements-cli.txt
python3 generate_drive_token.py
```

### Telegram User Session

```bash
python3 generate_string_session.py
```

Add the output to `USER_SESSION_STRING` in config.py

### Service Accounts (for GDrive)

```bash
python3 gen_sa_accounts.py --create-sas YOUR_PROJECT_ID
python3 gen_sa_accounts.py --download-keys YOUR_PROJECT_ID
```

Then add service accounts to your Team Drive:

```bash
python3 add_to_team_drive.py -d YOUR_TEAM_DRIVE_ID
```

## Bot Commands

Set these commands in [@BotFather](https://t.me/BotFather):

```
mirror - Mirror to cloud
leech - Leech to Telegram
qbmirror - Mirror torrent (qBittorrent)
qbleech - Leech torrent (qBittorrent)
ytdl - Download with yt-dlp
ytdlleech - Leech with yt-dlp
clone - Clone GDrive files
status - Get status
cancel - Cancel a task
cancelall - Cancel all tasks
rss - RSS menu
search - Search torrents
auth - Authorize user/chat
unauth - Unauthorize user/chat
help - Get help
```

## Architecture

This MVP follows the same architecture as the parent repository:

```
├── bot/
│   ├── __init__.py          # Global variables, locks, scheduler
│   ├── __main__.py          # Entry point
│   ├── core/                # Core managers (config, client, startup)
│   ├── helper/              # Utilities and listeners
│   └── modules/             # Command handlers
├── config_sample.py         # Configuration template
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose config
└── start.sh                # Startup script
```

## Dependencies

All dependencies match the parent repository versions:

- **Telegram**: kurigram (pyrogram fork), tgcrypto
- **Download Managers**: aioaria2, aioqbt, sabnzbdapi
- **Cloud Upload**: google-api-python-client, rclone
- **Video Download**: yt-dlp with curl-cffi support
- **Database**: pymongo
- **Web Interface**: fastapi, uvicorn, jinja2
- **Performance**: uvloop (fast event loop)
- **Scheduling**: apscheduler
- **Utilities**: aiofiles, aioshutil, psutil, pillow

## Important Notes

1. **This is an MVP** - It includes the core structure but requires the full parent repository code for complete functionality
2. **Read parent repo docs** - For detailed feature usage, see [anasty17/mirror-leech-telegram-bot](https://github.com/anasty17/mirror-leech-telegram-bot)
3. **Docker base image** - Uses `anasty17/mltb:latest` which includes aria2c, qBittorrent, rclone, ffmpeg, etc.
4. **Port requirements** - Ensure ports 80, 8070, 8090 are open for web interfaces
5. **MongoDB recommended** - For persistent settings and RSS data

## Troubleshooting

**Bot won't start**
- Check `BOT_TOKEN` is correct
- Verify all required config fields are filled
- Check logs: `sudo docker compose logs`

**Can't download**
- Ensure you're authorized (check `AUTHORIZED_CHATS`)
- Verify download services are running
- Check firewall/ports

**Database connection failed**
- Verify `DATABASE_URL` is correct
- Check MongoDB cluster is accessible
- Whitelist your IP in MongoDB settings

## Credits

- **Parent Repository**: [anasty17/mirror-leech-telegram-bot](https://github.com/anasty17/mirror-leech-telegram-bot)
- **Original Bot**: [lzzy12/python-aria-mirror-bot](https://github.com/lzzy12/python-aria-mirror-bot)

## License

This MVP follows the same license as the parent repository.

## Support

For full documentation and support:
- **Parent Repo**: https://github.com/anasty17/mirror-leech-telegram-bot
- **Telegram Channel**: https://t.me/mltb_official_channel
- **Telegram Group**: https://t.me/mltb_official_support

---

**Note**: This is a minimal viable product (MVP) version. For production use, please refer to the complete parent repository with all modules, handlers, and features fully implemented.