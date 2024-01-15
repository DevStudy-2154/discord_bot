import discord
import random, string
import settings.config as config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Ready!")

# いきたいスタンプが押されたらお誘いチャンネルに自動でスレッドを立てる
@client.event
async def on_raw_reaction_add(payload):
  target_reaction = "ikitai"
  invitation_channel = client.get_channel(config.INVITATION_CHANNEL_ID)
  target_channel = client.get_channel(payload.channel_id)
  reaction = payload.emoji.name

  if reaction != target_reaction:
    return

  """
  初期生成スレッド情報
  スレッド名：ランダム文字列
  初期メッセージ：スタンプが押されたメッセージリンク
  """
  message_link = f'https://discord.com/channels/{config.SERVER_ID}/{target_channel.id}/{payload.message_id}'
  thread_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
  thread = await invitation_channel.create_thread(name=thread_name,type=discord.ChannelType.public_thread)
  thread_link = thread.mention

  await thread.send(message_link)
  await target_channel.send(thread_link)

client.run(config.DISCORD_TOKEN)
