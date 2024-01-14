import discord
import settings.config as config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Ready!")

client.run(config.DISCORD_TOKEN)
