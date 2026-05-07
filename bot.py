import discord
from discord.ext import commands
import asyncio
import os
from flask import Flask
import threading
import traceback

# Flask web server
app = Flask('')
@app.route('/')
def home(): return "✅ Bot OK"
def run(): app.run(host='0.0.0.0', port=8080)
threading.Thread(target=run, daemon=True).start()
print("🌐 Web server started")

# Get token(s)
TOKENS = [t.strip() for t in os.getenv('DISCORD_TOKENS', '').split(',') if t.strip()]
OWNER_IDS = [int(i.strip()) for i in os.getenv('OWNER_IDS', '').split(',') if i.strip()]

print(f"📝 Found {len(TOKENS)} token(s)")
for i, t in enumerate(TOKENS):
    print(f"   Token {i+1} starts with: {t[:15]}... length {len(t)}")

if not TOKENS:
    print("❌ NO TOKENS. Set DISCORD_TOKENS env var.")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)
        self.is_blasting = False

    async def on_ready(self):
        print(f"✅ LOGGED IN AS {self.user.name} (ID: {self.user.id})")
        print(f"✅ In {len(self.guilds)} guilds")
        await self.change_presence(activity=discord.Game(name="!blast"))

    async def setup_hook(self):
        @self.command()
        async def blast(ctx, delay: int, *, target: str):
            if ctx.author.id not in OWNER_IDS:
                return
            if self.is_blasting:
                await ctx.send("Already blasting.")
                return
            self.is_blasting = True
            await ctx.send(f"🚀 Blasting {target} every {delay}s")
            messages = ["MSG1", "MSG2", "MSG3"]  # shortened for test
            while self.is_blasting:
                for m in messages:
                    if not self.is_blasting: break
                    await ctx.send(f"{target} {m}")
                    await asyncio.sleep(delay)
            await ctx.send("🛑 Stopped")

        @self.command()
        async def stop(ctx):
            if ctx.author.id not in OWNER_IDS: return
            self.is_blasting = False
            await ctx.send("Stopping...")

        @self.command()
        async def ping(ctx):
            if ctx.author.id not in OWNER_IDS: return
            await ctx.send(f"Pong! {round(self.latency*1000)}ms")

async def main():
    print("Starting bot(s)...")
    bots = [MyBot() for _ in TOKENS]
    tasks = []
    for bot, token in zip(bots, TOKENS):
        print(f"Attempting to start bot with token {token[:10]}...")
        tasks.append(bot.start(token))
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        print(f"❌ Login failed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
