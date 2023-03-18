from schematics.types import FloatType


class CurrencyType(FloatType):
    def convert(self, value, context=None):
        if not isinstance(value, str):
            return value
        number = value.replace('$', '')
        return float(number.replace(',', ''))
