import sys
import io
import json
import os

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class BookCollection:
    """A class to manage a collection of books"""
    def __init__(self):
        """Initialize the book collection"""
        self.book_list = []
        self.storage_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books_data.json")
        self.read_from_file()
        print(f"Loaded books: {len(self.book_list)}")  

    def read_from_file(self):
        """Load books from JSON file"""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, "r", encoding='utf-8') as file:
                    self.book_list = json.load(file)
                print("Books loaded successfully")
            else:
                print("No existing data file found, starting with empty collection")
                self.book_list = []
        except Exception as e:
            print(f"Error loading books: {e}")
            self.book_list = []

    def save_to_file(self):
        """Save books to JSON file"""
        try:
            with open(self.storage_file, "w", encoding='utf-8') as file:
                json.dump(self.book_list, file, indent=4, ensure_ascii=False)
            print("Books saved successfully")
        except Exception as e:
            print(f"Error saving books: {e}")

    def create_new_book(self):
        """Add a new book to the collection"""
        print("\nAdd new book:")
        book_title = input("Title: ")
        book_author = input("Author: ")
        publication_year = input("Publication year: ")
        book_genre = input("Genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print(f"Book '{book_title}' has been added to your collection.")

    def delete_book(self):
        """Remove a book from the collection"""
        book_title = input("Enter title of book to remove: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")

    def find_book(self):
        """Search for books in the collection"""
        search_text = input("Enter search term: ").lower()
        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]
        
        if found_books:
            print("\nMatching books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("\nNo matching books found.")

    def update_book(self):
        """Update book details"""
        book_title = input("Enter title of book to update: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("\nLeave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
                self.save_to_file()
                print("\nBook updated successfully!")
                return
        print("\nBook not found!")

    def show_all_books(self):
        """Display all books in the collection"""
        if not self.book_list:
            print("\nYour collection is empty.")
            return
        
        print("\nYour Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")

    def show_reading_progress(self):
        """Show reading progress statistics"""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0

        print(f"\nTotal books in collection: {total_books}")
        print(f"Books read: {completed_books}")
        print(f"Reading progress: {completion_rate:.2f}%")

    def start_application(self):
        """Run the application"""
        while True:
            print("\n" + "="*50)
            print("📖 Welcome to Your Book Collection Manager!".center(50))
            print("="*50)
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit\n")

            try:
                user_choice = input("Please choose an option (1-7): ").strip()
                
                if user_choice == "1": 
                    self.create_new_book()
                elif user_choice == "2":
                    self.delete_book()
                elif user_choice == "3":
                    self.find_book()
                elif user_choice == "4":
                    self.update_book()
                elif user_choice == "5":
                    self.show_all_books()
                elif user_choice == "6":
                    self.show_reading_progress()
                elif user_choice == "7":
                    self.save_to_file()
                    print("\nThank you for using Book Collection Manager. Goodbye!")
                    break
                else: 
                    print("\nInvalid choice. Please enter a number between 1-7.")
            except Exception as e:
                print(f"\nAn error occurred: {e}. Please try again.")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()