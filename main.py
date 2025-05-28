# 必要モジュールのインポート
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True

# botインスタンス作成
bot = commands.Bot(command_prefix='!', intents=intents)

# bot起動
bot.run(os.environ["BOT_TOKEN"])