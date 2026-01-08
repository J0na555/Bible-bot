"""Main entry point for the Amharic Bible Bot."""
import telebot

from config import API_TOKEN, DATA_DIR
from utils.bible_loader import load_bible_data
from handlers.inline_handler import handle_inline_query
from handlers.command_handler import handle_start_command


def main():
    """Initialize and run the bot."""
    # Initialize bot
    bot = telebot.TeleBot(API_TOKEN)
    
    # Load Bible data
    print(f"Loading Bible data from {DATA_DIR}...")
    all_books = load_bible_data(DATA_DIR)
    print(f"Loaded {len(all_books)} books")
    
    # Register inline query handler
    @bot.inline_handler(lambda query: len(query.query) > 0)
    def query_handler(query):
        handle_inline_query(bot, query, all_books)
    
    # Register command handlers
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        handle_start_command(bot, message)
    
    # Start polling
    print("Bot is running...")
    bot.infinity_polling()


if __name__ == '__main__':
    main()
