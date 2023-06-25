from pprint import pprint

from input.input import get_input
from model.list_person import ListPerson
from model.person import Person

# Reading .json file
json_input = get_input()

list_person = ListPerson(json_input)
list_person.validate()

print('List received:')
pprint(list_person.to_primitive(role='profile_info'))


# Transforming json in a list Person object and validating content
list_person = ListPerson(json_input)
list_person.validate()


# Printing list of a specific Person role
print('List received:')
pprint(list_person.to_primitive(role='profile_info'))
pprint(list_person.to_primitive(role='public_person'))

# Listing all friend and fruit information of all Person in list
for person in list_person.person:
    print('\n')
    [print(person.name + ' is friends with ' + friend.name) for friend in person.friends]
    print(person.name.split()[0] + ' favorite fruit is ' + person.favorite_fruit)
    print(person.external_id)

# Generating a mock with Person values
person_mock = Person.get_mock_object().to_primitive()
pprint(person_mock)
