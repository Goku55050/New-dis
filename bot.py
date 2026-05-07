import discord
from discord.ext import commands
import asyncio
import os

# --- CONFIGURATION ---
# Get tokens from environment variables
TOKENS = os.getenv('DISCORD_TOKENS', '').split(',')
# Remove any empty strings
TOKENS = [token.strip() for token in TOKENS if token.strip()]

PREFIX = '!'

# Get owner IDs from environment variables
MY_OWNER_IDS = [int(id.strip()) for id in os.getenv('OWNER_IDS', '').split(',') if id.strip()]

# Setup Intents
intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_blasting = False

    async def on_ready(self):
        print(f'✅ Logged in as {self.user.name}')
        print(f'🔒 Authorized Owner IDs: {MY_OWNER_IDS}')
        print(f'--- {self.user.name} is online and ready ---')

    async def setup_hook(self):
        # Add commands to this specific instance
        self.add_command(blast)
        self.add_command(stop)

@commands.command()
async def blast(ctx, delay: int, *, target: str):
    # SECURITY CHECK: Only authorized IDs can trigger this
    if ctx.author.id not in MY_OWNER_IDS:
        return

    if ctx.bot.is_blasting:
        await ctx.send(f"⚠️ [{ctx.bot.user.name}] A blast sequence is already running! Use `!stop` first.")
        return

    ctx.bot.is_blasting = True
    
    messages = [
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤣{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤣_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😍{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😍{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😍{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😍_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥵{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥵_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😡{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😡_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😝{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😝_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🥳{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🥳_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_😭{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄😭_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_💀{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄💀_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🤯{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🤯_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．",
        f"{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　　　　　．　　　　　　　　．　　　　　　　　．　　　　　　．　　　　．　　　　．　　　．　　　　　　．　　　　　_　　　　　　　_　　　　　_🔥{target} 　𝐂𝐇𝐀𝐋　𝐁𝐇𝐀𝐆　𝐌𝐓　𝐂𝐇𝐈𝐍𝐀𝐋　𝐊𝐄　𝐁𝐀𝐂𝐇𝐄🔥_　　　　　　　_　　　　　　　_　　　　　　　　　．　　　　　        .                 .       　𝐒𝐜𝐫𝐢𝐩𝐭 𝐁𝐲 𝐀𝐫𝐞𝐬 𝐃𝐚𝐝𝐝𝐲🔥．"
    ]

    await ctx.send(f"🚀 **[{ctx.bot.user.name}] Infinite Loop Started** for **{target}** with a {delay}s delay. Type `!stop` to end.")

    while ctx.bot.is_blasting:
        for msg in messages:
            if not ctx.bot.is_blasting:
                break
            
            try:
                await ctx.send(msg)
                if delay > 0:
                    await asyncio.sleep(delay)
            except Exception as e:
                print(f"Error sending message from {ctx.bot.user.name}: {e}")
                ctx.bot.is_blasting = False
                break
    
    await ctx.send(f"🛑 [{ctx.bot.user.name}] Blast sequence stopped.")

@commands.command()
async def stop(ctx):
    # SECURITY CHECK: Only authorized IDs can stop it
    if ctx.author.id not in MY_OWNER_IDS:
        return

    if not ctx.bot.is_blasting:
        await ctx.send(f"[{ctx.bot.user.name}] Nothing is running right now.")
    else:
        ctx.bot.is_blasting = False
        await ctx.send(f"🛑 [{ctx.bot.user.name}] Turning off the blast... please wait for the current cycle to end.")

async def main():
    if not TOKENS:
        print("ERROR: No Discord tokens found! Please set DISCORD_TOKENS environment variable.")
        return
    
    if not MY_OWNER_IDS:
        print("ERROR: No owner IDs found! Please set OWNER_IDS environment variable.")
        return
    
    print(f"Starting {len(TOKENS)} bot(s)...")
    # Create instances for all tokens
    bot_instances = [MyBot(command_prefix=PREFIX, intents=intents) for _ in TOKENS]
    
    # Run all bots simultaneously
    await asyncio.gather(*[bot.start(token) for bot, token in zip(bot_instances, TOKENS)])

# Start the multi-bot environment
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")
