from input.input import get_input
from model.list_person import ListPerson

input = get_input()

person = ListPerson(input)
person.validate()
print(person.to_primitive())
