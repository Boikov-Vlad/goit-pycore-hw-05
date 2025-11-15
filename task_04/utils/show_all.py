from decorators import input_error

@input_error
def show_all(args, contacts): 
    all_contacts = "Contacts:\n"
    
    for name, phone in contacts.items():
        all_contacts += f"{name} : {phone}\n"
        
    return all_contacts
    