#!/usr/bin/env python3
"""Script to add service accounts to Team Drive."""
import argparse
import json
import os
from glob import glob


def add_to_team_drive(drive_id):
    """Add all service accounts to the specified Team Drive."""
    print(f"Adding service accounts to Team Drive: {drive_id}")
    print("Note: This is a simplified version. Refer to parent repo for full implementation.")
    
    accounts_folder = "accounts"
    if not os.path.exists(accounts_folder):
        print(f"Error: {accounts_folder} folder not found!")
        return
    
    sa_files = glob(f"{accounts_folder}/*.json")
    print(f"Found {len(sa_files)} service account files.")
    print("You need to manually add these emails to your Team Drive.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add Service Accounts to Team Drive")
    parser.add_argument("-d", "--drive-id", required=True, help="Team Drive ID")
    
    args = parser.parse_args()
    add_to_team_drive(args.drive_id)