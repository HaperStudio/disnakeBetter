import disnake
from disnake.ext import commands

# Import disnakeBetter
import disnakeBetter

# Set bot configs
intents = disnake.Intents.default()
bot = commands.Bot(command_prefix = '!', intents = intents)

# Set logger configs
logger_commands = disnakeBetter.LoggerCommands(r'logger\commands.txt', color = False)

# Testing command
@bot.command()
@logger_commands.command(slash = False) # Add logger decorator
async def ping(inter: disnake.AppCmdInter):
    await inter.send("Pong!")

@bot.event
async def on_ready():
    print(f'Bot ready: {bot.user} (ID: {bot.user.id})')
    print('------')

# Starting bot
if __name__ == '__main__':
    bot.run("") # Bot token
