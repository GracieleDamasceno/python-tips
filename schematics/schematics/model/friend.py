from schematics import Model
from schematics.transforms import blacklist
from schematics.types import IntType, StringType


class Friend(Model):
    id = IntType()
    name = StringType()

    class Options:
        roles = {'public_person': blacklist()}
