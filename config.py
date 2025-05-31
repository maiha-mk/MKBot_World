from typing import Any


# DBから取得した設定情報を保持するためのクラス
class Config():

    # ログを送信するチャンネルのID
    LOG_CHANNEL_ID: int

    # コンストラクタ
    def __init__(self, rows: list[tuple[Any, ...]]):
        
        for row in rows:
            if row[0] == "LOG_CHANNEL_ID":
                self.LOG_CHANNEL_ID = int(row[1])