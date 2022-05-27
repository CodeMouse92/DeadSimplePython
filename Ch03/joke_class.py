class Joke:

    def __init__(self, joke_type):
        if joke_type == "funny":
            self.question = "How can you tell an elephant is in your fridge?"
            self.answer = "There are footprints in the butter!"
        elif joke_type == "lethal":
            self.question = "Wenn ist das Nunstück git und Slotermeyer?"
            self.answer = "Ja! Beiherhund das Oder die Flipperwaldt gersput!"
        else:
            self.question = "Why did the chicken cross the road?"
            self.answer = "To get to the other side!"

    def tell(self):
        print(self.question)
        print(self.answer)


lethal_joke = Joke("lethal")
lethal_joke.tell()
