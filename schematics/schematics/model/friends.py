from schematics import Model
from schematics.types import IntType, StringType


class Friends(Model):
    id = IntType()
    name = StringType()
