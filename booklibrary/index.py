import json

class BookCollection:
  
    def __init__(self):
        self.book_list = []
        self.storage_file = "book.json"
        self.read_from_file()

    def read_from_file(self):
        try: 
          with open(self.storage_file, "r") as file:
              self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
        
    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file , indent= 4)

    def create_new_book(self):
        """Add a new book in collection by gathering information from user."""
        book_title = input("Enter the title of book: ")
        book_author = input("Enter author name: ")
        publication_year = input("Publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = input("Have you read the book? (yes/no):").strip().lower()

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read 
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print(f"The book '{book_title}' is added to the collection!\n")

    def delete_book(self):
        """Delete the book from collection using title."""  
        book_title = input("Enter title of the book to remove. ")
        
        for book in self.book_list:
            if book["title"].lower() == book_title:
                self.book_list.remove(book)
                self.save_to_file()
                print(f"The book {book_title} is removed successfully!\n")
                return
            
        print("Book not found\n")


    def find_book(self):
        """Find the book from collection by using Book title or Author name.""" 
        # search_type = input("Search by:\n1. Title\n2. Author Name\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()

        found_books = [
            book 
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["title"].lower()
        ]
        
        if found_books:
            print("Matching Books:\n")
            for index, book in enumerate(found_books, index=1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index} {book["title"]} by {book["aurthor"]} - {book["year"]} - {book["genre"]} - {reading_status}.") 
        else:
            print("No matching books found.!\n")
 

    def update_book(self):
            """Modify the details of an existing book in the collection.""" 
            book_title = input("Enter the title of the book you want to edit: ")
            for book in self.book_list:
              if book["title"] == book_title:
                  print("Leave blank to keep the existing values.")
                  book_title = input(f"New Title: {book['title']}: " ) or book["title"]
                  book_author = input(f"New Author: {book['author']}") or book["author"]
                  book["year"] = input(f"Update year: {book['year']}") or book["year"]
                  book["genre"] = input(f"New genre: {book['genre']}") or book["genre"]
                  book["read"] = input(f"Have you read the book? (yes/no)").strip().lower()
                  self.save_to_file()
                  print("Book Updated successfully!\n")
                  return
            print("Book not found!")

    def show_all_books(self):
        """Display all the book from collection."""
        if not self.book_list:
            print("The collection is empty!\n")
            return 
        for index, book in enumerate(book):
            reading_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} - ({book["year"]}) - {book['genre']} - {book['read']}")

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"] )
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0)
        print(f"Total books in collection: {total_books}")
        print(f"Reading Progress: {completion_rate}")

    def start_application(self):
        """Run the main application loop with a user friendly menu interface."""
        while True:
            print("****************** Welcome to Your Book Collection manager!**************")
            print("1. Create a new book")
            print("2. Delete book")
            print("3. Search for a book")
            print("4. Update book")
            print("5. Show all book collection")
            print("6. Show reading progress")
            print("7. Exit")
            
            user_choice = input("Please choose an option (1-7): ")

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
                print("Thank you for using Book Collection Manager. Goodby!") 
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    library = BookCollection()
    library.start_application()


          

        

              



           


