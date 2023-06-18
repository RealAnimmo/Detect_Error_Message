import pandas as pd
import numpy as np
import pickle
import time

start_time = time.time()

# Load the serialized data
with open('serialized_data-2.pickle', 'rb') as file:
        data = pickle.load(file)
#print(len(data))

# Extract the required data
fraction_error_messages = data['fraction_error_messages']
train_error_bow = data['train_error_bow']
train_non_error_messages_bow = data['train_non_error_messages_bow']

#predict error message function
def predict_text(t, verbose=True):
        #Filter the word if the word does not appear in the lists of words
        valid_words = [w for w in t if w in train_error_bow]
        #get the probabilities of each valid word showing up in train_error_messages_bow and train_non_error_messages_bow
        error_probs = [train_error_bow[w] for w in valid_words]
        non_error_probs = [train_non_error_messages_bow[w] for w in valid_words]
        if verbose:
                data_df = pd.DataFrame()
                data_df['word'] = valid_words
                data_df['error_prob'] = error_probs
                data_df['non_error_prob'] = list(np.around(np.array(non_error_probs),6))
                data_df['ratio'] = [s/n if n > 0 else np.inf for s,n in zip(error_probs, non_error_probs)]
                print(data_df)
        #calculate error score as sum of logs for all probabilities
        error_score = sum([np.log(p) for p in error_probs]) + np.log(fraction_error_messages)
        #calculate non_error score as sum of logs for all probabilities
        non_error_score = sum([np.log(p) for p in non_error_probs]) + np.log(1-fraction_error_messages)
        #if verbose, report 2 scores
        if verbose:
                print('Error Score: %s'%error_score)
                print('Non-Error Score: %s'%non_error_score)
        #if error score is higher than non_error score, mark it as error
        return (error_score >= non_error_score)

predict_text("sorry, either you mistyped the url or we deleted that page, but let's agree to blame this on you.".split(), verbose=True)


print("--- %s seconds ---" % (time.time() - start_time))
