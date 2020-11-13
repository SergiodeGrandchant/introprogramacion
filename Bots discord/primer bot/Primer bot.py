import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="-")


@bot.command(name="s")#prefijo
async def sumar(ctx, num1, num2):
    response = int(num1) + int(num2)
    await ctx.send(response)

@bot.command(name="m")#prefijo
async def muliplicar(ctx, num1, num2):
    response = int(num1) * int(num2)
    await ctx.send(response)

@bot.command(name="leo")#prefijo
async def leo(ctx):
    response = str("Leo es re puto")
    await ctx.send(response)


@bot.command(name="yeyo")#prefijo
async def yeyo(ctx):
    r1 = str("El cumpleañero")
    await ctx.send(r1)


@bot.command(name="raul")#prefijo
async def yeyo(ctx):
    r1 = str("RAUL: puta de mierda y  toxica")
    await ctx.send(r1)


@bot.command(name="pulga")#prefijo
async def yeyo(ctx):
    r1 = str("EL come pansas y primas")
    await ctx.send(r1)


@bot.command(name="benja")#prefijo
async def yeyo(ctx):
    r1 = str("BENJA: maricon puto de mierda odiado por la puñete army")
    await ctx.send(r1)


bot.run(TOKEN)