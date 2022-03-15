import discord
from discord.ext import commands
# from discord.ext.commands import bot
import asyncio
import datetime as dt

import qrcode

TOKEN = 'OTUxODc5MTIzMjkzMzM5Njg4.Yit4hA.C2i32DlNj8a7y5nrMOJpgRxb85I'

bot = commands.Bot(command_prefix='$')
client = discord.Client()

@bot.event
async def on_ready() -> None:
    print(f'Bot is connected to Discord!\n')

@bot.command(
	# ADDS THIS VALUE TO THE $HELP PING MESSAGE.
	help="",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief=""
)
async def qr(ctx, url):
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')

    await ctx.channel.send('Here is your QR Code!', file=discord.File(r'/Users/eskrg/Documents/Projects/QRCodeBot/qr_code.png'))

	# await ctx.channel.send("pong")

@bot.command(
	# ADDS THIS VALUE TO THE $HELP PING MESSAGE.
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send("pong")

# @bot.event
# async def on_message(message):
#     if message.content == 'Here is your QR Code!':
#         return

#     qr = qrcode.QRCode(
#         version=1,
#         box_size=10,
#         border=5)

#     URL = message.content

#     qr.add_data(URL)
#     qr.make(fit=True)
#     img = qr.make_image(fill='black', back_color='white')
#     img.save('qr_code.png')

#     await message.channel.send('Here is your QR Code!', file=discord.File(r'/Users/eskrg/Documents/Projects/QRCodeBot/qr_code.png'))

#     await bot.process_commands(message)


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     qr = qrcode.QRCode(
#         version=1,
#         box_size=10,
#         border=5)

#     URL = message.content

#     qr.add_data(URL)
#     qr.make(fit=True)
#     img = qr.make_image(fill='black', back_color='white')
#     img.save('qr_code.png')
#     await message.channel.send('Here is your QR Code!', file=discord.File(r'/Users/eskrg/Documents/Projects/QRCodeBot/qr_code.png'))

bot.run(TOKEN)

