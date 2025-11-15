from utils import parse_input, add_contact, change_contact, show_phone, show_all

def main():
    contacts = {}

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all
    }

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command in commands:
            handler = commands[command]
            print(handler(args, contacts))
        elif command == '':
            continue
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
