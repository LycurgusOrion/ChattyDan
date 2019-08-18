import nltk
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open("novels/corpus.txt", "r") as f:
    raw = f.read()
    raw = raw.lower()

    sent_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)


lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(
        nltk.word_tokenize(
            text.lower().translate(remove_punct_dict)
        )
    )


def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()

    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there",
                      "hello", "I am glad! You are talking to me"]


def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


flag = True
print("Dan: My name is Dan. I will answer your queries about myself. If you want to exit, type bye...")

while flag is True:
    user_response = input()
    user_response = user_response.lower()

    if(user_response != 'bye'):

        if('thanks' in user_response or 'thank you' in user_response):
            flag = False
            print("Dan: You are welcome..")

        else:

            if(greeting(user_response) is not None):
                print("Dan: " + greeting(user_response))

            else:
                print("Dan: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)

    else:

        flag = False
        print("Dan: Bye! take care..")
