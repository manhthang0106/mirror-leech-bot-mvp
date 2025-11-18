#!/usr/bin/env python3
from pyrogram import Client

print("Enter your Telegram API credentials:")
api_id = input("API ID: ")
api_hash = input("API Hash: ")

with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
    print("\n\nYour String Session:")
    print(app.export_session_string())
    print("\n\nAdd this to USER_SESSION_STRING in config.py")