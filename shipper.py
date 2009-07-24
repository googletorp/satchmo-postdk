"""
Post Danmark shipping module
v 0.1

By Jakob Torp Svendsen - googletorp

- This module is still in development
"""

try:
    from decimal import Decimal
except:
    from django.utils._decimal import Decimal

from django.utils.translation import ugettext as _

from livesettings import config_get_group
from shipping.modules.base import BaseShipper
from shipping.modules.postdk.helper import pack_parcels

# Fees as per January 1st, 2009.
POSTDK_FEES = {
    'max_5': Decimal("75.00"),
    'max_10': Decimal("100.00"),
    'max_20': Decimal("160.00"),
    'volume': Decimal("76.00"),
    'fragile': Decimal("76.00"),
}



class Shipper(BaseShipper):

    id = "PostDK"
        
    def __str__(self):
        """
        This is mainly helpful for debugging purposes.
        """
        return "Post Danmark"
        
    def description(self):
        """
        A basic description that will be displayed to the user, when
        selecting their shipping options.
        """
        return _("Post Danmark shipping")

    def cost(self):
        """
        Complex calculations can be done here, as long as the return value is
        a decimal figure.
        """
        cartset = self.cart.cartitem_set.all()
        settings = config_get_group('shipping.modules.postdk')
        parcel_list = pack_parcels(cartset, settings)
        result = Decimal("0.00")
        for parcel in parcel_list:
            if parcel.weight <= 5:
                result += POSTDK_FEES['max_5']
            elif parcel.weight <= 10:
                result += POSTDK_FEES['max_10']
            elif parcel.weight <= 20:
                result += POSTDK_FEES['max_20']
            else:
                # TODO, raise error as we currently don't accept parcels over
                # 20 kg, or parcel has no weight.
                pass
            if parcel.volume_fee():
                result += POSTDK_FEES['volume']
            result *= settings['POSTDK_CURRENCY'].value
        return result

    def method(self):
        """
        Describes the actual delivery service (Mail, FedEx, DHL, UPS, etc).
        """
        return _("Post Danmark")

    def expectedDelivery(self):
        """
        Can be a plain string or complex calcuation returning an actual date.
        """
        return _("3 - 4 business days")

    def valid(self, order=None):
        """
        Can do complex validation about whether or not this option is valid.
        For example, may check to see if the recipient is in an allowed
        country or location.
        """
        return True

