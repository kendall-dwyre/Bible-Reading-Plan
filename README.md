# Bible Reading Plan Tracker

## Overview
This repository provides a simple and effective Python script to track your progress reading the 66 books of the Protestant Bible. With this tracker, you can mark the books you've read and view your progress at any time. The script is designed to be flexible, so you can also modify it to track any other type of reading plan or checklist.

## How to Use
1. Clone or Download this repository to your local machine.
2. Open the Python Script (or copy it to your own project) in your preferred development environment (e.g., VS Code, PyCharm, or even Google Colab).
3. Uncomment the books you have read by removing the # from the line next to the corresponding tracker.mark_as_read("BookName") function.
4. Run the Script to track your progress.

## Example: Tracking the Gospels
If you’ve read the books of Matthew and Mark but still have Luke and John to go, your script should look like this:

    tracker.mark_as_read("Matthew")
    tracker.mark_as_read("Mark")
    #tracker.mark_as_read("Luke")
    #tracker.mark_as_read("John")
    
When you run the code, the output will display:

    Matthew marked as read.
    Mark marked as read.
    
Luke and John will remain unread as they are still commented out.

## Checking Your Progress
At the end of the script, the tracker will automatically display:

* How many books you've read out of the total 66.
* A list of books you have yet to read.
  
You can use this to stay motivated and keep track of where you are in your reading plan.

## Additional Features
* Old and New Testament Sections: The tracker splits the Bible into the Old and New Testaments, allowing you to see your progress in each section.
* Reset Option: If you’d like to start your plan over, the code includes a simple reset function to clear your progress.
* Flexible for Other Plans: Although designed for tracking Bible reading, this script can be easily modified to track any type of reading list or checklist by simply replacing the Bible books with your own items.
  
## Running the Script in Google Colab
If you're unfamiliar with Python programming or don’t have a local environment set up, you can use Google Colab to run the code online:

1. Visit Google Colab.
2. Create a new notebook.
3. Copy and paste the code from this repository into a cell in your notebook.
4. Customize by uncommenting the books you've read.
5. Run the cell to track your progress!
   
## Conclusion
This simple Bible Reading Tracker is designed to help you stay organized and motivated on your journey through the Bible. You can also customize it for any list-based project, making it a versatile tool for personal tracking.

Feel free to share or modify this project to suit your needs!
