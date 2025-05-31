from typing import Any


# 設定情報を表すクラス
class Config():

    # ログを送信するチャンネルのID
    LOG_CHANNEL_ID: int

    # コンストラクタ
    # rows: DBから取得したデータ
    def __init__(self, rows: list[tuple[Any, ...]]):
        
        for row in rows:
            if row[0] == "LOG_CHANNEL_ID":
                self.LOG_CHANNEL_ID = int(row[1])
