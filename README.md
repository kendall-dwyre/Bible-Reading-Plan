# Bible-Reading-Plan
The purpose of this repository is to provide some code that someone could use if they wanted to keep track of the how many books of the Bible they have read.  

The books of the Bible follow the typical 66 in the Protestant Bible.  In order to use the code, all you have to do is uncomment the books that you have read.  For instance, let's look at the four Gospel (meaning Good News) accounts: 

    tracker.mark_as_read("Matthew")
    tracker.mark_as_read("Mark")
    #tracker.mark_as_read("Luke")
    #tracker.mark_as_read("John")

If this code were ran, the output say:

    Matthew marked as read.
    Mark marked as read.

However, Luke and John would not be marked as read since they still have the comment.  

Lastly, you can use this code for more than just a Bible Reading Plan.  This code can be a template for anything else that may be a plan or list that you would like to keep track of. 
