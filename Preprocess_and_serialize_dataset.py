import pandas as pd
import numpy as np
import string
import pickle
from predictor_function import predict_text
import time

start_time = time.time()

#Read Dataset
all_messages = pd.read_csv('TextAndErrorMessages-2.csv', encoding='ISO-8859-1')
#Fill all the 42 NaN with value 0
all_messages = all_messages.fillna(0)
#delete last row.
all_messages.drop(all_messages.tail(1).index, inplace=True)
#lowercase everything and remove punctuation.
def preprocess_text(text):
        if isinstance(text, str):
                text = text.lower()  # Convert to lowercase
                text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        return text
# Apply the preprocessing function to the "Text Or Error Message" column
all_messages['Text Or Error Message'] = all_messages['Text Or Error Message'].apply(preprocess_text)
#Shuffle data
all_messages = all_messages.sample(frac=1)
#print(all_messages.tail())
#get Training set
train_all_messages = all_messages.iloc[:int(len(all_messages)*0.7)]
#get Testing set
test_all_messages = all_messages.iloc[int(len(all_messages)*0.7):]
# % of Error messages from the Training set
fraction_error_messages = train_all_messages['Error = 1 Not Error = 0'].mean()
print(fraction_error_messages)
# Convert the values in "Text Or Error Message" column to strings
#test_all_messages["Text Or Error Message"] = test_all_messages["Text Or Error Message"].astype(str)
# get all words from error_messages and non_errormessages datasets.
train_error_messages = ' '.join(train_all_messages[train_all_messages["Error = 1 Not Error = 0"] == 1]['Text Or Error Message'].astype(str)).split(' ')
train_non_error_messages = ' '.join(train_all_messages[train_all_messages["Error = 1 Not Error = 0"] == 0]['Text Or Error Message'].astype(str)).split(' ')
#print(train_non_error_messages)
#create a intersection for train_error_messages and train_non_error_messages.
common_words = set(train_error_messages).intersection(set(train_non_error_messages))
#print(common_words)
#create a key value dictionary for the error messages, with the name of the word as key and the frequency of that word compared to all the words as the value
train_error_bow = dict()
for w in common_words:
        train_error_bow[w] = train_error_messages.count(w) / len(train_error_messages)
#create a key value dictionary for the error messages, with the name of the word as key and the frequency of that word compared to all the words as the value
train_non_error_messages_bow = dict()
for w in common_words:
        train_non_error_messages_bow[w] = train_non_error_messages.count(w) / len(train_non_error_messages)
#print(train_error_bow)
#Create specify the needed data to serealize
data = {
        'fraction_error_messages': fraction_error_messages,
        'train_error_bow': train_error_bow,
        'train_non_error_messages_bow': train_non_error_messages_bow
}

with open('serialized_data-2.pickle', 'wb') as file:
        pickle.dump(data, file)


#predict error message function
#def predict_text(t, verbose=True):
        #Filter the word if the word does not appear in the lists of words
#       valid_words = [w for w in t if w in train_error_bow]
        #get the probabilities of each valid word showing up in train_error_messages_bow and train_non_error_messages_bow
#       error_probs = [train_error_bow[w] for w in valid_words]
#       non_error_probs = [train_non_error_messages_bow[w] for w in valid_words]
#       if verbose:
#               data_df = pd.DataFrame()
#               data_df['word'] = valid_words
#               data_df['error_prob'] = error_probs
#               data_df['non_error_prob'] = list(np.around(np.array(non_error_probs),6))
#               data_df['ratio'] = [s/n if n > 0 else np.inf for s,n in zip(error_probs, non_error_probs)]
#               print(data_df)
        #calculate error score as sum of logs for all probabilities
#       error_score = sum([np.log(p) for p in error_probs]) + np.log(fraction_error_messages)
        #calculate non_error score as sum of logs for all probabilities
#       non_error_score = sum([np.log(p) for p in non_error_probs]) + np.log(1-fraction_error_messages)
        #if verbose, report 2 scores
#       if verbose:
#               print('Error Score: %s'%error_score)
#               print('Non-Error Score: %s'%non_error_score)
        #if error score is higher than non_error score, mark it as error
#       return (error_score >= non_error_score)

#print(predict_text("sorry, either you mistyped the url or we deleted that page, but let's agree to blame this on you.".split(), verbose=True))
#calculate the accuracy of determen if the given text is a error message or not tested on the tasting data.
#predictions = test_all_messages['Text Or Error Message'].apply(lambda t: predict_text(str(t).split()))
#calculate the fraction of error messages that got correctly detected.
#frac_error_messages_correctly_detected = np.sum((predictions == True) & (test_all_messages['Error = 1 Not Error = 0'] == True)) / np.sum(test_all_messages['Error = 1 Not Error = 0'] == True)
#print('Fraction Error Correctly Detected: %s'%frac_error_messages_correctly_detected)
print("--- %s seconds ---" % (time.time() - start_time))

