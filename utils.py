import nltk
from nltk import word_tokenize # returns a list of words
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.collocations import *
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
stopwords = stopwords.words("english")

def tokenize(text: str) -> list:
	tokenized_text = word_tokenize(text.lower())
	return tokenized_text

def remove_punctuation(tokens: list) -> list:
    # Empty List to store words:
    tokens_no_punc = []

    # Removing punctuation marks :
    for t in tokens:
        if t.isalpha():
            tokens_no_punc.append(t)
    return tokens_no_punc

def remove_stopwords(tokens: list) -> list:  
    # Empty list to store clean words :
	tokens_no_stops = []
    
	# Remove stopwords
	for t in tokens:
		if t not in stopwords:
			tokens_no_stops.append(t)
	return tokens_no_stops

def lemmatize(tokens: list) -> list:
	wnl = WordNetLemmatizer()
	lemmatized_tokens = [wnl.lemmatize(t) for t in tokens]
	return [wnl.lemmatize(t, pos = 'v') for t in lemmatized_tokens]

def noun_only(tokens: list) -> list:
    tagged_tokens = nltk.pos_tag(tokens)
    filtered_tokens =[tt[0] for tt in tagged_tokens if tt[1] in ['NN', 'JJ']]
    return filtered_tokens

# Filter for bigrams with only noun-type structures
def bigram_filter(bigram: list) -> bool:
    tag = nltk.pos_tag(bigram)
    if tag[0][1] not in ['JJ', 'NN'] and tag[1][1] not in ['NN']:
        return False
    if bigram[0] in stopwords or bigram[1] in stopwords:
        return False
    if 'n' in bigram or 't' in bigram:
        return False
    if 'PRON' in bigram:
        return False
    return True

def create_bigrams(tokens: list) -> list:
	# Convert list of tokens nto sequence of words
	tokens_seq = ' '.join(tokens)

	bigram_measures = nltk.collocations.BigramAssocMeasures()
	bigram_finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
	bigram_finder.apply_freq_filter(2)

	raw_bigrams = bigram_finder.nbest(bigram_measures.likelihood_ratio, 10)
	for bg in raw_bigrams:
		if bigram_filter(bg) is False:
			raw_bigrams.remove(bg) 
	bigrams = [' '.join(x) for x in raw_bigrams if len(x[0]) > 2 or len(x[1]) > 2]

	for bigram in bigrams:
		tokens_seq = tokens_seq.replace(bigram, bigram.replace(' ','_'))

	return tokens_seq.split()



	

