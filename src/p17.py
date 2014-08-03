table=("", "one", "two", 'three','four','five','six','seven','eight','nine')
def number_to_string(a):
    ''' 1-> one, 2->two,...,9->nine
    '''
    return table[a]

for a in range(0,10):
    print number_to_string(a)
