def hwl(word):
    length = len(word)
    if word[0] == word[length-1]:
        if length > 2:
            return hwl(word[1:length-1])
        else:
            print ('是回文联!')
    else:
        print('不是回文联!')
hwl('ABCCBA')
