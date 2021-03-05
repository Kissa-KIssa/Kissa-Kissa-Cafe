import discord
import os
import requests 
from keep_alive import keep_alive
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online,activity=discord.Game('NEKOPARA Vol. 3'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('KKC hello'):
        await message.channel.send('Haii ! ')

keep_alive()
client.run(os.getenv('TOKEN'))