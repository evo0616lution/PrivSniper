import discord, random, os
from time import sleep
from colorama import Fore as color
from colorama import init
from plyer import notification
from pyjavaproperties import Properties
from discord.ext import commands
from playsound import playsound
p = Properties()
init()
p.load(open('sniper.properties'))
TOKEN = p['token']
bot = commands.Bot(command_prefix="prv!!", help_command=None, self_bot=True)
snipe_message_author = {}
snipe_message_content = {}
###################################################
###################################################
def main():
    print(color.LIGHTGREEN_EX + """
__________        .__        _________      .__                     
\______   \_______|__|__  __/   _____/ ____ |__|_____   ___________ 
 |     ___/\_  __ \  \  \/ /\_____  \ /    \|  \____ \_/ __ \_  __ \
 |    |     |  | \/  |\   / /        \   |  \  |  |_> >  ___/|  | \/
 |____|     |__|  |__| \_/ /_______  /___|  /__|   __/ \___  >__|   
                                   \/     \/   |__|        \/       
    """)
    print(color.RESET + "By https://github.com/evo0616lution")
    sleep(0.2)

main()
@bot.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    if isinstance(message.channel, discord.channel.DMChannel):
        print(color.LIGHTRED_EX + f"[!] Message sniped! | {snipe_message_content[message.channel.id]} | Sent by {snipe_message_author[message.channel.id]}")
        playsound("ding.mp3")

bot.run(str(TOKEN), bot=False)
