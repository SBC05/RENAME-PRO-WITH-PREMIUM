import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"ššØš­šš„ šš¬šš«: {total_user()}\n\nššØš­ : @Renamer_Pro_bot\n\nšš«ššš­šš« : @ChVivekTomar\n\nššš§š š®šš š : Python3\n\nšš¢šš«šš«š² : Pyrogram 2.0\n\nššš«šÆšš« : Paid\n\nššØš­šš„ ššš§šš¦šš šš¢š„š : {total_rename}\n\nššØš­šš„ šš¢š³š ššš§šš¦šš : {humanbytes(int(total_size))} ",quote=True)
