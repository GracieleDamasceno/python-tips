from schematics import Model
from schematics.types import ModelType, StringType, IntType, UUIDType, BooleanType, URLType, EmailType, DateTimeType, \
    GeoPointType, ListType

from model.friends import Friends
from model.schematics_types.currency_type import CurrencyType


class Person(Model):
    id = StringType(deserialize_from='_id')
    index = IntType()
    guid = UUIDType()
    is_active = BooleanType(deserialize_from='isActive')
    balance = CurrencyType()
    picture = URLType()
    age = IntType()
    eye_color = StringType(deserialize_from='eyeColor')
    name = StringType()
    gender = StringType()
    company = StringType()
    email = EmailType()
    phone = StringType()
    about = StringType()
    registered = DateTimeType(formats='%Y-%m-%dT%H:%N:%S %Z')
    coordinates = GeoPointType()
    tags = ListType(StringType)
    friends = ListType(ModelType(Friends))
    greetings = StringType()
    favorite_fruit = StringType(deserialize_from='favoriteFruit')
