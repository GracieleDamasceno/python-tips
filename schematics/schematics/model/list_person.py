from schematics import Model
from schematics.transforms import blacklist
from schematics.types import ModelType, ListType

from model.person import Person


class ListPerson(Model):
    person = ListType(ModelType(Person))

    class Options:
        roles = {'public_person': blacklist()}
