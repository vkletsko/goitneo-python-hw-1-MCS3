def validate_args(cmd: str, args: list):
    is_valid = True
    err_msg = ""

    if (cmd == "add" or cmd == "change") and len(args) == 2:
        return (args, is_valid, err_msg)
    elif cmd == "phone" and len(args) == 1:
        return (args, is_valid, err_msg)
    else:
        is_valid = False
        err_msg = f"Please enter a correct values for command '{cmd}', allowed is 1 or 2 arguments"
        return ([], is_valid, err_msg)


def parse_input(user_input: str) -> (str, list):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return "invalid_command", []


def add_contact(cmd: str, contact_data: list, contacts: dict) -> str:
    (args, is_valid, err_msg) = validate_args(cmd, contact_data)
    if is_valid:
        contacts[args[0]] = args[1]
        return "Contact added"
    else:
        return err_msg


def change_contact(cmd: str, contact_data: list, contacts: dict) -> str:
    (args, is_valid, err_msg) = validate_args(cmd, contact_data)
    if is_valid:
        contacts[args[0]] = args[1]
        return "Contact updated"
    else:
        return err_msg


def show_phone(cmd: str, data: list, contacts: dict) -> str:
    (args, is_valid, err_msg) = validate_args(cmd, data)
    if is_valid:
        search_name = args[0]
        for name, phone in contacts.items():
            if search_name == name:
                return f"{search_name.title()} {phone}"
            else:
                return f"Contact {search_name.title()} doesn't exist"
    else:
        return err_msg


def show_all(contacts: dict) -> str:
    phonebook = ""
    for name, phone in contacts.items():
        phonebook += "Contact: {} {}\n".format(name.title(), phone)

    return phonebook


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        cmd, *args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(cmd, args, contacts))
        elif cmd == "change":
            print(change_contact(cmd, args, contacts))
        elif cmd == "phone":
            print(show_phone(cmd, args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
