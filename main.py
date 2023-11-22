import discord
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channel = message.channel
    data = json.load(open('data.json', 'r'))[0]
    dataKey = list(data.keys())
    if message.author == client.user:
        return
    if '-log' in message.content:
        if channel.name == "ubuntulog":
            if message.content.startswith('-log personal'):
                embed = discord.Embed(title="Personal Saving", color=0xFF5733)
                for key in dataKey:
                    if 'Personal' in key:
                        splitKey = key.split(' ')
                        embed.add_field(name=splitKey[1], value='Rs {0}'.format(data.get(key)), inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('Please connect to ubuntulog text channel.')
    else:
        await message.channel.send('Please connect to ubuntulog text channel.')


client.run(os.getenv('TOKEN'))
