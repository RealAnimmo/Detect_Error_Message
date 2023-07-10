# Error Message detector

This Python script is designed to identify whether a given sentence contains an error message.

## Description

This script works with the Bag-of-words algorithm to calculate how freequent and important a word is for each document.
After creating multiple slightly different datasets with +-84.000 lines, where +-26% of the datasets contains error messages.
The datasets got splited into two sub-datasets: one containing only error messages and the other containing non-error messages.
This division enables the calculation of the likelihood that a word is associated with either the error or non-error sub-dataset, extending to the evaluation of entire sentences.
As a result, the script can determine the probability that a given sentence is an error message.
By serializing the necessary data, the tool is able to perform the calculations in less than 0.03 seconds.
This functionality can be integrated into bug bounty hunting activities to identify error messages related to specific behaviors.
The Dataset contains Error messages from:

 * Windows
  
 * Linux
  
 * MacOS
  
 * Multiple different SQL Databases
  
 * DB2
  
 * HTTP
  
 * Javascript
  
 * Oracle
  
 * PHP
  
 * Pointbase
  
 * Sybase
  



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
* Unzip TextAndErrorMessages-3.7z


### Executing program

* Start to build the pickled object with the 1_Preprocess_and_serialize_dataset.py
```
Python3 1_Preprocess_and_serialize_dataset.py
```
* Now you can change the error message in the second last line of 2_Predict_if_text_is_error_message_or_text.py where the function predict_text() gets called.
```
python3 2_Predict_if_text_is_error_message_or_text.py
```



### Performance

The sentence "sorry, either you mistyped the url or we deleted that page, but let's agree to blame this on you." got successfully detected as a Error message.

NOTE: the number that is closer to 0 is True, in the following example: ```Error Score: is -91``` and ```Non-Error Score is -93``` that means Error score is close to 0 and this message got detected as a error message. The output also displays how biased each word is compared to the 2 subdatasets(Error messages, Non-Error messages), by the scores we can see that ```url``` and ```deleted``` are very biased and more related to error messages than non-error messages.


![alt text](https://i.postimg.cc/FK0TxgFr/Screenshot-2023-06-18-181049.png)

### Performance with slightly different datasets
This section provides an overview of the performance achieved by training models using slightly different datasets. By increasing and diversifying the dataset, the likelihood of words appearing in multiple datasets is enhanced. Consequently, this can lead to a shift in the bias associated with these words.

Fraction Error Correctly Detected: 0.8691330756488128 3-cleared.csv

Fraction Error Correctly Detected: 0.8759561711804837 2.csv

Fraction Error Correctly Detected: 0.9509260511017981 1.csv

