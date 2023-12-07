# Mobile numbers of Bangladesh

import re

def validate_bangladesh_mobile_number(number):
    pattern = r'^01[3-9]\d{8}$'   #Typical format for a mobile phone number is 01XXX NNNNNN, e.g. 01054 694200
    result = re.search(pattern, number)

    if result is not None:
        return True
    else:
        return False

print(validate_bangladesh_mobile_number('01712345678'))
print(validate_bangladesh_mobile_number('5856-541-166'))
print(validate_bangladesh_mobile_number('01799363999'))

