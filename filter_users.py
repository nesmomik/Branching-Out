import json

FILENAME = "users.json"

def filter_users_by_name(name):
    """prints all data of users that match the given name in the json data of file FILENAME"""
    with open(FILENAME, "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """prints all data of users that match the given age in the json data of file FILENAME"""
    with open(FILENAME, "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == int(age)]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """prints all data of users that match the given email address in the json data of file FILENAME"""
    with open(FILENAME, "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)

def main(): 
    """Allows to filter json formatted data in file with name FILENAME by name, age or email-address"""
    filter_option = (
        input("What would you like to filter by? ('name', 'age', 'email'): ").strip().lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()