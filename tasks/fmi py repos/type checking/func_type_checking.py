#Testing and improving skills in the field decorators in py

IOS_MESSAGE = {'in': 'input arguments', 'out': 'output values'}

def try_io(io, valid_types, *args):
    for arg in args:
        if not isinstance(arg, valid_types):
            print(f'Invalid {IOS_MESSAGE[io]}, expected {', '.join(str(x) for x in valid_types)}!')
            return

def type_check(io):
    def types(*valid_types):
        def wrapper(func):
            def power_wrapper(num, pwr):
                if io == 'in':
                    try_io(io, valid_types, num, pwr)
                result = func(num, pwr)
                if io == 'out':
                    try_io(io, valid_types, result)
                return result
            return power_wrapper
        return wrapper
    return types

@type_check('in')(int, float)
@type_check("out")(int, float)
def power(num, pwr):
    return num ** pwr

@type_check("in")(str)
def concatenate(*strings, separator=' beep boop '):
    return separator.join(strings)

#print(power(6j, 2))
#print(concatenate(5, '6'))
