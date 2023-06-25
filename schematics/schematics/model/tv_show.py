from schematics import Model
from schematics.types import StringType, IntType


class TVShow(Model):
    name = StringType()
    year = IntType()
    network = StringType()

    @classmethod
    def _claim_polymorphic(cls, data):
        return data.get('network')
