import os
import discord
from dotenv import load_dotenv

client = discord.client.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message: discord.Message):
    # Siia kirjutatud koodi jooksutatakse iga kord kui bot näeb, et sõnum saadetakse.
    # pass statementi ja käesoleva kommentaari võite ära kustutada, kui olete juba päris koodi siia kirjutanud.
    pass


if __name__ == '__main__':
    client.run(TOKEN)
