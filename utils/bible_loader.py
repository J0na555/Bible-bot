"""Bible data loading utilities."""
import os
import json
from pathlib import Path
from typing import Dict


def load_bible_data(data_dir: Path) -> Dict[str, list]:
    """
    Load all Bible books from JSON files in the specified directory.
    
    Args:
        data_dir: Path to directory containing JSON files
        
    Returns:
        Dictionary mapping book names to their chapters
    """
    all_books = {}
    
    # Get all JSON files sorted by filename
    json_files = sorted(data_dir.glob('*.json'))
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                book_data = json.load(f)
                # Extract book name from filename (e.g., '01_ኦሪት ዘፍጥረት.json' -> 'ኦሪት ዘፍጥረት')
                book_name = file_path.stem.split('_')[-1]
                all_books[book_name] = book_data.get('chapters', [])
        except (json.JSONDecodeError, KeyError, IOError) as e:
            print(f"Error loading {file_path}: {e}")
            continue
    
    return all_books
