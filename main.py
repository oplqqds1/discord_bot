import os
import discord
from discord.ext import commands
import DiscordUtils
import datetime
from os import system 
from time import sleep
from colorama import Fore

from myserver import server_on


prefixs = '!'
guils_id = 1272071858564632686
logs_welcome_id = 1272080610311147633
logs_leave_id = 1272080651863982081
welcome_channel_id = 1272035720776908853
leave_channel_id = 1272056197129703434


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = prefixs, intents = intents)
client.remove_command('help')

invtrck = DiscordUtils.InviteTracker(client)

@client.event
async def on_ready():
    system('cls')
    print(' -----')
    print('\n > Login....')
    sleep(1)
    system('cls')
    print(' -----')
    print(f'{Fore.GREEN}\n > Login Token client Done!{Fore.RESET}')
    sleep(0.5)
    system('cls')
    print(' -----')
    print(f'\n > Login Token client : {client.user}')
    print('\n -----')
    await client.change_presence(activity=discord.Game(name="TEST LOG"))

@client.event
async def on_member_join(member):

    inver = await invtrck.fetch_inviter(member) 
    channel = client.get_channel(logs_welcome_id)
    guild = client.get_guild(guils_id)
    total = 0

    for i in await guild.invites():
        if i.inviter == inver :
            total += i.uses

        embedjoin = discord.Embed(
            title = "WELCOME TO MEOAW HUB",
            description = f"คุณ {member.mention} เข้าร่วมเซิฟเวอร์ ยืนยันตัวตนได้ที่<#996394902508281896>\n\nได้รับคำเชิญจาก : {inver.mention}",
            colour = 0x00FF99
        ) 
        embedjoin.timestamp = datetime.datetime.utcnow()
        embedjoin.set_footer(text=" | MEOAW HUB WELCOME")
        embedjoin.set_thumbnail(url = f"{member.avatar.url}")
        
    await channel.send(embed=embedjoin)

@client.event
async def on_member_remove(member):
    
    inver = await invtrck.fetch_inviter(member) 
    channel = client.get_channel(logs_leave_id)
            
    embedremove = discord.Embed(
        title = "สมาชิกได้ออกจากServer",
        description = f"คุณ {member.mention} ออกดิสไปแล้ว",
        colour = 0x00FF99
    ) 
    embedremove.timestamp = datetime.datetime.utcnow()
    embedremove.set_footer(text=" | 𝐒𝐍𝐎𝐖 𝐒𝐇𝐎𝐏 𝐅𝐎𝐑 𝐆𝐨𝐨𝐝𝐛𝐲𝐞 ")
    await channel.send(embed=embedremove)
    
server_on()

client.run(os.getenv('TOKEN'))