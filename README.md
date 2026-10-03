# Mail / Session Manager Bot

Telegram session management bot with:

- Manage accounts (hex / string / .session)
- Device dashboard, terminate sessions, clear data
- Fetch OTP, change login email, 2FA
- **One-click Change Mail** with email case-variants + auto IMAP OTP capture (Gmail / Outlook / Yahoo)
- Auto **logout saved mail** when no email combo works
- Safe / Guard mode
- Coloured inline buttons (`primary` / `success` / `danger`)

## Requirements

```
python-telegram-bot==22.8
telethon==1.44.0
motor==3.6.1
pymongo==4.9.2
```

Python 3.10+

## Configuration

Set environment variables (recommended on Railway):

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | From @BotFather |
| `API_ID` | From my.telegram.org |
| `API_HASH` | From my.telegram.org |
| `MONGO_URI` | MongoDB connection string |
| `DB_NAME` | Database name (default `sessionbot`) |
| `OWNER_IDS` | Comma-separated Telegram user IDs |

Optional: `ALLOW_LOGIN_SECONDS`, `GUARD_INTERVAL`, `VERSION`

Or edit `config.py` for local runs (do not commit secrets).

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Railway

1. New project → Deploy from GitHub (`mailbot`)
2. Add Variables listed above
3. Start command: `python main.py`

## Mail feature

```
/addmail aarabharyan@outlook.com your_app_password
```

Then in **Change Mail** → **⚡ Use Saved Mail (auto + variants)**.

If every capitalisation combo fails, the bot automatically removes (logs out) the saved mail.
