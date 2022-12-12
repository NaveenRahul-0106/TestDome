from collections import namedtuple
from functools import reduce
from itertools import chain
from operator import add

def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """ 
    cls = namedtuple("Patient", reduce(add, (arg._fields for arg in records)))
    #cls = namedtuple("_".join(arg.__class__.__name__ for arg in records), reduce(add, (arg._fields for arg in records)))

    return cls(*chain(*records))
    # return None
    
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                   
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
  
print(merge(personal_details, complexion))