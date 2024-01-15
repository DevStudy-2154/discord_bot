import discord
import settings.config as config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Ready!")

# いきたいスタンプが押されたらお誘いチャンネルに自動でスレッドを立てる
target_reaction = "ikitai"
@client.event
async def on_raw_reaction_add(payload):
  channel = client.get_channel(payload.channel_id)
  reaction = payload.emoji.name

  if reaction != target_reaction:
    return

  message_link = f'https://discord.com/channels/{config.SERVER_ID}/{channel.id}/{payload.message_id}'

  await channel.send(message_link)

client.run(config.DISCORD_TOKEN)
