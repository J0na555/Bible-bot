"""Configuration settings for the Bible Bot."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Telegram Bot API Token 
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not API_TOKEN:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN not found in environment variables. "
    )

# Paths
DATA_DIR = PROJECT_ROOT / 'data' / 'bible'
LOGS_DIR = PROJECT_ROOT / 'logs'
USERS_FILE = PROJECT_ROOT / 'data' / 'users.txt'

# Ensure directories exist
LOGS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)
(PROJECT_ROOT / 'data').mkdir(parents=True, exist_ok=True)

# Bot settings
CACHE_TIME = 1  # Cache time for inline queries in seconds
MAX_SUGGESTIONS = 5  # Maximum number of suggestions for fuzzy matching
