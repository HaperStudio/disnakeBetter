import disnake
from disnake.ext import commands
from disnake.gateway import DiscordWebSocket

# Import disnakeBetter
from disnakeBetter.ext import BotWebSocket

# Set bot configs
intents = disnake.Intents.default()
bot = commands.Bot(command_prefix = '!', intents = intents)

# Testing command
@bot.command()
async def ping(inter: disnake.AppCmdInter):
    await inter.send("Pong!")

@bot.event
async def on_ready():
    print(f'Bot ready: {bot.user} (ID: {bot.user.id})')
    print('------')

# Starting bot
if __name__ == '__main__':
    DiscordWebSocket.identify = BotWebSocket.status_mobile # Set custom bot web socket preset. For example mobile status
  
    bot.run("") # Bot token
