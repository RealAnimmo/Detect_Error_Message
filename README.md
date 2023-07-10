# Error Message detector

This Python script is designed to identify whether a given sentence contains an error message.

## Description

This script works with the Bag-of-words algorithm to calculate how freequent and important a word is for each document.
After creating multiple slightly different datasets 1x with +-84.000 lines and 1x with 114.000 lines, from which +-29% contains error messages.
The datasets got splited into two sub-datasets: one containing only error messages and the other containing non-error messages.
This division enables the calculation of the likelihood that a word is associated with either the error or non-error sub-dataset, extending to the evaluation of entire sentences.
As a result, the script can determine the probability that a given sentence is an error message.
By serializing the necessary data, the tool is able to perform the calculations in less than 0.03 seconds.
This functionality can be integrated into bug bounty hunting activities to identify error messages related to specific behaviors.

    



## Getting Started

### Dependencies

* numpy==1.24.3
* pandas==2.0.1
* python-dateutil==2.8.2
* pytz==2023.3
* six==1.16.0
* tzdata==2023.3


### Installing

* python3 -m pip install -r requirements.txt
* Unzip ___TextAndErrorMessages-2_cleaned.7z___ or ___TextAndErrorMessages_cleaned.7z___


### Executing program

* Start to build the pickled object with the ___1_Preprocess_and_serialize_dataset.py___

NOTE: at line 11 in ___1_Preprocess_and_serialize_dataset.py___ you have to specify the name of the unziped csv dataset file.
```
Python3 1_Preprocess_and_serialize_dataset.py
```
* Now you can change the error message in the second last line of ___2_Predict_if_text_is_error_message_or_text.py___ where the function ___predict_text()___ gets called.
```
python3 2_Predict_if_text_is_error_message_or_text.py
```



## Performance

The sentence ___"sorry, either you mistyped the url or we deleted that page, but let's agree to blame this on you."___ got successfully detected as a Error message.

NOTE: the number that is closer to 0 is True, in the following example: ```Error Score: is -91``` and ```Non-Error Score is -93``` that means Error score is close to 0 and this message got detected as a error message. The output also displays how biased each word is compared to the 2 subdatasets(Error messages, Non-Error messages), by the scores we can see that ```url``` and ```deleted``` are very biased and more related to error messages than non-error messages.


![alt text](https://i.postimg.cc/FK0TxgFr/Screenshot-2023-06-18-181049.png)

### Performance with slightly different datasets
This section provides an overview of the performance and accuracy achieved by the training model using both datasets. By increasing and diversifying the dataset, the likelihood of words appearing in multiple datasets is enhanced. Consequently, this can lead to a shift in the bias associated with these words.


#### TextAndErrorMessages-2_cleaned.csv Fraction Error Correctly Detected: 0.8759561711804837

Meaning that this model predicted for 87% the right answers while testing thousands of neverseen sentences.

TextAndErrorMessages-2_cleaned.csv contains Error messages from:

    1. Android
    2. C
    3. C#
    4. COBOL
    5. DB2
    6. Firebase
    7. HPWorkstation
    8. HSQL
    9. HTTP
    10. Java
    11. Javascript
    12. Linux
    13. MacOs
    14. MySQL
    15. Oracle
    16. Perl
    17. PHP
    18. Pointbase
    19. PostgreSQL
    20. Python
    21. Solaris
    22. SQLServer
    23. Sybase
    24. Windows






#### TextAndErrorMessages_cleaned.csv Fraction Error Correctly Detected: 0.9509260511017981

Meaning that this model predicted for 95% the right answers while testing thousands of neverseen sentences.

TextAndErrorMessages_cleaned.csv contains Error messages from:

    1. DB2
    2. HSQL
    3. HTTP
    4. Javascript
    5. Linux
    6. MySQL
    7. Oracle
    8. PHP
    9. Pointbase
    10. PostgreSQL
    11. SQLServer
    12. Sybase
    13. Windows
