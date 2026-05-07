import discord
from discord.ext import commands
import asyncio
import os
import datetime
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

# ==================== GLOBAL SPAM CONTROLLER ====================
spam_state = {
    "active": False,
    "target": "",
    "task": None
}

async def spam_worker(bots):
    """Background task that makes ALL bots spam simultaneously with DIFFERENT messages."""
    target = spam_state["target"]
    
    # Original messages split across bots - each bot gets a unique set
    all_messages = [
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
    
    # Distribute messages to bots (each bot gets different messages)
    # Bot 1 gets messages at even indexes (0,2,4...)
    # Bot 2 gets messages at odd indexes (1,3,5...)
    # If more bots, cycle through them
    bot_messages = {}
    for i, bot in enumerate(bots):
        bot_messages[bot] = [msg for idx, msg in enumerate(all_messages) if idx % len(bots) == i]
    
    while spam_state["active"]:
        # Each bot sends its own unique message
        # Use asyncio.gather to send ALL bot messages in PARALLEL
        tasks = []
        for bot in bots:
            if hasattr(bot, 'spam_channel') and bot.spam_channel:
                channel = bot.get_channel(bot.spam_channel)
                if channel and bot_messages.get(bot):
                    # Each bot sends its next message (cycling through its unique list)
                    msg_index = spam_state.get(f"msg_index_{bot.user.id}", 0) % len(bot_messages[bot])
                    msg = bot_messages[bot][msg_index]
                    tasks.append(channel.send(msg))
                    spam_state[f"msg_index_{bot.user.id}"] = msg_index + 1
        
        # Send all messages simultaneously (TRUE PARALLEL)
        if tasks:
            await asyncio.gather(*tasks)
        
        # Wait 1 second before next batch
        await asyncio.sleep(1)
    
    # Cleanup
    for bot in bots:
        if hasattr(bot, 'spam_channel'):
            del bot.spam_channel
        # Clean up message indexes
        if f"msg_index_{bot.user.id}" in spam_state:
            del spam_state[f"msg_index_{bot.user.id}"]

# ==================== DISCORD BOT CONFIG ====================
TOKENS = [t.strip() for t in os.getenv('DISCORD_TOKENS', '').split(',') if t.strip()]
OWNER_IDS = [int(i.strip()) for i in os.getenv('OWNER_IDS', '').split(',') if i.strip()]
PREFIX = '!'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True   # for userinfo, kick, ban etc.

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, intents=intents)
        self.spam_channel = None
        self.all_bots = []   # will be filled after creation
        # Remove the default help command to avoid conflict
        self.remove_command('help')

    async def on_ready(self):
        print(f'✅ Logged in as {self.user.name} (ID: {self.user.id})')
        print(f'📡 Connected to {len(self.guilds)} guild(s)')
        await self.change_presence(activity=discord.Game(name=f"{PREFIX}help | {PREFIX}spam"))

    async def setup_hook(self):
        # Add all commands (some are inside the class, some will be added as methods)
        self.add_command(spam)
        self.add_command(stop_spam)
        self.add_command(status)
        self.add_command(ping)
        self.add_command(help_cmd)
        self.add_command(clear)
        self.add_command(slowmode)
        self.add_command(serverinfo)
        self.add_command(userinfo)
        self.add_command(say)
        self.add_command(kick)
        self.add_command(ban)
        self.add_command(unban)
        self.add_command(lock)
        self.add_command(unlock)
        self.add_command(poll)
        self.add_command(massdm)

# ==================== SPAM COMMAND (all bots together) ====================
@commands.command(name='spam')
async def spam(ctx, *, target: str):
    """Spam a target user/name (fixed 1s delay). ALL bots will spam together."""
    if ctx.author.id not in OWNER_IDS:
        await ctx.send("❌ Unauthorized.")
        return

    global spam_state
    if spam_state["active"]:
        await ctx.send("⚠️ Spam already active. Use `!stop` to stop.")
        return

    # Set the channel for all bots to send messages
    for bot in ctx.bot.all_bots:
        bot.spam_channel = ctx.channel.id

    spam_state["active"] = True
    spam_state["target"] = target

    # Start the global spam worker if not already running
    if spam_state["task"] is None or spam_state["task"].done():
        spam_state["task"] = asyncio.create_task(spam_worker(ctx.bot.all_bots))

    await ctx.send(f"🚀 **ALL bots are now spamming** `{target}` every 1 second. Use `!stop` to end.")

