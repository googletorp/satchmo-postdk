"""
Post Danmark shipping module
v 0.1

By Jakob Torp Svendsen - googletorp

- This module is still in development
"""

import pdb


# Note, make sure you use decimal math everywhere!
try:
    from decimal import Decimal
except:
    from django.utils._decimal import Decimal

from django.utils.translation import ugettext as _
from shipping.modules.base import BaseShipper

class Shipper(BaseShipper):

    flatRateFee = Decimal("15.00")
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
        test = self.cart.cartitem_set.all()
        test1 = test[0]
        pdb.set_trace()
        help_a = help[0]
        
        raise
        assert(self._calculated)
        return(self.flatRateFee)

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

