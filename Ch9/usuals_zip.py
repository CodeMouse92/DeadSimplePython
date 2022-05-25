regulars = ['William', 'Devin', 'Kyle', 'Simon', 'Newman']
usuals = ['french press', 'double-shot espresso', 'mocha cappuccino',
          'chai latte', 'tea', 'drip']

usual_orders = dict(zip(regulars, usuals))

print(usual_orders['Devin'])  # prints 'double-shot espresso'