@commands.command(name='stop')
async def stop_spam(ctx):
    """Stop the current spam."""
    if ctx.author.id not in OWNER_IDS:
        return
    global spam_state
    if not spam_state["active"]:
        await ctx.send("No spam is currently running.")
        return
    spam_state["active"] = False
    if spam_state["task"]:
        spam_state["task"].cancel()
    await ctx.send("🛑 **All bots stopped spamming.**")

# ==================== BASIC COMMANDS (preserved) ====================
@commands.command()
async def status(ctx):
    """Check bot status and latency."""
    if ctx.author.id not in OWNER_IDS:
        return
    embed = discord.Embed(title="🤖 Bot Status", color=discord.Color.green())
    embed.add_field(name="Status", value="✅ Online", inline=True)
    embed.add_field(name="Latency", value=f"{round(ctx.bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Spam Active", value="Yes" if spam_state["active"] else "No", inline=True)
    embed.add_field(name="Servers", value=str(len(ctx.bot.guilds)), inline=True)
    await ctx.send(embed=embed)

@commands.command()
async def ping(ctx):
    """Simple ping command."""
    if ctx.author.id not in OWNER_IDS:
        return
    await ctx.send(f"Pong! 🏓 ({round(ctx.bot.latency * 1000)}ms)")

# ==================== ADVANCED MODERATION & UTILITY COMMANDS ====================
@commands.command()
async def clear(ctx, amount: int):
    """Delete a specified amount of messages (max 100)."""
    if ctx.author.id not in OWNER_IDS:
        return
    if amount < 1:
        await ctx.send("Amount must be at least 1.")
        return
    if amount > 100:
        amount = 100
    deleted = await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"✅ Deleted {len(deleted)-1} messages.")
    await asyncio.sleep(3)
    await msg.delete()

@commands.command()
async def slowmode(ctx, seconds: int):
    """Set slowmode delay in this channel (0 to disable)."""
    if ctx.author.id not in OWNER_IDS:
        return
    await ctx.channel.edit(slowmode_delay=seconds)
    if seconds == 0:
        await ctx.send("✅ Slowmode disabled.")
    else:
        await ctx.send(f"✅ Slowmode set to {seconds} seconds.")

@commands.command()
async def serverinfo(ctx):
    """Display information about the server."""
    if ctx.author.id not in OWNER_IDS:
        return
    guild = ctx.guild
    embed = discord.Embed(title=guild.name, color=discord.Color.blue())
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Boost Level", value=guild.premium_tier, inline=True)
    embed.add_field(name="Created", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
    await ctx.send(embed=embed)

@commands.command()
async def userinfo(ctx, member: discord.Member = None):
    """Display information about a user."""
    if ctx.author.id not in OWNER_IDS:
        return
    member = member or ctx.author
    embed = discord.Embed(title=str(member), color=member.color)
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Joined Discord", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Roles", value=", ".join([r.mention for r in member.roles[1:]]) or "None", inline=False)
    await ctx.send(embed=embed)

@commands.command()
async def say(ctx, *, message):
    """Make the bot say a message (then delete command message)."""
    if ctx.author.id not in OWNER_IDS:
        return
    await ctx.message.delete()
    await ctx.send(message)

@commands.command()
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    """Kick a member from the server."""
    if ctx.author.id not in OWNER_IDS:
        return
    if member.guild_permissions.administrator:
        await ctx.send("❌ Cannot kick an administrator.")
        return
    await member.kick(reason=reason)
    await ctx.send(f"✅ Kicked {member.mention} | Reason: {reason}")

@commands.command()
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    """Ban a member from the server."""
    if ctx.author.id not in OWNER_IDS:
        return
    if member.guild_permissions.administrator:
        await ctx.send("❌ Cannot ban an administrator.")
        return
    await member.ban(reason=reason)
    await ctx.send(f"✅ Banned {member.mention} | Reason: {reason}")

