from decorators import input_error

@input_error
def change_contact(args, contacts): 
    name, phone = args
    contacts[name] = phone
    return "Contact updated."
    
    