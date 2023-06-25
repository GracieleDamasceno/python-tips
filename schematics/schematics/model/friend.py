from schematics import Model
from schematics.transforms import wholelist
from schematics.types import IntType, StringType


class Friend(Model):
    id = IntType()
    name = StringType()

    class Options:
        roles = {'public_person': wholelist(), 'profile_info': wholelist()}
