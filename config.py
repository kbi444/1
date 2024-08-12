from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "24574525")
APP_HASH = os.environ.get("APP_HASH", "d9c4c2459f68da63c58517e431d49149")
SESSION = os.environ.get("TERMUX", "1ApWapzMBuwVYD3s-hSv6m7CdoiuG4PuLqESgDls19g_l5OJ7mIFWwTD-igUrrFbGGc_kIfjNdSNnm1DDipfsIIJVtwjK8WWKVfYo0tRISzURCBsTymeUBT1rbBWe-zA4Y4zgwI2nKkHZkKwrPRVV5UHfLCDG9Bf08lPQQerM74gEW1uDqlfALvOBsWxWJX_I8V32wi79XQSU_RQ8y4u-UUMkEw2kM2PDWXRSUBBVU871L-0BGpBhLZ7xEq9ozCvfXnMMzCPRC8u-uxAmcLfOUSlzh2J4U1X7esFHna-Z4eGXITLS0atjDDQxgwxF3DkIfIPKd6KM0RRrM_ouWTP1sv8gdpfcMQE=")
olgaly = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
olgaly.start()
