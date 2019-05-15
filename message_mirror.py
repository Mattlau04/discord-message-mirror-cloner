import discord
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import sys
import requests
import aiohttp

client = discord.Client()
token = "put ur token here"

fromchannel = int(sys.argv[1])
webtoken = sys.argv[2]

@client.event
async def on_ready():
    print ("Logged in")
    

@client.event
async def on_message(message):
    fchannel = client.get_channel(fromchannel)
    if message.channel == fchannel:
        attach = message.attachments
        sentembed = message.embeds
        print ("Forwarding this message: "+ message.content)
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webtoken, adapter=AsyncWebhookAdapter(session))
            await webhook.send(content=message.content, username=message.author.display_name, avatar_url=message.author.avatar_url)

client.run(token, bot=False)