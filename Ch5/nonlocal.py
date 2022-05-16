spam = True


def order():
    eggs = 12

    def cook():
        nonlocal eggs

        if spam:
            print("Spam!")

        if eggs:
            eggs -= 1
            print("...and eggs.")

    cook()


order()
