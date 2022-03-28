import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)



# name = your status and url = your your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "x", url = "x"))



alive.alive()
client.run(os.getenv("OTI3OTIyNTk1MzAxNTcyNjM5.YkBojQ.VDXs6nb0MMRC3ugP7YndTtOLB-A"), bot=False)
