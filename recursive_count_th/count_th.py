'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if not word:
        return 0
        # go thru each element in word
        # if element == t
        # check if next element == h
    elif len(word) > 1 and word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:]) # if true count + 1
    else:
        return 0 + count_th(word[1:]) # call count_th()