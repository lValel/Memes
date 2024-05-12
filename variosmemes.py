import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeatmessage(ctx,*,mensaje):
    await ctx.send(mensaje)
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)    

@bot.command()
async def sendmessage(ctx,*,texto):
    canal_id='1229596709852549184'
    
    canal_destino=bot.get_channel(int(canal_id))
    if canal_destino is None:
        await ctx.send("el canal no existe")
        return
    await canal_destino.send(texto)
    await ctx.send('mensaje enviado al canal juegos')
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') 

@bot.command()
async def numberandom(ctx, menor:int, mayor:int):
    numrandom=random.randint(menor, mayor)
    await ctx.send("Tu número aleatorio es: ")       
    
@bot.command()
async def mem(ctx):
    num = random.randint(1,3)
    if num==1:
        with open('img/1era.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif num==2:
        with open('img/2nda.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    else:
        with open('img/3era.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
            
@bot.command()
async def comandos(ctx):
    await ctx.send(f"!hello")
    await ctx.send(f"!repeatmessage")
    await ctx.send(f"!add")
    await ctx.send(f"!sendmessage")
    await ctx.send(f"!numberandom")
    await ctx.send(f"!mem")
