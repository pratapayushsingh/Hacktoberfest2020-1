def is_pallindrome(string):


    #backwords=string[::-1]

    #return backwords==string

    return string[::-1].casefold() == string.casefold()


def pallindrome_sentence(sentence):
    string=""
    for ch in sentence:
        if ch.isalnum():
            string+=ch
    print(string)
    return is_pallindrome(string)

word=input("enter the word here")
if pallindrome_sentence(word):
    print("{} is pallindrome".format(word))
else:
    print("{} is not pallindrome" .format(word))
