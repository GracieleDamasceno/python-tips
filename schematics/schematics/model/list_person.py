from schematics import Model
from schematics.types import ModelType, ListType

from model.person import Person


class ListPerson(Model):
    person = ListType(ModelType(Person))
