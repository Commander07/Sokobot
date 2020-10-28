import discord
import random
import asyncio

class game:
  def __init__(self,channel,player):
    self.base_map = [
      [':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:'],
      [':white_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':white_large_square:'],
      [':white_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':white_large_square:'],
      [':white_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':white_large_square:'],
      [':white_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':white_large_square:'],
      [':white_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':black_large_square:', ':white_large_square:'],
      [':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:']
    ]
    self.channel = channel
    self.player = player

    self.player_pos = self.new_pos([])
    self.box_pos = self.new_pos([self.player_pos])
    self.end_pos = self.new_pos([self.player_pos,self.box_pos])
    self.message = None

  def new_pos(self,p):
    x = [random.randint(1,5), random.randint(1,5)]
    for pos in p:
      if pos == x:
        self.new_pos(p)
    return x

  async def stop(self):
    await self.message.delete()
    self.message = None
    del self

  async def move(self,action,client):
    if action == "up" and self.player_pos[0] > 1:
      self.map_[self.player_pos[0]][self.player_pos[1]] = ":white_large_square:"
      self.player_pos[0] -= 1
    elif action == "down" and self.player_pos[0] < 5:
      self.map_[self.player_pos[0]][self.player_pos[1]] = ":white_large_square:"
      self.player_pos[0] += 1
    elif action == "r" and self.player_pos[1] < 5:
      self.map_[self.player_pos[0]][self.player_pos[1]] = ":white_large_square:"
      self.player_pos[1] += 1
    elif action == "l" and self.player_pos[1] > 1:
      self.map_[self.player_pos[0]][self.player_pos[1]] = ":white_large_square:"
      self.player_pos[1] -= 1
    elif action == "reset":
      self.map_ = self.base_map
      self.player_pos = self.new_pos([])
      self.box_pos = self.new_pos([self.player_pos])
      self.end_pos = self.new_pos([self.player_pos,self.box_pos])
    
    await self.run(client)

  async def remove_reactions(self,reaction,client):
    async for user in reaction.users():
      if user != client.user:
        await reaction.remove(user)

  async def run(self,client):
    self.map_ = self.base_map

    self.map_[self.player_pos[0]][self.player_pos[1]] = ":grinning:"
    self.map_[self.end_pos[0]][self.end_pos[1]]       = ":question:"
    self.map_[self.box_pos[0]][self.box_pos[1]]       = ":brown_square:"

    _map = ""
    for y in self.map_:
      for x in y:
        _map += x
      _map += "\n"

    embed=discord.Embed(title="Level 1", description=_map)
    embed.set_footer(text="W = up A = left S = down D = right R = reset")

    if self.message:
      await self.message.edit(embed=embed)
    else:
      self.message = await self.channel.send(embed=embed)
      await self.message.add_reaction("⬆️")
      await self.message.add_reaction("⬇️")
      await self.message.add_reaction("⬅️")
      await self.message.add_reaction("➡️")
      await self.message.add_reaction("🔄")
    

    def check(reaction, user):
        return user == self.player and str(reaction.emoji) in ["⬆️","⬇️","⬅️","➡️","🔄"]

    if self.message:
      try:
        reaction, user = await client.wait_for('reaction_add', timeout=120.0, check=check)
      except asyncio.TimeoutError:
        embed=discord.Embed(title="ERROR", description="Game removed due to inactivity!", color=0xff0000)
        await self.channel.send(embed=embed)
      else:
        if reaction.emoji   == "⬆️":
          await self.remove_reactions(reaction,client)
          await self.move("up",client)
        elif reaction.emoji == "⬇️":
          await self.remove_reactions(reaction,client)
          await self.move("down",client)
        elif reaction.emoji == "⬅️":
          await self.remove_reactions(reaction,client)
          await self.move("l",client)
        elif reaction.emoji == "➡️":
          await self.remove_reactions(reaction,client)
          await self.move("r",client)
        elif reaction.emoji == "🔄":
          await self.remove_reactions(reaction,client)
          await self.move("reset",client)