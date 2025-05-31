# 必要モジュールのインポート
import os
from datetime import datetime, timedelta, timezone

import discord
from discord.ext import commands
from dotenv import load_dotenv

# from cogs.admin import AdminCog
from dbconnection import get_config

# 環境変数を読み込む
load_dotenv()

# Botクラス
class MKBotWorld(commands.Bot):

    # コンストラクタ
    def __init__(self):

        # インテントの設定
        intents = discord.Intents.default()
        intents.message_content = True

        # 設定を取得
        self.config = get_config()

        super().__init__("!", intents=intents)

    # 起動時の処理 on_ready()よりも早い
    async def setup_hook(self):
        pass
        # Cogを追加
        # await self.add_cog(AdminCog(bot, self.config))

    # 起動時の処理
    async def on_ready(self):
        
        # 現在時刻(JST)
        jst_now = datetime.now(timezone.utc)+timedelta(hours=9)

        # 埋め込みメッセージ
        embed = discord.Embed(color=discord.Color.green(), title="ログイン")
        embed.set_footer(text=jst_now.strftime("%Y/%m/%d %H:%M:%S.%f"))
        await self.get_channel(self.config.LOG_CHANNEL_ID).send(embed=embed)

# botインスタンス作成
bot = MKBotWorld()

# bot起動
bot.run(os.environ["BOT_TOKEN"])