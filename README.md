# Discord Multi‑Bot Spammer 🚀

A powerful Discord bot that supports **multiple bot tokens** running simultaneously, with a **parallel spam command** where all bots send **different messages at the same time** (fixed 1‑second delay). Includes advanced moderation commands and a built‑in Flask web server for 24/7 uptime on Render.

## ✨ Features

- Run **multiple Discord bots** from a single script
- `!spam <target>` – all bots spam the target **simultaneously** with **different messages** (1s delay between cycles)
- `!stop` – stops the spam immediately
- `!status`, `!ping` – monitor bot health
- Moderation: `!clear`, `!slowmode`, `!kick`, `!ban`, `!unban`, `!lock`, `!unlock`
- Utility: `!serverinfo`, `!userinfo`, `!say`, `!poll`, `!massdm`
- `!help` – paginated help with categories
- Built‑in **Flask web server** keeps the bot alive on Render (free tier)
- Fully asynchronous – **all bots send messages in parallel** using `asyncio.gather`

## 📋 Prerequisites

- Python 3.8 or higher
- Discord Bot Token(s) – [Get them from Discord Developer Portal](https://discord.com/developers/applications)
- **Privileged Gateway Intents must be enabled** for each bot:
  - `MESSAGE CONTENT INTENT` – **required** (to read commands)
  - `SERVER MEMBERS INTENT` – **optional** (needed for `!userinfo`, `!kick`, `!ban`, `!massdm`; if not enabled, those commands will have limited functionality)

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
   ```bash
   export DISCORD_TOKENS="token1,token2,token3"
   export OWNER_IDS="your_discord_user_id"
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
   · DISCORD_TOKENS = token1,token2,...
   · OWNER_IDS = your_user_id
6. Click Create Web Service.
7. To prevent sleeping on free tier, use cron-job.org to ping https://your-service.onrender.com every 10 minutes.

🤖 Bot Commands (Owner Only)

Command Description Example
!spam <target> All bots spam <target> simultaneously with different messages (1s delay) !spam @User
!stop Stops the spam immediately !stop
!status Shows latency, spam status, and number of bots !status
!ping Ping the bot !ping
!clear <amount> Delete messages (max 100) !clear 50
!slowmode <seconds> Set channel slowmode (0 to disable) !slowmode 5
!kick <user> [reason] Kick a member !kick @Spammer
!ban <user> [reason] Ban a member !ban @Troll
!unban <user#discrim or ID> Unban a user !unban Username#1234
!lock Lock the current text channel !lock
!unlock Unlock the channel !unlock
!serverinfo Display server information !serverinfo
!userinfo [user] Display user information !userinfo @Member
!say <message> Make the bot say a message !say Hello!
!poll <question> Create a yes/no poll !poll Is pizza good?
!massdm <message> DM all members (use with caution) !massdm Hello everyone!
!help [category] Show all commands or a specific category !help moderation

⚡ How the Parallel Spam Works

· All bots send messages at the same time (using asyncio.gather)
· Each bot gets a different set of messages from the pool – no two bots send the same message in the same cycle
· Delay between cycles is fixed at 1 second (can be changed in code)
· This design bypasses Discord's per‑channel rate limit (5 messages/5 seconds) by using multiple bots in parallel

🛠️ Configuration

All settings are managed via environment variables:

Variable Description Required Example
DISCORD_TOKENS Comma‑separated list of bot tokens Yes token1,token2
OWNER_IDS Comma‑separated Discord user IDs allowed to use commands Yes 873940090248896522

⚠️ Important Notes

· Message Content Intent must be enabled for every bot in the Discord Developer Portal → Bot → Privileged Gateway Intents.
· Server Members Intent is optional but required for userinfo/kick/ban/massdm to work fully.
· Free Render services sleep after 15 minutes of inactivity; use a cron job (cron-job.org) to ping your URL and keep it awake.
· The spam messages are long by design – you can edit the all_messages list in bot.py to customise them.

📁 File Structure

```
├── bot.py               # Main bot script (multi‑token + parallel spam + Flask)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

📜 License

This project is for educational purposes. Use responsibly and comply with Discord's Terms of Service.

---

Made with ❤️ for Discord automation
Now spam faster, smarter, and with style! 🔥

```
