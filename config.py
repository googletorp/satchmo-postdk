from django.utils.translation import ugettext_lazy as _
from livesettings import *

SHIP_MODULES = config_get('SHIPPING', 'MODULES')
SHIP_MODULES.add_choice(('shipping.modules.postdk', 'Post Danmark'))

SHIPPING_GROUP = ConfigurationGroup('shipping.modules.postdk',
  _('Post Danmark Shipping Settings'),
  requires = SHIP_MODULES,
  requiresvalue='shipping.modules.postdk',
  ordering = 101
)

config_register_list(

    DecimalValue(SHIPPING_GROUP,
        'POSTDK_HANDLING',
        description=_("Handling fee"),
        help_text=_("The cost of packaging and taking order to post office \
                    (in DKK)"),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="50.00",
        ordering=1),

    StringValue(SHIPPING_GROUP,
        'POSTDK_DAYS',
        description=_("Post Danmark Delivery Days."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="3 - 4 business days",
        ordering=2),

    DecimalValue(SHIPPING_GROUP,
        'POSTDK_CURRENCY',
        description=_("Currency calculation"),
        help_text=_("If you're using another currency than Danish Crowns \
                    used by Post Danmark, enter the amount of currency \
                    you would get per 1 DKK."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="1.00",
        ordering=3),

    StringValue(SHIPPING_GROUP,
        'POSTDK_PACKING',
        description=_("Packaging"),
        help_text=_("Choose how you would like to pack your pakages. Packing \
                    will be optimised to avoid high weight and volume fees \
                    when possible."),
        choices=(
                    (("SINGLE", "All products in a single parcel")),
                    #(("PRODUCT", "One parcel per product type")),
                    (("CART", "One parcel per cart item")),
        ),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default='PRODUCT',
        ordering=4),

    DecimalValue(SHIPPING_GROUP,
        'POSTDK_PERCENT_VOLUME',
        description=_("Percent volume usage"),
        help_text=_("As Post Danmark has a volume fee, if a package is \
                    larger than 50x50x100 cm, set how many percent of such \
                    a parcel would be used in averedge. Used to calculate \
                    when a new parcel is needed if many items are ordered."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="80.00",
        ordering=5),

    StringValue(SHIPPING_GROUP,
        'POSTDK_DEFAULT_SIZE_UNITS',
        description=_("Default size units"),
        help_text=_("Choose the units for the default size of your parcel."),
        choices=(
                    (("cm", "cm - centimeters")),
        ),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="cm",
        ordering=6),

    DecimalValue(SHIPPING_GROUP,
        'POSTDK_DEFAULT_LENGTH',
        description=_("Default length of parcel"),
        help_text=_("This is used if you haven't entered a value for for \
                    the product's length."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="50.00",
        ordering=7),
        
    DecimalValue(SHIPPING_GROUP,
        'POSTDK_DEFAULT_WIDTH',
        description=_("Default width of parcel"),
        help_text=_("This is used if you haven't entered a value for for \
                    the product's width."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="25.00",
        ordering=9),

    DecimalValue(SHIPPING_GROUP,
        'POSTDK_DEFAULT_HEIGHT',
        description=_("Default height of parcel"),
        help_text=_("This is used if you haven't entered a value for for \
                    the product's height."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="25.00",
        ordering=8),

    StringValue(SHIPPING_GROUP,
        'POSTDK_DEFAULT_WEIGHT_UNITS',
        description=_("Default weight unit"),
        help_text=_("Choose the units for the default weigth of your \
                    parcel."),
        choices=(
                    (("kg", "kg - kilogram")),
        ),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="kg",
        ordering=10),

    DecimalValue(SHIPPING_GROUP,
        'POSTDK_DEFAULT_WEIGHT',
        description=_("Default weight of parcel"),
        help_text=_("This is used if you haven't entered a value for for \
                    the product's weight."),
        requires=SHIP_MODULES,
        requiresvalue='shipping.modules.postdk',
        default="5.00",
        ordering=11),
)
