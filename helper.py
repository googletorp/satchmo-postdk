"""
This file is used to hold some helper functions used to calculate the
cost of sending the the merchandise bought by the users. The prices
used will be in Danish Crowens (DKK), the end result however can be
overridden to any currency through the admin interface.
"""

from exceptions import ImportError, KeyError

try:
    from decimal import Decimal
except ImportError:
    from django.utils._decimal import Decimal


class Parcel(object):
    """
    Parcel class, a constructor for parcels that should be sent.
    
    Will hold parcel attributes - weight and size along with methods to
    calculate special services, like volume fee. The units for parcels
    should always be cm for lengths and kg for weight.
    """
    def __init__(self, *args, **kwargs):
        super(Parcel, self).__init__(*args, **kwargs)
        try:
            self.height = kwargs['height']
            self.length = kwargs['length']
            self.width = kwargs['width']
            self.weigth = kwargs['weight']
        except KeyError:
            raise KeyError, "Parcel object requires to be initialized with \
                                kwargs: height, length, width and weight."
        self.products = []

    def volume_fee(self):
        """
        Method to calculate if volume fee should be added to parcel.
        """
        count = 0
        for length in (self.height * self.width * self.length):
            if length > 150:
                return True
            if length > 50:
                count += 1
            if count > 1:
                return True
        return False


def pack_parcels(cartset, settings):
    """
    Function used to calculate how to pack parcels.

    This function will fist go through all the products in the cart
    QuerySet and set default values on size and weight where needed.
    Then it will calculate how to best pack the products in parcels,
    given the settings set.

    cartset = Queryset of the cart
    settings: the postdk livesettings
    """

    # set all the size values if one is missing:
    for ci in cartset:
        product = ci.product
        default = False
        if not (product.width and product.height and product.lenght):
            default = True
        if not (product.width_units.lower() and products.length_units.lower() \
                and product.height_units.lower()) != 'cm':
            default = True
        if default:
            ci.product.width = settings['POSTDK_DEFAULT_WIDTH']
            # ci.product.width_units = settings['POSTDK_DEFAULT_SIZE_UNITS']
            ci.product.length = settings['POSTDK_DEFAULT_LENGTH']
            # ci.product.length_units = settings['POSTDK_DEFAULT_SIZE_UNITS']
            ci.product.height = settings['POSTDK_DEFAULT_HEIGHT']
            # ci.product.height_units = settings['POSTDK_DEFAULT_SIZE_UNITS']
        if not product.weight or product.weight_units.lower() != 'kg':
            ci.product.weight = settings['POSTDK_DEFAULT_HEIGHT']
            # ci.product.weight_units = settings['POSTDK_DEFAULT_SIZE_UNITS']

    # easy, one parcel per cart item
    if settings['POSTDK_PACKING'] == 'CART'
        result = []
        for ci in cartset:
            if ci.product.is_shippable:
                for quantity in range(ci.quantity):
                    parcel = Parcel(
                        height=ci.product.height,
                        length=ci.product.length
                        width=ci.product.width
                        weight=ci.product.width
                    )
                    parcel.products.append(ci.product)
                    result.append(parcel)

    return result

