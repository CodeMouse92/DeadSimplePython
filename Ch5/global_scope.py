high_score = 10


def score():
    global high_score
    new_score = 465             # SCORING LOGIC HERE
    if new_score > high_score:
        print("New high score")
        high_score = new_score


score()
print(high_score)  # prints 465
