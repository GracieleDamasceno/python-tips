from schematics import Model
from schematics.transforms import blacklist
from schematics.types import ModelType, StringType, IntType, UUIDType, BooleanType, URLType, EmailType, DateTimeType, \
    GeoPointType, ListType

from model.friend import Friend
from model.schematics_types.currency_type import CurrencyType
from model.validators import is_uppercase, is_email_valid, is_over_18


class Person(Model):
    id = StringType(deserialize_from='_id')  # with deserialize_from, we inform schematics of the field's alias received
    index = IntType()
    guid = UUIDType()
    is_active = BooleanType(deserialize_from='isActive')
    balance = CurrencyType()
    picture = URLType()
    age = IntType(validators=[is_over_18])  # using a method to validate value received. We invoke the validation
    # method inside brackets, without parentheses.
    eye_color = StringType(deserialize_from='eyeColor')
    name = StringType()
    gender = StringType()
    company = StringType(validators=[is_uppercase])
    email = EmailType(validators=[is_email_valid])
    phone = StringType()
    address = StringType()
    about = StringType()
    registered = DateTimeType()
    coordinates = GeoPointType()
    tags = ListType(StringType)
    friends = ListType(ModelType(Friend))  # creating a list of compound type Friend
    greeting = StringType()
    favorite_fruit = StringType(deserialize_from='favoriteFruit')

    # Creating a role to be implemented by schematics when outputting data to primitive. This role is called
    # 'public_person' and omits sensitive data, such as id, index and balance. This role should be declared in inner
    # and outer classes of this context as well, which declaration of itens could be empty (see: Friend class).
    class Options:
        roles = {
            'public_person': blacklist('id', 'index', 'guid', 'is_active', 'balance')
        }
