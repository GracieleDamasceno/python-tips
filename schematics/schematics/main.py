from input.input import get_input
from model.list_person import ListPerson

json_input = get_input()

list_person = ListPerson(json_input)
list_person.validate()
print(list_person.to_primitive(role='public_person'))

