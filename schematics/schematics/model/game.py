from schematics import Model
from schematics.types import StringType, IntType


class Game(Model):
    name = StringType()
    year = IntType()
    console = StringType()

    @classmethod
    def _claim_polymorphic(cls, data):
        return data.get('console')
