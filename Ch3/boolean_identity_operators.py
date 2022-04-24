spam = True
eggs = False
potatoes = None

if spam is True:  # Evaluates to True
    print("We have spam.")

if spam is not False:  # Evaluates to True
    print("I DON'T LIKE SPAM!")

if spam:  # Implicitly evaluates to True (preferred)
    print("Spam, spam, spam, spam...")


if eggs is False:  # Evaluates to True
    print("We're all out of eggs.")

if eggs is not True:  # Evaluates to True
    print("No eggs, but we have spam, spam, spam, spam...")

if not eggs:  # Implicitly evaluates to True (preferred)
    print("Would you like spam instead?")


if potatoes is not None:  # Evaluates to False (preferred)
    print("Yum")          # We never reach this...potatoes is None!

if potatoes is None:      # Evaluates to True (preferred)
    print("Yes, we have no potatoes.")

if eggs is spam:          # Evaluates to False (CAUTION!!!)
    print("This won't work.")
