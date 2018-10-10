antonyms = {}   # {}=dict()
while 1:
    word = input("Please Enter a word :")
    # print(word)
    if word in antonyms:
        print("antonym of " + word + " is: " + (antonyms[word]))
    else:
        x = input("I don't know . if you know Press 'y' else Press 'n' :")
        if x == 'y':
            antonym = input("Please Enter antonym :")
            antonyms.update({word: antonym})
            antonyms.update({antonym: word})
