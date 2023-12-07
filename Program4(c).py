# write a python function to validate the regular expression for the telephone numbers of usa


import re

def validate_usa_telephone_number(number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    
    result = re.search(pattern, number)
   if result is not None:
        return True
    else:
        return False

print(validate_usa_telephone_number('866-635-8412'))
print(validate_usa_telephone_number('5856-541-166'))
print(validate_usa_telephone_number('891 181 6415'))
