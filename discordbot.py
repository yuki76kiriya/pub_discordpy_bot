# インストールした discord.pyを読み込む
import discord
from discord.ext import commands
import os
import traceback
# 接続に必要なオブジェクトを作成
# ------------------------------------------
# intents=discord.Intents.all()
# client = discord.Client(intents=intents)
# ------------------------------------------
client = discord.Client()

# サーバーID
# SERVER_ID = 999999999999999999
# トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']
ENTRANCE_CHANNEL_ID = os.environ['DISCORD_BOT_CHANNEL_ID']

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    text_chat = client.get_channel(CHANNEL_ID)
    await text_chat.send("みんな、お疲れ様、ﾁｮｯﾄは休めよ。")


# 新規メンバー参加時に実行するイベントハンドラ
# @client.event
# async def on_member_join(member):
#     login_chat = client.get_channel(ENTRANCE_CHANNEL)
#     await login_chat.send(str(member.mention) + "さん、ようこそ！アタシは桐生つかさ。ギャルで社長。んでアイドル。とりあえず自己紹介してきなよ。アタシの演出、お前に任せたぜ。")


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # メンション
    if message.content.startswith("つかさ、お疲れ様。"):
        await message.channel.send(str(message.author.mention) + "お疲れ。アタシの仕事はもう終わらせたけど、お前は？")
    # wiki
    if message.content.startswith("!wiki"):
        await message.channel.send(WIKI)
    # 起動確認
    if message.content.startswith("/ping"):
        await message.channel.send("/pong")
    # 強制終了
    if message.content.startswith("!SHUTDOWN_BOT"):#!SHUTDOWN_BOTが入力されたら強制終了
        await client.logout()
        await sys.exit()

# ボイスチャット入室退室時
# @client.event
# async def on_voice_state_update(member,before,after):
#     if (before.channel == client.get_channel(VOICE_ID)) or (after.channel == client.get_channel(VOICE_ID)):
#         voice_chat = client.get_channel(VOICETEXT_ID)
#         if before.channel is None:
#             msg = str(member.name) + "が入室しました。"
#             await voice_chat.send(msg)
#         elif after.channel is None:
#             msg = str(member.name) + "が退室しました。"
#             await voice_chat.send(msg)
#     elif (before.channel == client.get_channel(VOICE_MEETING_ID)) or (after.channel == client.get_channel(VOICE_MEETING_ID)):
#         voice_meeting_chat = client.get_channel(VOICETEXT_MEETING_ID)
#         if before.channel is None:
#             msg = str(member.name) + "が入室しました。"
#             await voice_meeting_chat.send(msg)
#         elif after.channel is None:
#             msg = str(member.name) + "が退室しました。"
#             await voice_meeting_chat.send(msg)
#     elif (before.channel == client.get_channel(LIPA_VOICE_ID)) or (after.channel == client.get_channel(LIPA_VOICE_ID)):
#         voice_lipa_chat = client.get_channel(LIPA_ID)
#         if before.channel is None:
#             msg = str(member.name) + "が入室しました。"
#             await voice_lipa_chat.send(msg)
#         elif after.channel is None:
#             msg = str(member.name) + "が退室しました。"
#             await voice_lipa_chat.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
