#!/usr/bin/env python3
"""
Remove emoji characters from text files in specified directories.
"""
import os
import re
import argparse
from pathlib import Path

# Regex for emojis and various symbol blocks often used as emojis
# This is a broad range to catch most common emojis while trying to preserve useful symbols.
# Ranges covered:
# 1F600-1F64F: Emoticons
# 1F300-1F5FF: Misc Symbols and Pictographs
# 1F680-1F6FF: Transport and Map Symbols
# 2600-26FF: Misc Symbols
# 2700-27BF: Dingbats
# FE0F: Variation Selector-16 (often hidden but part of emoji sequences)
# 1F900-1F9FF: Supplemental Symbols and Pictographs
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U00002600-\U000026FF"
    "\U00002700-\U000027BF"
    "\U0000FE0F"
    "\U0001F900-\U0001F9FF"
    "\U0001F1E6-\U0001F1FF" # Flags
    "]+", flags=re.UNICODE
)

def remove_emojis_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = EMOJI_PATTERN.sub("", content)
        
        if content != new_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"cleaned: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"error processing {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Remove emojis from markdown files")
    parser.add_argument("directories", nargs="+", help="Directories to scan")
    args = parser.parse_args()
    
    count = 0
    for dirname in args.directories:
        path = Path(dirname)
        if not path.exists():
            print(f"Skipping non-existent directory: {dirname}")
            continue
            
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    if remove_emojis_from_file(file_path):
                        count += 1
                        
    print(f"\n✨ Cleaned emojis from {count} files.")

if __name__ == "__main__":
    main()
