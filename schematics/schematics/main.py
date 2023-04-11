from pprint import pprint

from input.input import get_input
from model.list_person import ListPerson

json_input = get_input()

list_person = ListPerson(json_input)
list_person.validate()

print('List received:')
pprint(list_person.to_primitive(role='profile_info'))

for person in list_person.person:
    print('\n')
    [print(person.name + ' is friends with ' + friend.name) for friend in person.friends]
    print(person.name.split()[0] + ' favorite fruit is ' + person.favorite_fruit)
