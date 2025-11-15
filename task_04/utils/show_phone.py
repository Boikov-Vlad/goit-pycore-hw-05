from decorators import input_error

@input_error
def show_phone(args, contacts):
    name = args[0]    
    return contacts[name]