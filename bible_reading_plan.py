class BibleTracker:
    def __init__(self):
        self.books = {
            "Genesis": False, "Exodus": False, "Leviticus": False, "Numbers": False,
            "Deuteronomy": False, "Joshua": False, "Judges": False, "Ruth": False,
            "1 Samuel": False, "2 Samuel": False, "1 Kings": False, "2 Kings": False,
            "1 Chronicles": False, "2 Chronicles": False, "Ezra": False, "Nehemiah": False,
            "Esther": False, "Job": False, "Psalms": False, "Proverbs": False,
            "Ecclesiastes": False, "Song of Solomon": False, "Isaiah": False, "Jeremiah": False,
            "Lamentations": False, "Ezekiel": False, "Daniel": False, "Hosea": False,
            "Joel": False, "Amos": False, "Obadiah": False, "Jonah": False,
            "Micah": False, "Nahum": False, "Habakkuk": False, "Zephaniah": False,
            "Haggai": False, "Zechariah": False, "Malachi": False,
            "Matthew": False, "Mark": False, "Luke": False, "John": False,
            "Acts": False, "Romans": False, "1 Corinthians": False, "2 Corinthians": False,
            "Galatians": False, "Ephesians": False, "Philippians": False, "Colossians": False,
            "1 Thessalonians": False, "2 Thessalonians": False, "1 Timothy": False, "2 Timothy": False,
            "Titus": False, "Philemon": False, "Hebrews": False, "James": False,
            "1 Peter": False, "2 Peter": False, "1 John": False, "2 John": False,
            "3 John": False, "Jude": False, "Revelation": False
        }

    def mark_as_read(self, book):
        if book in self.books:
            self.books[book] = True
            print(f"{book} marked as read.")
        else:
            print(f"{book} not found in the list of books.")

    def display_progress(self):
        total_books = len(self.books)
        read_books = sum(self.books.values())
        print(f"You have read {read_books} out of {total_books} books.")

    def display_unread_books(self):
        unread_books = [book for book, read_status in self.books.items() if not read_status]
        if unread_books:
            print("Unread books:")
            for book in unread_books:
                print(f"- {book}")
        else:
            print("Congratulations! You have read all the books.")

# Example usage
if __name__ == "__main__":
    tracker = BibleTracker()

    # Manually mark books as read

    # OLD TESTAMENT ---

    #tracker.mark_as_read("Genesis")
    #tracker.mark_as_read("Exodus")
    #tracker.mark_as_read("Leviticus")
    #tracker.mark_as_read("Numbers")
    #tracker.mark_as_read("Deuteronomy")
    #tracker.mark_as_read("Joshua")
    #tracker.mark_as_read("Judges")
    #tracker.mark_as_read("Ruth")
    #tracker.mark_as_read("1 Samuel")
    #tracker.mark_as_read("2 Samuel")
    #tracker.mark_as_read("1 Kings")
    #tracker.mark_as_read("2 Kings")
    #tracker.mark_as_read("1 Chronicles")
    #tracker.mark_as_read("2 Chronicles")
    #tracker.mark_as_read("Ezra")
    #tracker.mark_as_read("Nehemiah")
    #tracker.mark_as_read("Esther")
    #tracker.mark_as_read("Job")
    #tracker.mark_as_read("Psalms")
    #tracker.mark_as_read("Proverbs")
    #tracker.mark_as_read("Ecclesiastes")
    #tracker.mark_as_read("Song of Solomon")
    #tracker.mark_as_read("Isaiah")
    #tracker.mark_as_read("Jeremiah")
    #tracker.mark_as_read("Lamentations")
    #tracker.mark_as_read("Ezekiel")
    #tracker.mark_as_read("Daniel")
    #tracker.mark_as_read("Hosea")
    #tracker.mark_as_read("Joel")
    #tracker.mark_as_read("Amos")
    #tracker.mark_as_read("Obadiah")
    #tracker.mark_as_read("Jonah")
    #tracker.mark_as_read("Micah")
    #tracker.mark_as_read("Nahum")
    #tracker.mark_as_read("Habakkuk")
    #tracker.mark_as_read("Zephaniah")
    #tracker.mark_as_read("Haggai")
    #tracker.mark_as_read("Zechariah")
    #tracker.mark_as_read("Malachi")

    # NEW TESTAMENT --- 

    #tracker.mark_as_read("Matthew")
    #tracker.mark_as_read("Mark")
    #tracker.mark_as_read("Luke")
    #tracker.mark_as_read("John")
    #tracker.mark_as_read("Acts")
    #tracker.mark_as_read("Romans")
    #tracker.mark_as_read("1 Corinthians")
    #tracker.mark_as_read("2 Corinthians")
    #tracker.mark_as_read("Galatians")
    #tracker.mark_as_read("Ephesians")
    #tracker.mark_as_read("Philippians")
    #tracker.mark_as_read("Colossians")
    #tracker.mark_as_read("1 Thessalonians")
    #tracker.mark_as_read("2 Thessalonians")
    #tracker.mark_as_read("1 Timothy")
    #tracker.mark_as_read("2 Timothy")
    #tracker.mark_as_read("Titus")
    #tracker.mark_as_read("Philemon")
    #tracker.mark_as_read("Hebrews")
    #tracker.mark_as_read("James")
    #tracker.mark_as_read("1 Peter")
    #tracker.mark_as_read("2 Peter")
    #tracker.mark_as_read("1 John")
    #tracker.mark_as_read("2 John")
    #tracker.mark_as_read("3 John")
    #tracker.mark_as_read("Jude")
    #tracker.mark_as_read("Revelation")

    # Display progress and list of unread books
    tracker.display_progress()
    tracker.display_unread_books()
