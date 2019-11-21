new_order = Orders(person=new_person1)
session.add(new_order)
session.commit()

all_people = session.query(Address).join(Person, Address.person_id).all()

for row in all_people:
    pprint(row.name)
    pprint(row.post_code)

objects = [
    Person(name="u1"),
    Person(name="u2"),
    Person(name="u3")
]