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
        
