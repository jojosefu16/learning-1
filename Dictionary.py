#Dictionary
import json
import uuid
import unicodedata
from Validators import get_valid_name, get_valid_country, get_valid_height, get_valid_age, normalize_text

def main_menu():
   while True:
        print("\n---Main Menu--")
        print("1. Create user")
        print("2. Show all users")
        print("3. Edit user")
        print("4. Delete user")
        print("5. Exit")

        choice=input("Choose an option: ").strip()
        if choice =="1":
           create_user_profile()
        elif choice=="2":
            show_users()
        elif choice=="3":
            edit_user()
        elif choice=="5":
            break
        elif choice=="4":
           delete_user()
        else:
            print("Invalid option. Try again.")



def create_user_profile():
    print("Let's create your user profile.\n")

    name=get_valid_name("Enter your name: ")
    age=get_valid_age("Enter your age: ")
    height=get_valid_height("Enter your height (format 1,75): ")
    country=get_valid_country("Enter the country you live in: ")

    user={
    "id": str(uuid.uuid4()),
    "name": name,
    "age": age,
    "height": height,
    "country": country,
    }

    try:
        with open("G:/Python prácticas/user_profile.json", "r", encoding="utf-8") as file:
            users= json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users= []
    
    users.append(user)

    try:
        with open("G:/Python prácticas/user_profile.json", "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")
        return
    print ("\n Your profile has been created successfully.\n")
    for key, value in user.items():
        print(f"{key.capitalize()}: {value}")



def show_users():
    try:
        with open("G:/Python prácticas/user_profile.json", "r", encoding="utf-8") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("\n No user data found. Please create a profile first.")
        return
    except json.JSONDecodeError:
        print("\n The data file is corrupted or empty.")
        return
    
    if not users:
        print("\n No users found.")
        return

    while True:
        print("\n ---USERS LIST---")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user['name']}")
        
        print("\nOptions:")
        print("1. View details of a specific user")
        print("2. Return to main menu")
        option= input("Choose an option: ").strip()

        if option=="1":
            name=input("\nEnter the user's name to search: ").strip()
            normalized_name=normalize_text(name)
            matched_users=[user for user in users if normalize_text(user["name"])==normalized_name]
            if not matched_users:
                print(f"\nNo user found with the name '{name}'")
                continue
            
            if len(matched_users) >= 1:
                print(f"\n ---Users found with the name '{name}'---")
                for i, user in enumerate(matched_users, start=1):
                    print(f"{i}. {user['name']}")

                select_user = input("\nSelect the number of the user you want to see or type 'exit' to leave: ").strip()
                if select_user.lower() == 'exit':
                    print("Returning to search.")
                    continue

                try:
                    select_user = int(select_user)
                    if 1 <= select_user <= len(matched_users):
                        user = matched_users[select_user - 1]
                        print("\n--- USER DETAILS ---")
                        for key, value in user.items():
                            print(f"{key.capitalize()}: {value}")
                    else:
                        print("Invalid number. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

                    for key, value in user.items():
                        print(f"\n{key.capitalize()}: {value}")
            else:
                matched_users[0]
                for key, value in user.items():
                    print(f"{key.capitalize()}: {value}")
                    return  
                      
        elif option=="2":
            return
        else: print("Invalid option. Try again.")



def edit_user():
    try:
        with open("G:/Python prácticas/user_profile.json", "r", encoding="utf-8") as file:
            users=json.load(file)
    except FileNotFoundError:
        print ("\n No user data found.")
        return
    except json.JSONDecodeError:
        print("\n The data file is corrupted or empty.")
        return
    
    if not users:
        print ("\n No users found to edit.")
        return
    
    print("\n--- EDIT USER ---")
    for i, user in enumerate(users,start=1):
        print(f"{i}. {user['name']}")
    
    while True:
        name = input("\nEnter the name of the user to edit (or type 'exit' to cancel): ").strip().title()
        
        if name.lower() == 'exit':
            print("Returning to main menu...")
            return

        user_found = None
        for user in users:
            if user["name"].lower() == name.lower():
                user_found = user
                break

        if user_found:
            print(f"\n Editing user: {user_found['name']}")
            while True:
                print("\n--- Edit Menu ---")
                print("1. Edit name")
                print("2. Edit age")
                print("3. Edit height")
                print("4. Edit country")
                print("5. Show current data")
                print("6. Return to main menu")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    user_found["name"] = get_valid_name("Enter new name: ")
                    print("Name updated successfully!")

                elif choice == "2":
                    user_found["age"] = get_valid_age("Enter new age: ")
                    print("Age updated successfully!")

                elif choice == "3":
                    user_found["height"] = get_valid_height("Enter new height (format 1,75): ")
                    print("Height updated successfully!")

                elif choice == "4":
                    user_found["country"] = get_valid_country("Enter new country: ")
                    print("Country updated successfully!")

                elif choice == "5":
                    print("\n--- Current User Data ---")
                    for key, value in user_found.items():
                        print(f"{key.capitalize()}: {value}")

                elif choice == "6":
                    with open("G:/Python prácticas/user_profile.json", "w", encoding="utf-8") as file:
                        json.dump(users, file, ensure_ascii=False, indent=4)
                    print("\nChanges saved successfully. Returning to main menu...")
                    return
                else:
                    print("Invalid option. Try again.")
        else:
            print(f"\nNo user found with the name '{name}'. Please try again.")

        

def delete_user():
    try:
        with open("G:/Python prácticas/user_profile.json", "r", encoding="utf-8") as file:
            users=json.load(file)
    except FileNotFoundError:
        print ("\nNo user data found")
        return
    except json.JSONDecodeError:
        print("\nThe data file is corrupted or empty.")
        return
    
    if not users:
        print ("\nNo user found to delete")
        return

    print("---DELETE USER---")
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user['name']}")
        
    name= input("\nEnter the name of the user to delete (or type 'exit' to cancel): ").strip().title()

    if name.lower()=='exit':
        print("Returning to the main menu")
        return
    
    matched_users=[user for user in users if user["name"]==name]

    if not matched_users:
        print("\nNo user found with the name '{name}'.")
        return
    
    if len(matched_users)>1:
        print("\nMultiple users named '{name}' found:")
        for i, users in enumerate(matched_users, start=1):
            print(f"\nUser {i}:")
            for key, value in user.items():
                print(f"{key.capitalize()}: {value}")
            try:
                index=int(input("\nEnter the number of the user to delete: ").strip()) - 1
                if index < 0 or index >= len(matched_users):
                    print("Invalid selection. Operation cancelled.")
                    return
                user_to_delete=matched_users[index]
            except ValueError:
                print("Invalid input. Operation Cancelled.")
                return
    else:
        user_to_delete=matched_users[0]

    confirm=input(f"\n Are you sure you want to delete '{user_to_delete['name']}? (y/n): ").strip().lower()
    if confirm !='y':
        print("Deletion cancelled.")
        return
    
    users.remove(user_to_delete)

    with open("G:/Python prácticas/user_profile.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

    print(f"\nUser '{user_to_delete['name']}' deleted successfully.")

                            

if __name__=="__main__":
    main_menu()
