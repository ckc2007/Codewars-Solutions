# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

# My solutions

def remove_exclamation_marks(s):
    return s.replace('!', '')


# def remove_exclamation_marks(s):
#    """ return s.replace('!', '') """
#    new_s = ''
#    for i in s:
#        if i != '!':
#            new_s += i
#    return new_s
# 
# note there is no multi line break out in python for notes

def remove_exclamation_marks(s):
    """ return s.replace('!', '') """
    new_s = ''
    for i in s:
        if i != '!':
            new_s += i
    return new_s

# another solution to study format

def remove_exclamation_marks(s):
    return ''.join([x for x in s if x != '!'])


# last one to study format