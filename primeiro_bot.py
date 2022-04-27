import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Olá, estou pronto para iniciar! Estou conectado como {bot.user} #Bot Misaki Mei")

bot.run("OTY4OTMwNzMwMzAwMjc2Nzc3.YmmBDw.-0kGrl0MhqjvFvqLbhIKqErpUlY")