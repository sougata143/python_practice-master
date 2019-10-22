#Install NLTK before proceeding with the python program for word tokenization.
#conda install -c anaconda nltk
import nltk
nltk.download('punkt')

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)

#Tokenizing Sentences
sentence_data = "Sun rises in the east. Sun sets in the west."
nltk_tokens2 = nltk.sent_tokenize(sentence_data)
print (nltk_tokens2)