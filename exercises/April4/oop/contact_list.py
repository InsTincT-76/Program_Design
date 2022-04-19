from person import Person



people = (
    Person("Sandra", "white", "803-454-6677"),
    Person("Bobby", "white", "803-454-6214"),
    Person("Daniel", "white", "803-454-6457"),
    Person("Kimmie", "white", "803-454-6077"),
)

for person in people:
    person.display()