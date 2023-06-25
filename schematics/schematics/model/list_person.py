from schematics import Model
from schematics.transforms import wholelist
from schematics.types import ModelType, ListType

from model.person import Person


class ListPerson(Model):
    person = ListType(ModelType(Person))

    class Options:
        roles = {'public_person': wholelist(), 'profile_info': wholelist()}
