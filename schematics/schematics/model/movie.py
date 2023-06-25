from schematics import Model
from schematics.types import StringType, IntType


class Movie(Model):
    name = StringType()
    year = IntType()
