import nltk
import sys
import os
import collections
import math


FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dic=dict()
    for file in os.listdir(directory):
        with open(os.path.join(directory,file), encoding='utf8') as f:
            dic[file]=f.read()
    return dic
            



def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    stopword=nltk.corpus.stopwords.words("english")
    token=[x.lower() for x in nltk.tokenize.word_tokenize(document) if 'a'<=x<'z' or 'A'<=x<='Z']
    nostopwords=[x for x in token if x not in stopword]
    return nostopwords



def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    words=[]
    idf=dict()
    for i in documents:
        words+=documents[i]
    words=set(words)
    for i in words:
        count=0
        for j in documents:
            if i in documents[j]:
                count+=1
        idf[i]=math.log(len(documents)/count)

    return idf


    
    


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    wordcount=dict()
    tfidf=dict()
    for i in files:
        wordcount[i]=collections.Counter(files[i])
        tfidf[i]=0

    
    for i in query:
        for j in wordcount:
            if i in wordcount[j]:
                tfidf[j]+=idfs[i]*wordcount[j][i]
    
    a = sorted(tfidf.items(), key=lambda x: x[1],reverse=True)   
    b=[x[0] for x in a]

    return b[:n]

                
                
        
        


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    matchingword=dict()
    wordcount=dict()
    for i in sentences:
        wordcount[i]=collections.Counter(sentences[i])
        matchingword[i]=[0,0]


    for i in query:
        for j in sentences:
            if i in sentences[j]:
                matchingword[j][0]+=idfs[i]
                matchingword[j][1]+=1/len(sentences[j])
    
    a = sorted(matchingword.items(), key=lambda x: x[1],reverse=True)
    b=[x[0] for x in a]

    return b[:n]
    


if __name__ == "__main__":
    main()
