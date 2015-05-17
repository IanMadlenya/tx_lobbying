"""
Take address objects and clean each individual fields.

Other examples that all take full addresses:

* http://pyparsing.wikispaces.com/file/view/streetAddressParser.py
* https://github.com/pnpnpn/street-address
* https://github.com/SwoopSearch/pyaddress
"""
from __future__ import unicode_literals

import logging
import re

logger = logging.getLogger(__name__)


# A zip+4 or zip+4 with a missing dash
zip_4 = re.compile(r'^\d{5}\-?(\d{4})?$')


def clean_zipcode(input):
    if zip_4.match(input):
        # malformed zip+4
        logger.debug('cleaned zip code: {}'.format(input))
        return input[0:5]
    return input


def clean_street(address1, address2=''):
    """
    Clean street address.

    # address
    # [predir_apprev] N S E W
    # street_name
    # street_type_abbrev
    # postdir_abbrev
    # internal

    http://postgis.net/docs/Normalize_Address.html
    """
    # Strip "care of" lines
    if re.match(r'c/o ', address1, re.IGNORECASE):
        return address2
    return '{} {}'.format(address1, address2).strip()
