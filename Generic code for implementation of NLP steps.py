# ================================================================================
# ======================= Libraries ==============================================
# ================================================================================
import nltk                                         # Used for performing the steps of NLP

from nltk import word_tokenize                      # For splitting strings into tokens
from nltk.probability import FreqDist               # Count the number of times that each token of an experiment occurs
from nltk.tokenize import blankline_tokenize        # Tokenize a string, treating any sequence of blank lines as a delimiter.

from nltk.stem import PorterStemmer                 # Used for removing the "ing" endings from words
from nltk.stem import LancasterStemmer              # Used for removing the inflexional endings from words


from nltk.stem import WordNetLemmatizer             # Used for converting the word into its meaningful base form
from nltk.corpus import stopwords                   # Used for removing the stop words

from nltk import ne_chunk                           # Used to perform grouping of tokens
# ================================================================================



# ================================================================================
# ======================= For the string from the user ===========================
# ================================================================================
x= input("Enter the string: ")
# ================================================================================



# ================================================================================
# ======================== Tokenization ==========================================
# ================================================================================
x_token = word_tokenize(x)
f = FreqDist()

print(x_token)
print("Number of tokens in the string: ", len(x_token))

for word in x_token:
    f[word.lower()] = f[word.lower()] + 1
print(f)
print("The 10 most occuring tokens are:\n", f.most_common(10))

x_blank = blankline_tokenize(x)
print("Number of blank lines within the string: ", len(x_blank))

x_bigrams = list(nltk.bigrams(x_token))
print(x_bigrams)

x_trigrams = list(nltk.trigrams(x_token))
print(x_trigrams)

x_ngrams = list(nltk.ngrams(x_token, 4))
print(x_ngrams)
# =======================================================================



# ========================================================================
# ======================== Stemming ======================================
# ========================================================================
ps = PorterStemmer()
for words in x_token:
    print(words + ": " + ps.stem(words))

ls = LancasterStemmer()
for words in x_token:
    print(words + ": " + ls.stem(words))
# ========================================================================




# =========================================================================
# ======================= Lemmatization ===================================
# =========================================================================
lm = WordNetLemmatizer()
for words in x_token:
    print(words + ": " + lm.lemmatize(words))

print(stopwords.words('english'))
print("Number of stopwords in the string: ", len(stopwords.words('english')))
# ==========================================================================



# ==========================================================================
# ============= Part of Speech Tags & Named Entity Recognition =============
# ==========================================================================
for token in x_token:
    post = nltk.pos_tag([token])
    print(post)
e = ne_chunk(post)
print(e)
# ==========================================================================



# ==========================================================================
# =========================== Chunking =====================================
# ==========================================================================
g = r"NP: {<DT>?<JJ>?<NN>}"
c = nltk.RegexpParser(g)
c_result = c.parse(post)
c_result.draw()