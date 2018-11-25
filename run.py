import discord
from discord.ext import commadns
from discord.ext.commands import Bot
import asyncio

cilent = discord.Client()
client = commands.Bot(command_prefix="*")

@client.event
async def on_ready():
  print("I am Logged in")
  
@client.event
async def on_message(message):
  if messgae.content.startswith(*hello):
    msg="Hello {o.author.mention}. How is ur Day".format(message)
    await client.send_message(message.channel,msg)
   
  

client.run('NTEzMzE2MTgzNTA0ODQ2ODU4.DtwsHg.AhmCqvSJqXP47x4UzL-SGXhB6rI
')
