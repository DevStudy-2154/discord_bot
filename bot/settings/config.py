import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID=os.getenv('SERVER_ID')
INVITATION_CHANNEL_ID=int(os.getenv('INVITATION_CHANNEL_ID'))
