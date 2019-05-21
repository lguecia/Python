from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    # take in string inputs a, b
    # split each string into lines
    lineA = a.split("\n")
    lineB = b.split("\n")
    # compute a list of lines that appear in both a and b using data structure (list, set)
    # return the list that contains all lines present in string a and b, avoiding duplicates
    return list(set(lineA).intersection(lineB))


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    # take in string inputs a, b
    # split each string into sentences
    sentenceA = set(sent_tokenize(a))
    sentenceB = set(sent_tokenize(b))
    # calculate the list of sentences that appear in both a and b
    # return list of sentences that appear in both a and b
    return list(set(sentenceA).intersection(sentenceB))

# extract substrings from strings
    # s[i:j] returns the substring of s from index i to (but not including) index j
# write a helper function that can take a string and get you all the substrings of a particular length


def substring(str, n):
    substrings = []

    for i in range(len(str) - n + 1):
        substrings.append(str[i:i + n])

    return substrings


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    # take in string inputs a, b and substring length int n
    # split each string into all possible substrings of length n characters
    # extract substrings from strings
    # s[i:j] returns the substring of s from index i to (but not including) index j
    # write a helper function that can take a string and get you all the substrings of a particular length
    substringA = set(substring(a, n))
    substringB = set(substring(b, n))

    # calculate the list of all substrings that appear in both a and b
    # return list of substrings that appear in both a and b
    return list(set(substringA).intersection(substringB))