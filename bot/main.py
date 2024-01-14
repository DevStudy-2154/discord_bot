import discord
import settings.config as config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Ready!")

# いきたいスタンプが押された時にお誘いチャンネルに自動でスレッドを立てる
target_reaction = "ikitai"
@client.event
async def on_raw_reaction_add(payload):
  channel = client.get_channel(payload.channel_id)
  message = await channel.fetch_message(payload.message_id)
  reaction = payload.emoji.name

  if reaction != target_reaction:
    return

  print(message.system_content)

client.run(config.DISCORD_TOKEN)
