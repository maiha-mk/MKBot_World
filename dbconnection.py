import os

import psycopg2
from psycopg2.extensions import connection

from config import Config


# DBへの接続を取得します
def get_connection() -> connection:
    return psycopg2.connect(os.environ["DATABASE_PUBLIC_URL"])

# configテーブルのデータを全件取得し、Configオブジェクトとして返します。
def get_config() -> Config:

    # クエリ
    query = "SELECT" \
            "    *" \
            "FROM" \
            "    config"
    
    # 接続してクエリ実行
    with get_connection() as conn:
        with conn.cursor() as cur:
            
            # クエリを実行
            cur.execute(query)
            # 全件取得
            rows = cur.fetchall()

    return Config(rows)