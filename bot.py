import discord
from discord.ext import commands
import asyncio
import os
from flask import Flask
import threading

# ==================== FLASK WEB SERVER (Keep Alive) ====================
app = Flask('')

@app.route('/')
def home():
    return "✅ Discord Multi‑Bot is running 24/7!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()
    print("🌐 Web server started on port 8080")

# ==================== DISCORD BOT CONFIG ====================
# Environment variables
TOKENS = [t.strip() for t in os.getenv('DISCORD_TOKENS', '').split(',') if t.strip()]
OWNER_IDS = [int(i.strip()) for i in os.getenv('OWNER_IDS', '').split(',') if i.strip()]
PREFIX = '!'

# Intents
intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, intents=intents)
        self.is_blasting = False

    async def on_ready(self):
        print(f'✅ Logged in as {self.user.name} (ID: {self.user.id})')
        print(f'📡 Connected to {len(self.guilds)} guild(s)')
        await self.change_presence(activity=discord.Game(name=f"{PREFIX}blast | {PREFIX}stop"))

    async def setup_hook(self):
        self.add_command(blast)
        self.add_command(stop)
        self.add_command(status)
        self.add_command(ping)

# ==================== COMMANDS ====================
@commands.command()
async def blast(ctx, delay: int, *, target: str):
    """Blast a target with custom messages every X seconds."""
    if ctx.author.id not in OWNER_IDS:
        await ctx.send("❌ You are not authorized to use this command.")
        return

    if ctx.bot.is_blasting:
        await ctx.send(f"⚠️ A blast is already running. Use `{PREFIX}stop` first.")
        return

    ctx.bot.is_blasting = True
    await ctx.send(f"🚀 **Blast started** for `{target}` every {delay} seconds. Use `{PREFIX}stop` to end.")

    messages = [
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😍{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😍{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😍{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"# {target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　        .                 .       　𝐒𝐜𝐫𝐢𝐩𝐭 𝐁𝐲 𝐀𝐫𝐞𝐬 𝐃𝐚𝐝𝐝𝐲🔥．"
    ]

    while ctx.bot.is_blasting:
        for msg in messages:
            if not ctx.bot.is_blasting:
                break
            try:
                await ctx.send(msg)
                await asyncio.sleep(delay)
            except Exception as e:
                print(f"Error sending message: {e}")
                ctx.bot.is_blasting = False
                break

    await ctx.send(f"🛑 **Blast stopped** for `{target}`.")

@commands.command()
async def stop(ctx):
    """Stop the current blast."""
    if ctx.author.id not in OWNER_IDS:
        return
    if not ctx.bot.is_blasting:
        await ctx.send("No blast is currently running.")
    else:
        ctx.bot.is_blasting = False
        await ctx.send("🛑 Stopping blast... (current cycle will finish)")

@commands.command()
async def status(ctx):
    """Check bot status and latency."""
    if ctx.author.id not in OWNER_IDS:
        return
    embed = discord.Embed(title="🤖 Bot Status", color=discord.Color.green())
    embed.add_field(name="Status", value="✅ Online", inline=True)
    embed.add_field(name="Latency", value=f"{round(ctx.bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Blasting", value="Yes" if ctx.bot.is_blasting else "No", inline=True)
    embed.add_field(name="Servers", value=str(len(ctx.bot.guilds)), inline=True)
    await ctx.send(embed=embed)

@commands.command()
async def ping(ctx):
    """Simple ping command."""
    if ctx.author.id not in OWNER_IDS:
        return
    await ctx.send(f"Pong! 🏓 ({round(ctx.bot.latency * 1000)}ms)")

# ==================== MULTI‑BOT LAUNCHER ====================
async def main():
    keep_alive()

    if not TOKENS:
        print("❌ ERROR: No Discord tokens found. Set DISCORD_TOKENS environment variable.")
        return
    if not OWNER_IDS:
        print("⚠️ WARNING: No owner IDs set. Commands will be locked.")

    print(f"🚀 Starting {len(TOKENS)} bot(s)...")
    bots = [MyBot() for _ in TOKENS]
    await asyncio.gather(*[bot.start(token) for bot, token in zip(bots, TOKENS)])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Shutting down.")
