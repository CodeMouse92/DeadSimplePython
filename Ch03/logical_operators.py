spam = True
eggs = False

if spam and eggs:        # AND operator, evaluates to False
    print("I do not like green eggs and spam.")

if spam or eggs:         # OR operator, evaluates to True
    print("Here's your meal.")

if (not eggs) and spam:  # NOT (and AND) operators, evaluates to True
    print("But I DON'T LIKE SPAM!")
