***** HOW TO USE this python script *******

PURPOSE: To convert Mysql part of the PHP code older than version 7 to PHP version 7


LIMITATIONS: Only mysql_qyery function is supported right now. Rest are in pipline. Reach out for requests.

HOW TO USE: Download the upgradephp7.py file and run the program with one parameter providing the Directory location where all the files are placed which are to be upgraded.

py upgradephp7.py <directory_location>

RESULT: All the files in this directory will be overwritten with the resultant text if there is a match found. 
The connection parameter is assumed to be $cn if the function mysql_query is not using any connection parameter.

*************************************************
