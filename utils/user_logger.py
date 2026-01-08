"""User logging utilities."""
from pathlib import Path
from typing import Optional


def log_user(user_id: int, user_name: Optional[str], users_file: Path) -> None:
    """
    Log user information to a file.
    
    Args:
        user_id: Telegram user ID
        user_name: User's first name
        users_file: Path to the users log file
    """
    try:
        with open(users_file, 'a', encoding='utf-8') as f:
            f.write(f"{user_id}, {user_name}\n")
    except IOError as e:
        print(f"Error logging user: {e}")
