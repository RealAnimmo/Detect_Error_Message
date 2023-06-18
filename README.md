# Error Message detector

A Python script to detect if a sentence contains a error message.

## Description

This script works with the Bag-of-words algorithm to calculate how freequent and important a word is for each document.
After creating a dataset of 84.000 lines, where 26% of the dataset contains error messages.
The Dataset was splitted in to 2 documents/sub datasets, one containing only error messages and the other only non-error messages.
To than calculate how likely it is that a word is more likely related to the error or non-error sub-dataset, doing that for a whole sentence.
By that we can calculate also how likely it is that a sentence is more likely a error message or not.
This tool pickles the needed data to be able to execute the calculation in less than 0.03 seconds.
This tool could be integrated in Bug bounty hunting to find error messages for specific behaviour.



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
![alt text](https://i.postimg.cc/FK0TxgFr/Screenshot-2023-06-18-181049.png)
