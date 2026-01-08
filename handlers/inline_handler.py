"""Inline query handler for Bible search."""
from telebot import types
from typing import List

from utils.text_utils import suggest_books, clean_text
from config.config import CACHE_TIME, MAX_SUGGESTIONS


def handle_inline_query(bot, query, all_books: dict):
    """
    Handle inline queries for Bible search.
    
    Args:
        bot: TeleBot instance
        query: Inline query object from Telegram
        all_books: Dictionary of all Bible books
    """
    user_input = query.query.strip()
    results = []

    if ':' not in user_input:  # User typed a book and chapter (e.g., 'ምሳሌ 1')
        try:
            book_name, chapter_input = user_input.rsplit(' ', 1)  # Split book and chapter
            suggested_books = suggest_books(book_name, all_books, MAX_SUGGESTIONS)
            if suggested_books:
                closest_book_name, _, _ = suggested_books[0]
                chapter = int(chapter_input)

                # Check if the chapter exists in the book
                if chapter <= len(all_books[closest_book_name]):
                    verses = all_books[closest_book_name][chapter - 1]['verses']
                    
                    # Display all verses in the chapter
                    verses_to_display = verses[:]
                    verse_texts = "\n".join(
                        f"{i + 1}: {clean_text(verse)}" 
                        for i, verse in enumerate(verses_to_display)
                    )

                    # Create inline keyboard with search button
                    keyboard = types.InlineKeyboardMarkup()
                    search_button = types.InlineKeyboardButton(
                        text="Search", 
                        switch_inline_query_current_chat=""
                    )
                    keyboard.add(search_button)

                    # Add the result for the inline query
                    results.append(
                        types.InlineQueryResultArticle(
                            id=f"chapter_{closest_book_name}_{chapter}",
                            title=f"{closest_book_name} {chapter}",
                            input_message_content=types.InputTextMessageContent(
                                f"{closest_book_name} {chapter} \n {verse_texts}"
                            ),
                            description=f" `{closest_book_name}   ምዕራፍ {chapter}   \n{verse_texts}`",
                            reply_markup=keyboard
                        )
                    )
        except (ValueError, IndexError):
            pass

    else:  # User typed the full chapter:verse (e.g., 'ምሳሌ 1:5')
        try:
            book_chapter, verse_input = user_input.rsplit(':', 1)  # Split chapter and verse
            book_name, chapter_input = book_chapter.rsplit(' ', 1)
            chapter, verse = int(chapter_input), int(verse_input)

            suggested_books = suggest_books(book_name, all_books, MAX_SUGGESTIONS)
            if suggested_books:
                closest_book_name, _, _ = suggested_books[0]

                # Check if the chapter and verse exist in the book
                if chapter <= len(all_books[closest_book_name]):
                    verses = all_books[closest_book_name][chapter - 1]['verses']
                    if verse <= len(verses):
                        full_verse = clean_text(verses[verse - 1])

                        # Create inline keyboard with search button
                        keyboard = types.InlineKeyboardMarkup()
                        search_button = types.InlineKeyboardButton(
                            text="Search", 
                            switch_inline_query_current_chat=""
                        )
                        keyboard.add(search_button)

                        # Add the result for the inline query
                        results.append(
                            types.InlineQueryResultArticle(
                                id=f"verse_{closest_book_name}_{chapter}_{verse}",
                                title=f"{closest_book_name} {chapter}:{verse}",
                                input_message_content=types.InputTextMessageContent(
                                    f"`{full_verse}\n — {closest_book_name} {chapter}:{verse} `"
                                ),
                                description=full_verse,
                                reply_markup=keyboard
                            )
                        )
        except (ValueError, IndexError):
            pass

    bot.answer_inline_query(query.id, results, cache_time=CACHE_TIME)
