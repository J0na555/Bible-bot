"""Text processing utilities."""
from rapidfuzz import process


def clean_text(text: str) -> str:
    """
    Remove the reference number and title from the text.
    
    Args:
        text: The verse text that may contain reference numbers
        
    Returns:
        Cleaned text without reference numbers
    """
    parts = text.split(' - ', 1)  # Split on the first occurrence of ' - '
    if len(parts) > 1:
        return parts[1].strip()
    return text.strip()


def suggest_books(user_input: str, all_books: dict, limit: int = 5) -> list:
    """
    Suggest book names based on fuzzy matching.
    
    Args:
        user_input: User's input text
        all_books: Dictionary of all Bible books
        limit: Maximum number of suggestions to return
        
    Returns:
        List of tuples (book_name, score, index)
    """
    matched_books = process.extract(user_input, all_books.keys(), limit=limit)
    return matched_books


def suggest_chapters(book_name: str, chapter_input: str, all_books: dict, limit: int = 5) -> list:
    """
    Suggest chapters based on fuzzy matching.
    
    Args:
        book_name: Name of the Bible book
        chapter_input: User's chapter input
        all_books: Dictionary of all Bible books
        limit: Maximum number of suggestions to return
        
    Returns:
        List of tuples (chapter_number, score, index) or empty list if book not found
    """
    if book_name in all_books:
        chapters = all_books[book_name]
        chapter_numbers = [i + 1 for i in range(len(chapters))]
        matched_chapters = process.extract(chapter_input, map(str, chapter_numbers), limit=limit)
        return matched_chapters
    return []
