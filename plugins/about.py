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
	await message.reply_text(f"𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫: {total_user()}\n\n𝐁𝐨𝐭 : @Renamer_Pro_bot\n\n𝐂𝐫𝐞𝐚𝐭𝐞𝐫 : @ChVivekTomar\n\n𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : Python3\n\n𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : Pyrogram 2.0\n\n𝐒𝐞𝐫𝐯𝐞𝐫 : Paid\n\n𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐧𝐚𝐦𝐞𝐝 𝐅𝐢𝐥𝐞 : {total_rename}\n\n𝐓𝐨𝐭𝐚𝐥 𝐒𝐢𝐳𝐞 𝐑𝐞𝐧𝐚𝐦𝐞𝐝 : {humanbytes(int(total_size))} ",quote=True)
