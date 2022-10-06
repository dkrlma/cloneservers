import discord, os
from colorama import init
from src.utils import *
from config import *

init(autoreset=True, convert=True) # Se tiver erros no print, remova esta linha.

client = discord.Client()
if windows:
    os.system("title CloneServers Tool - Iniciando...")
print("CloneServers Tool - Iniciando...\n")

from src import ServerCloner
            
async def clone():
    guild = client.get_guild(int(input_guild_id))
    new_guild = client.get_guild(int(output_guild_id))

    cloner = ServerCloner(client, guild, new_guild, clear=clear_server)
    await cloner.start()
    log(blue+'[CloneServers]'+r, 'Processo de clonação finalizado.')
    if windows:
        os.system('title Clone Server Tool - Finalizado!')
        os.system('pause')

@client.event
async def on_ready():
    await clone()

client.run(token, bot=False)