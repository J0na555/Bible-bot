"""Command handlers for the Bible Bot."""
from telebot import types

from utils.user_logger import log_user
from config.config import USERS_FILE


def handle_start_command(bot, message):
    """
    Handle the /start command.
    
    Args:
        bot: TeleBot instance
        message: Message object from Telegram
    """
    # Store user ID and name
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(f"New user: {user_name} (ID: {user_id})")
    
    # Log user to file
    log_user(user_id, user_name, USERS_FILE)
    
    welcome_text = (
        '''Welcome to the Amharic Bible Bot!  
This bot allows you to read Bible by typing the name of the book, chapter, and verse.

Here's an example of how to use it:

First, type @Amh_bible_bot and then leave a space or an open space before continuing...
1. Book Name: For example, to get the names of the books, type 'ዘፍጥረት'
2. After typing the book name, leave a small space and type in the chapter name. For example, to get the first chapter of ዘፍጥረት, type 'ዘፍጥረት 1'
3. To continue with the chapter, type the chapter number (:) by creating two dots. For example, 'ዘፍጥረት 1:1.' You can then follow up with further inquiries.


You can use the buttons below to start reading 

This bot works in channels and groups as well.

If you encounter any issues or have feedback, please inform me @kkyk1286
   '''
    )
    
    # Create inline keyboard
    markup = types.InlineKeyboardMarkup()
    
    # Add the "Search" button that opens the inline query
    search_button = types.InlineKeyboardButton(
        text="Search", 
        switch_inline_query_current_chat=""
    )
    markup.add(search_button)
    
    # Send welcome message with inline keyboard
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
