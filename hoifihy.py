import math

"""
How Old Is Fido In Human Years
"""

def new_formula(dog_age):
    return 16 * math.log(dog_age) + 31
    
    
def old_formula(dog_age):
    return 7 * dog_age
    
    
if __name__ == '__main__':
    age = input('how old is Fido? ')
    dog_age = float(age)
    print('Fido is {0} in human years according to the new formula.'.format(new_formula(dog_age)))
    print('Fido is {0} in human years according to the old formula.'.format(old_formula(dog_age)))
    print('Long live Fido!')