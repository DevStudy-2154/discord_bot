import discord
import settings.config as config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Ready!")

# 動作確認(おうむ返し)
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  await message.channel.send("Hello World!")

client.run(config.DISCORD_TOKEN)
