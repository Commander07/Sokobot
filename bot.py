import discord
import os
import yaml
import game

client = discord.Client()

games = {}

def load_settings():
  global default_prefix,prefix
  default_prefix = "$"
  prefix = yaml.load(open("data/prefix.yml","r"),Loader=yaml.SafeLoader)

def save_prefix(_prefix,guild):
  prefix[str(guild)] = _prefix
  yaml.dump(prefix,open("data/prefix.yml","w"))

@client.event
async def on_ready():
  load_settings()
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  _prefix = ""
  if str(message.guild.id) in prefix.keys():
    _prefix = prefix[str(message.guild.id)]
  else:
    _prefix = default_prefix

  if message.content.startswith(f"{_prefix}play"):
    if message.author in games.keys():
      embed=discord.Embed(title="ERROR", description="Only 1 game is allowed per user!", color=0xff0000)
      await message.channel.send(embed=embed)
      return
    new_game = game.game(message.channel,message.author)
    games[message.author] = new_game
    await new_game.run(client)
  elif message.content.lower() in ["w","a","s","d","r"] and message.author in games.keys():
    a = message.content.lower()
    player = message.author
    await message.delete()
    if   a == "w": await games[player].move("up",client)
    elif a == "a": await games[player].move("l",client)
    elif a == "s": await games[player].move("down",client)
    elif a == "d": await games[player].move("r",client)
    elif a == "r": await games[player].move("reset",client)
  elif message.content.startswith(f"{_prefix}set_prefix"):
    if message.author.guild_permissions.administrator:
      args = message.content.split(" ")
      if len(args) >= 2:
        save_prefix(args[1],message.guild.id)
        load_settings()
        embed=discord.Embed(title="Success", description=f"Successfully changed prefix to '{prefix[str(message.guild.id)]}'!", color=0x48ff45)
        await message.channel.send(embed=embed)
        return
      else:
        embed=discord.Embed(title="ERROR", description=f"Usage: {_prefix}set_prefix <prefix>.", color=0xff0000)
        await message.channel.send(embed=embed)
        return
    else:
      embed=discord.Embed(title="ERROR", description=f"You are not allowed to you that command!", color=0xff0000)
      await message.channel.send(embed=embed)
      return

client.run(os.getenv("TOKEN"))