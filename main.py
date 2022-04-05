import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

malardito = commands.Bot(command_prefix='>', description="Malardito")


@malardito.command()
async def ping(ctx):
    await ctx.send('Ando READY')


@malardito.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Hora",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.red())
    embed.add_field(name="Fecha de creacion del Server: ",
                    value=f"{ctx.guild.created_at}")
    embed.add_field(name="Patron del Server:", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del Server:", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del Server:", value=f"{ctx.guild.id}")
    embed.set_thumbnail(
        url=
        "https://i.pinimg.com/474x/73/18/98/7318980cd159190b338f2200d6bbacd3.jpg"
    )
    await ctx.send(embed=embed)


@malardito.command()
async def yutub(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' +
                                   query_string)
    search_results = re.findall('href = \"\\/watch\\?v=(.{11})',
                                html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


malardito.run('OTYwNjAxMDMxNjA2MTYxNDQ4.YkszbQ.KxtPLt0AGddZwmRmnSbX2sdCLhs')
