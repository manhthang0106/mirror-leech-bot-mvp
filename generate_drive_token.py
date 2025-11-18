#!/usr/bin/env python3
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from pickle import dump

SCOPES = ["https://www.googleapis.com/auth/drive"]


def generate_token():
    creds = None
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0, open_browser=True)
    except Exception as e:
        print(f"Error: {e}")
        return

    with open("token.pickle", "wb") as token:
        dump(creds, token)
        print("Token generated successfully!")
        print("token.pickle file created.")


if __name__ == "__main__":
    generate_token()