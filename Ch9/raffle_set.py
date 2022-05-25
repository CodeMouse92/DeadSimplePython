raffle = {'James', 'Denis', 'Simon'}

raffle.add('Daniel')
raffle.add('Denis')
print(raffle)  # prints {'Daniel', 'Denis', 'Simon', 'James'}

raffle.discard('Simon')
print(raffle)  # prints {'Daniel', 'Denis', 'Simon'}

winner = raffle.pop()
print(winner)  # prints arbitrary item of set, e.g. 'Denis'
