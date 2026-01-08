# Project File Structure

This document provides a detailed overview of the project's file structure and organization.

## Directory Tree

```
Bible-bot/
│
├── config/                          # Configuration module
│   ├── __init__.py                 # Package initialization
│   └── config.py                   # Bot settings and paths
│
├── data/                            # Data directory
│   ├── bible/                      # Bible JSON files (66 books)
│   │   ├── 01_ኦሪት ዘፍጥረት.json
│   │   ├── 02_ኦሪት ዘጸአት.json
│   │   └── ... (all 66 books)
│   └── users.txt                   # User log file
│
├── handlers/                        # Bot handlers module
│   ├── __init__.py                 # Package initialization
│   ├── command_handler.py         # Command handlers (/start, etc.)
│   └── inline_handler.py          # Inline query handler
│
├── utils/                           # Utility functions module
│   ├── __init__.py                 # Package initialization
│   ├── bible_loader.py             # Bible data loading functions
│   ├── text_utils.py               # Text processing utilities
│   └── user_logger.py             # User logging utilities
│
├── logs/                            # Log files (gitignored)
│
├── main.py                         # Main entry point
├── migrate_files.py                # Script to migrate JSON files
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
└── STRUCTURE.md                    # This file
```

## Module Descriptions

### `config/`
**Purpose**: Centralized configuration management

- **`config.py`**: 
  - Loads environment variables
  - Defines project paths
  - Sets bot configuration constants
  - Creates necessary directories

### `data/`
**Purpose**: Data storage

- **`bible/`**: Contains all 66 Bible books as JSON files
- **`users.txt`**: Logs user IDs and names when they start the bot

### `handlers/`
**Purpose**: Bot interaction handlers

- **`command_handler.py`**: 
  - Handles `/start` command
  - Sends welcome message
  - Logs new users

- **`inline_handler.py`**: 
  - Processes inline queries
  - Handles two query formats:
    - Book + Chapter: `"ምሳሌ 1"`
    - Book + Chapter + Verse: `"ምሳሌ 1:5"`
  - Creates inline query results with search buttons

### `utils/`
**Purpose**: Reusable utility functions

- **`bible_loader.py`**: 
  - Loads all JSON files from data directory
  - Extracts book names from filenames
  - Returns dictionary of all books

- **`text_utils.py`**: 
  - `clean_text()`: Removes reference numbers from verses
  - `suggest_books()`: Fuzzy matching for book names
  - `suggest_chapters()`: Fuzzy matching for chapter numbers

- **`user_logger.py`**: 
  - Logs user information to file
  - Handles file I/O errors gracefully

### Root Files

- **`main.py`**: 
  - Initializes the bot
  - Loads Bible data
  - Registers handlers
  - Starts polling

- **`migrate_files.py`**: 
  - Helper script to move JSON files to data/bible/
  - Useful for initial setup

## Data Flow

1. **Startup** (`main.py`):
   - Load configuration
   - Load Bible data from JSON files
   - Initialize bot
   - Register handlers

2. **User Interaction**:
   - User sends `/start` → `command_handler.py`
   - User types inline query → `inline_handler.py`
   - Handler uses utilities from `utils/` to process request
   - Returns formatted Bible verses

3. **Data Access**:
   - All handlers access `all_books` dictionary
   - Dictionary loaded once at startup
   - Fast in-memory access for queries

## Benefits of This Structure

1. **Separation of Concerns**: Each module has a single responsibility
2. **Maintainability**: Easy to find and modify specific functionality
3. **Scalability**: Easy to add new handlers or utilities
4. **Testability**: Each module can be tested independently
5. **Configuration Management**: Centralized settings in one place
6. **Data Organization**: Clear separation of code and data

## Adding New Features

### New Command
1. Add handler function to `handlers/command_handler.py`
2. Register in `main.py` with `@bot.message_handler(commands=['new'])`

### New Utility Function
1. Add function to appropriate file in `utils/`
2. Export in `utils/__init__.py`
3. Import where needed

### New Configuration
1. Add to `config/config.py`
2. Export in `config/__init__.py`
3. Use throughout codebase
