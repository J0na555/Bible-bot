#!/usr/bin/env python3
"""Script to migrate JSON files to the data/bible directory."""
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / 'data' / 'bible'

def migrate_json_files():
    """Move all JSON files from root to data/bible directory."""
    # Ensure data/bible directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Find all JSON files in root directory
    json_files = list(PROJECT_ROOT.glob('*.json'))
    
    if not json_files:
        print("No JSON files found in root directory.")
        return
    
    print(f"Found {len(json_files)} JSON files to migrate...")
    
    moved_count = 0
    for json_file in json_files:
        try:
            destination = DATA_DIR / json_file.name
            if destination.exists():
                print(f"  Skipping {json_file.name} (already exists in destination)")
                continue
            shutil.move(str(json_file), str(destination))
            print(f"  Moved: {json_file.name}")
            moved_count += 1
        except Exception as e:
            print(f"  Error moving {json_file.name}: {e}")
    
    print(f"\nMigration complete! Moved {moved_count} files to {DATA_DIR}")

if __name__ == '__main__':
    migrate_json_files()
