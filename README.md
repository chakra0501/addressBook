# addressBook
To run the files for this application, first open 
the driver.py,AnalysisRuntime.py, and AnalysisOperations.py files 
in your preferred IDE which supports Python.

The driver.py file is the interface for the text-based application we designed. 
The user can interact with this file to explore the features
of our application.

The AnalysisRuntime.py and AnalysisOperations.py files are two driver classes 
to collect data on our Skip List implementation's performance. 
 
Running AnalysisRuntime.py will provide data about the runtime for 
the insert() and search() methods of or Skip List implementation.

Running AnalysisOperations.py will provide data
on the average number of operations that the insert() and search()
methods of our Skip List implementation use when inserting or searching data. 

Once AnalysisRuntime.py or AnalysisOperations.py finish collecting data, the two files
will write the data to the two files insertData.txt and searchData.txt. The file insertData.txt
will store runtime and operations data for the insert() method of our Skip List implementation.
The file searchData.txt will store runtime and operations data for the search() method of our
Skip List implementation.

The dataset that we are using to collect runtime and operations is stored in dataset.txt. 
It contains 200 distinct, randomly-generated Strings. We gathered this data using a 
random-String generation at the following link: https://www.random.org/strings/

The files runtimeDataForInsertAnalysis.txt and runtimeDataForSearchAnalysis.txt contain the data 
that we used to make the graphs in section 6 showing
the logarithmic runtime of the insert() and search() methods of our Skip List implementation respectively.
