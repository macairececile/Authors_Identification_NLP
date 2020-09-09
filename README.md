# NLP project

FIRST RUN THE Produce_Author_File, this going back the folder where the books are will generate a full alphabetically ordered author list and put it in a file, the same one that you have the program in.

Please change the path to reflect where the books are, the path is at the top of the program below import csv

Second Run the Test_Books file, Also change the path to were the same books that you assigned for Produce_Author_File are (Same path)

All the things you need to change are at the bottom in the def loadinbooks():

But also change the first path to the type of books you want to change, the firstpart variable indicates the type of books you test, whether it is processed by POS or processed by sentences etc. I may even be plain.

You are free to change the input list for the philosophers as you wish, it's case sensitive though.

When you want to test your own procedures, paste them above loadinbooks and trigger them after the display score, this is where you assign a result list which stores the results for each book.

Finally pass the result list and the result for the authors, displayscore will display it nicely

2 runs of the procedure need to be compute. The first run will be for the non test books. Be careful to store the data in the data_authors.csv file (you need to specify the name of the fil in the create_csv function in the Test_Books file). 
After, you can see your results with the PCA_authors python script. 

The second run will be for your test book (only one can be tested). Your text file needs to have this name form : ...._unknow_nameofyourbook.
Run the Test_Books file after changing the name of the csv file from data_authors.csv to data_authors2.csv. 
Then, run the PCA_new_text python script in order to display nicely your data. You will see your unknow text in the graph. 
