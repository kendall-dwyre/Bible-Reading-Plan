class BibleTracker:
    def __init__(self):
        self.old_testament = {
            "Genesis": False, "Exodus": False, "Leviticus": False, "Numbers": False,
            "Deuteronomy": False, "Joshua": False, "Judges": False, "Ruth": False,
            "1 Samuel": False, "2 Samuel": False, "1 Kings": False, "2 Kings": False,
            "1 Chronicles": False, "2 Chronicles": False, "Ezra": False, "Nehemiah": False,
            "Esther": False, "Job": False, "Psalms": False, "Proverbs": False,
            "Ecclesiastes": False, "Song of Solomon": False, "Isaiah": False, "Jeremiah": False,
            "Lamentations": False, "Ezekiel": False, "Daniel": False, "Hosea": False,
            "Joel": False, "Amos": False, "Obadiah": False, "Jonah": False,
            "Micah": False, "Nahum": False, "Habakkuk": False, "Zephaniah": False,
            "Haggai": False, "Zechariah": False, "Malachi": False
        }

        self.new_testament = {
            "Matthew": False, "Mark": False, "Luke": False, "John": False,
            "Acts": False, "Romans": False, "1 Corinthians": False, "2 Corinthians": False,
            "Galatians": False, "Ephesians": False, "Philippians": False, "Colossians": False,
            "1 Thessalonians": False, "2 Thessalonians": False, "1 Timothy": False, "2 Timothy": False,
            "Titus": False, "Philemon": False, "Hebrews": False, "James": False,
            "1 Peter": False, "2 Peter": False, "1 John": False, "2 John": False,
            "3 John": False, "Jude": False, "Revelation": False
        }

    def mark_as_read(self, book):
        if book in self.old_testament:
            self.old_testament[book] = True
            print(f"{book} marked as read (Old Testament).")
        elif book in self.new_testament:
            self.new_testament[book] = True
            print(f"{book} marked as read (New Testament).")
        else:
            print(f"{book} not found in the list of books.")

    def display_progress(self):
        total_books = len(self.old_testament) + len(self.new_testament)
        read_books = sum(self.old_testament.values()) + sum(self.new_testament.values())
        print(f"You have read {read_books} out of {total_books} books.")

        old_testament_read = sum(self.old_testament.values())
        print(f"Old Testament: {old_testament_read} out of {len(self.old_testament)} books read.")

        new_testament_read = sum(self.new_testament.values())
        print(f"New Testament: {new_testament_read} out of {len(self.new_testament)} books read.")

    def display_unread_books(self):
        unread_books = [book for book, read_status in {**self.old_testament, **self.new_testament}.items() if not read_status]
        if unread_books:
            print("Unread books:")
            for book in unread_books:
                print(f"- {book}")
        else:
            print("Congratulations! You have read all the books.")

    def reset_progress(self):
        self.old_testament = {book: False for book in self.old_testament}
        self.new_testament = {book: False for book in self.new_testament}
        print("Progress has been reset.")

# Example usage
if __name__ == "__main__":
    tracker = BibleTracker()

    # Uncomment lines as you complete reading the books.
    
    # OLD TESTAMENT ---
    # tracker.mark_as_read("Genesis")
    # tracker.mark_as_read("Exodus")
    # tracker.mark_as_read("Leviticus")
    # tracker.mark_as_read("Numbers")
    
    # NEW TESTAMENT ---
    # tracker.mark_as_read("Matthew")
    # tracker.mark_as_read("Mark")
    # tracker.mark_as_read("Luke")
    # tracker.mark_as_read("John")

    # Display progress and list of unread books
    tracker.display_progress()
    tracker.display_unread_books()
