
# Discord Multi‑Bot Blaster 🚀

A powerful Discord bot that supports **multiple bot tokens** running simultaneously, with a spam/blast command and 24/7 uptime using a Flask web server. Perfect for Render or any cloud platform.

## ✨ Features

- Run **multiple Discord bots** from a single script
- `!blast <delay> <target>` – sends a sequence of spam messages to a user
- `!stop` – stops the current blast safely
- `!status` – shows bot latency and blasting status
- `!ping` – simple ping command
- Built‑in **Flask web server** to keep the bot alive (ideal for Render free tier)
- Fully asynchronous using `asyncio.gather` (bots run concurrently)

## 📋 Prerequisites

- Python 3.8 or higher
- Discord Bot Token(s) – [Get one from Discord Developer Portal](https://discord.com/developers/applications)
- (Optional) Render account for free hosting

## 🚀 Quick Start (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/discord-multi-bot.git
   cd discord-multi-bot
```

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables
   Create a .env file (or export directly):
   ```env
   DISCORD_TOKENS=your_first_token,second_token
   OWNER_IDS=your_discord_user_id
   ```
   Multiple tokens must be comma‑separated, no spaces.
3. Run the bot
   ```bash
   python bot.py
   ```

☁️ Deploy on Render (Free 24/7 Hosting)

1. Push this repository to GitHub.
2. Log in to Render → New → Web Service.
3. Connect your GitHub repo.
4. Use the following settings:
   · Build Command: pip install -r requirements.txt
   · Start Command: python bot.py
5. Add environment variables (Render Dashboard → Environment):
   · DISCORD_TOKENS = token1,token2
   · OWNER_IDS = your_user_id
6. Click Create Web Service.
7. To prevent sleeping on free tier, use cron-job.org to ping https://your-service.onrender.com every 10 minutes.

🤖 Bot Commands (Owner Only)

Command Description Example
!blast <delay> <target> Starts blasting @target every delay seconds !blast 2 @Spammer
!stop Immediately stops the blast !stop
!status Shows latency and whether a blast is active !status
!ping Replies with "Pong!" and latency !ping

Replace <target> with a user mention, name, or ID.

🛠️ Configuration

All settings are managed via environment variables:

Variable Description Required Example
DISCORD_TOKENS Comma‑separated list of bot tokens Yes token1,token2
OWNER_IDS Comma‑separated Discord user IDs allowed to use commands Yes 873940090248896522

🧪 Testing Your Tokens

Use the included test script to verify a token works locally:

```bash
python test_token.py
```

📁 File Structure

```
├── bot.py               # Main bot script (multi‑token + Flask)
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── test_token.py        # Optional: simple token validator
```

⚠️ Important Notes

· Message Content Intent must be enabled for every bot in the Discord Developer Portal → Bot → Privileged Gateway Intents.
· Always regenerate and reset your token if it has been exposed.
· Free Render services sleep after 15 minutes of inactivity; use a cron job (like cron-job.org) to ping your URL and keep it awake.
· The blast messages are long by design – adjust the messages list in bot.py if you want shorter content.

📜 License

This project is for educational purposes. Use responsibly and comply with Discord's Terms of Service.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

Made with ❤️ for Discord automation
Enjoy blasting (responsibly) and running multiple bots 24/7 for free!

```
