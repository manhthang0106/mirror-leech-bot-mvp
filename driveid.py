#!/usr/bin/env python3
"""Script to generate list_drives.txt for multi-drive support."""

print("Multi-Drive List Generator")
print("="*50)
print("Format: DriveName folderID/tdID IndexLink(optional)")
print("Example: TD1 root https://example.dev")
print("Example: TD2 0AO1JDB1t3i5jUk9PVA https://example.dev")
print("="*50)
print("\nEnter drive details (press Ctrl+C to finish):")

drives = []
try:
    while True:
        name = input("\nDrive Name: ").strip()
        if not name:
            break
        folder_id = input("Folder/TD ID (or 'root'): ").strip()
        index_url = input("Index URL (optional, press Enter to skip): ").strip()
        
        line = f"{name} {folder_id}"
        if index_url:
            line += f" {index_url}"
        drives.append(line)
        print(f"Added: {line}")
except KeyboardInterrupt:
    print("\n\nFinished!")

if drives:
    with open("list_drives.txt", "w") as f:
        f.write("\n".join(drives))
    print(f"\nCreated list_drives.txt with {len(drives)} drives.")
else:
    print("\nNo drives added.")