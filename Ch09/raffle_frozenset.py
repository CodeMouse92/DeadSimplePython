raffle = {'Kyle', 'Denis', 'Jason'}
prev_winners = frozenset({'Denis', 'Simon'})
raffle -= prev_winners  # remove previous winners
print(raffle)           # prints {'Jason', 'Kyle'}
winner = raffle.pop()
print(winner)           # prints arbitrary item of set, e.g. 'Kyle'