@commands.command()
async def unban(ctx, *, member):
    """Unban a user by name#discrim or ID."""
    if ctx.author.id not in OWNER_IDS:
        return
    banned_users = [entry async for entry in ctx.guild.bans()]
    name, discrim = member.split('#') if '#' in member else (member, None)
    for ban_entry in banned_users:
        user = ban_entry.user
        if (discrim and str(user) == member) or (not discrim and str(user.id) == member):
            await ctx.guild.unban(user)
            await ctx.send(f"✅ Unbanned {user.mention}")
            return
    await ctx.send("❌ User not found in ban list.")

@commands.command()
async def lock(ctx):
    """Lock the current text channel (disable send messages for @everyone)."""
    if ctx.author.id not in OWNER_IDS:
        return
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔒 Channel locked.")

@commands.command()
async def unlock(ctx):
    """Unlock the current text channel."""
    if ctx.author.id not in OWNER_IDS:
        return
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = None
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔓 Channel unlocked.")

@commands.command()
async def poll(ctx, *, question):
    """Create a simple yes/no poll."""
    if ctx.author.id not in OWNER_IDS:
        return
    embed = discord.Embed(title="📊 Poll", description=question, color=discord.Color.purple())
    embed.set_footer(text=f"Requested by {ctx.author.display_name}")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

@commands.command()
async def massdm(ctx, *, message):
    """DM all members of the server (use with caution, rate limits)."""
    if ctx.author.id not in OWNER_IDS:
        return
    await ctx.send("⚠️ This command will DM every member. This may take a while and hit rate limits. Continue? (yes/no)")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["yes", "no"]
    try:
        resp = await ctx.bot.wait_for('message', timeout=30.0, check=check)
        if resp.content.lower() != "yes":
            await ctx.send("Cancelled.")
            return
    except asyncio.TimeoutError:
        await ctx.send("Timed out.")
        return

    count = 0
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(message)
            count += 1
            await asyncio.sleep(1)  # avoid rate limit
        except:
            pass
    await ctx.send(f"✅ Sent DM to {count} members.")

# ==================== HELP COMMAND ====================
@commands.command(name='help')
async def help_cmd(ctx, *, category: str = None):
    """Shows all commands or details for a specific command."""
    if ctx.author.id not in OWNER_IDS:
        return

    commands_list = {
        "Spam": ["`!spam <target>` - Spam a target (1s delay, all bots together)", "`!stop` - Stop the spam"],
        "Basic": ["`!status` - Bot status & latency", "`!ping` - Ping the bot"],
        "Moderation": [
            "`!clear <amount>` - Delete messages (max 100)",
            "`!slowmode <seconds>` - Set channel slowmode",
            "`!kick <user> [reason]` - Kick a member",
            "`!ban <user> [reason]` - Ban a member",
            "`!unban <user#discrim or ID>` - Unban a user",
            "`!lock` - Lock the channel",
            "`!unlock` - Unlock the channel"
        ],
        "Utility": [
            "`!serverinfo` - Show server info",
            "`!userinfo [user]` - Show user info",
            "`!say <message>` - Make bot say something",
            "`!poll <question>` - Create a yes/no poll",
            "`!massdm <message>` - DM all members (use carefully)"
        ]
    }

    if category is None:
        # Show all categories
        embed = discord.Embed(title="📚 Bot Commands", color=discord.Color.gold())
        for cat, cmds in commands_list.items():
            embed.add_field(name=f"**{cat}**", value="\n".join(cmds), inline=False)
        embed.set_footer(text=f"Type `{PREFIX}help <category>` for more details")
        await ctx.send(embed=embed)
    else:
        # Show specific category
        category_lower = category.lower().capitalize()
        if category_lower in commands_list:
            embed = discord.Embed(title=f"**{category_lower} Commands**", color=discord.Color.gold())
            embed.description = "\n".join(commands_list[category_lower])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"❌ Unknown category. Available: {', '.join(commands_list.keys())}")

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
    # Share the list of all bots with each instance
    for bot in bots:
        bot.all_bots = bots
    await asyncio.gather(*[bot.start(token) for bot, token in zip(bots, TOKENS)])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Shutting down.")
