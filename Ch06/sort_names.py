people = [
    ("Jason", "McDonald"),
    ("Denis", "Pobedrya"),
    ("Daniel", "Foerster"),
    ("Jaime", "López"),
    ("James", "Beecham")
]

by_last_name = sorted(people, key=lambda x: x[1])
print(by_last_name)
