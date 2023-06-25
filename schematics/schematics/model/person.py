import datetime
from schematics import Model
from schematics.transforms import blacklist, whitelist
from schematics.types import ModelType, StringType, IntType, UUIDType, BooleanType, URLType, EmailType, DateTimeType, \
    GeoPointType, ListType, serializable, PolyModelType

from model.friend import Friend
from model.game import Game
from model.movie import Movie
from model.schematics_types.currency_type import CurrencyType
from model.tv_show import TVShow
from model.validators import is_uppercase, is_email_valid, is_over_18


class Person(Model):
    id = StringType(deserialize_from='_id')  # with deserialize_from, we inform schematics of the field's alias received
    index = IntType()
    guid = UUIDType()
    is_active = BooleanType(deserialize_from='isActive')
    balance = CurrencyType()
    picture = URLType()
    age = IntType(validators=[is_over_18])  # using a custom method to validate value received. We invoke the validation
    # method inside brackets, without parentheses.
    eye_color = StringType(deserialize_from='eyeColor')
    name = StringType(required=True)
    gender = StringType()
    company = StringType(validators=[is_uppercase])
    email = EmailType(validators=[is_email_valid], required=True)
    phone = StringType(required=True)
    address = StringType()
    about = StringType()
    registered = DateTimeType()
    coordinates = GeoPointType()
    tags = ListType(StringType)
    friends = ListType(ModelType(Friend))  # creating a list of compound type Friend
    greeting = StringType()
    favorite_fruit = StringType(deserialize_from='favoriteFruit')
    favorite_media = PolyModelType([
        Movie,
        TVShow,
        Game
    ], deserialize_from='favoriteMedia')
    created_at = DateTimeType(default=datetime.datetime.now)  # setting default value to field

    # creating external_id field, which is composed of index and id
    @serializable
    def external_id(self):
        return u'%s-%s' % (self.index, self.id)

    # Creating a role to be implemented by schematics when outputting data to primitive. The role 'public_person'
    # omits sensitive data, such as id, index and balance.
    # Those roles should be declared in inner and outer classes of this context as well, which declaration of items
    # could be empty (see: Friend class).
    class Options:
        serialize_when_none = False
        roles = {
            'public_person': blacklist('id', 'index', 'guid', 'is_active', 'balance'),
            'profile_info': whitelist('name', 'greeting', 'gender', 'picture', 'about', 'age')
        }
