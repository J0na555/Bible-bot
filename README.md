# Amharic Bible Bot

A Telegram bot that allows users to search and read the Amharic Bible using inline queries. The bot supports fuzzy matching for book names, making it easy to find Bible verses even with partial or misspelled input.

## Features

- 🔍 **Inline Search**: Search Bible verses directly in any chat
- 📖 **Fuzzy Matching**: Find books even with partial or misspelled names
- 📚 **Full Bible Support**: All 66 books of the Bible in Amharic
- 💬 **Works Everywhere**: Use in private chats, groups, and channels
- 🎯 **Easy Navigation**: Search by book, chapter, and verse

## Project Structure

```
Bible-bot/
├── config/                 # Configuration files
│   ├── __init__.py
│   └── config.py          # Bot configuration and settings
├── data/                   # Data files
│   ├── bible/             # JSON files for Bible books
│   └── users.txt          # User log file
├── handlers/               # Bot handlers
│   ├── __init__.py
│   ├── command_handler.py # Command handlers (/start, etc.)
│   └── inline_handler.py  # Inline query handler
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── bible_loader.py    # Bible data loading
│   ├── text_utils.py      # Text processing utilities
│   └── user_logger.py     # User logging utilities
├── logs/                   # Log files (gitignored)
├── main.py                # Main entry point
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Installation

1. **Clone the repository** (or navigate to the project directory)

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory
   - Add your Telegram bot token:
     ```
     TELEGRAM_BOT_TOKEN=your_bot_token_here
     ```
   - Or modify `config/config.py` directly (not recommended for production)

5. **Move Bible JSON files**:
   - Move all JSON files from the root directory to `data/bible/`
   ```bash
   mv *.json data/bible/
   ```

## Usage

1. **Start the bot**:
   ```bash
   python main.py
   ```

2. **Use the bot**:
   - In any Telegram chat, type `@your_bot_name` followed by:
     - Book name only: `ዘፍጥረት`
     - Book and chapter: `ዘፍጥረት 1`
     - Book, chapter, and verse: `ዘፍጥረት 1:1`

## Configuration

Edit `config/config.py` to customize:
- `CACHE_TIME`: Cache time for inline queries (default: 1 second)
- `MAX_SUGGESTIONS`: Maximum number of fuzzy match suggestions (default: 5)
- `DATA_DIR`: Path to Bible JSON files
- `USERS_FILE`: Path to user log file

## Development

### Code Structure

- **`main.py`**: Initializes the bot, loads data, and registers handlers
- **`handlers/`**: Contains all bot handlers (commands and inline queries)
- **`utils/`**: Utility functions for text processing, data loading, and logging
- **`config/`**: Centralized configuration management

### Adding New Features

1. **New Commands**: Add handlers in `handlers/command_handler.py`
2. **New Utilities**: Add functions in `utils/`
3. **Configuration**: Update `config/config.py`

## License

This project is open source and available for personal and educational use.

## Support

For issues or feedback, contact @kkyk1286 on Telegram.
