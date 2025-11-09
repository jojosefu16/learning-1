print("Hola. Entorno funcionando.")

#Numbers
age=22
height=1,76

#Text(String)
name="José"

#Boolean (True or False)
is_stuyding= True


def build_persona():
 food= input("\nNow, what is your favorite food?").strip().capitalize().lower() 
 hobby= input ("\nAnd your favorite activity?").strip().capitalize().lower()
 print("Name: ", name, "\nAge: ", age, "\nHeight: ", "\nStudying: ", is_stuyding,"\nHis favorite food is",food,"and his favorite activity is",hobby)

def ask_yes_no(question):

    answer= input(question + " (Yes/No) ").strip().lower()
    while answer not in ["yes", "no"]:
        answer=input ("I told you only answer 'yes' or 'no':").strip().lower()
    return answer

def cat_question():
 likes_cats=ask_yes_no("\nReally important question. Do you... like cats?")
 if likes_cats=="yes":
    print ("I like you!")
 else: 
    print("That's okay. Not everyone has good taste.") 

def top_songs():
 print("\nNow, let's build your top 5 favorite songs.")
 songs= []
 for i in range(5):
    song= input (f"Enter song #{i+1}: ").strip().title()
    songs.append(song)
 print("\nThen your top 5 songs are:")
 for i, song in enumerate(songs, start=1):
     print(f"{i}. {song}")

 check_song=ask_yes_no("\nDo you want to check a song in your playlist?") 
 if check_song=="yes":
    check_music= input("\nWhich one yo you want to check?").strip().title()
    if check_music in songs:
        print("The song is in your top.")
    else:
        print("No. It is not in your top.")
 else:
    print("OK")

def countries_list():
 print ("Now it is time for you to name 3 countries you'd like to live in.")
 countries= []

 for i in range(3):
    country=input(f"Enter your {i+1} country:").title()
    countries.append(country)

 while True:
    print("\nThen your list is:")
    for i, country in enumerate(countries, start=1):
        print(f"{i}. {country}")
    countrie_check=ask_yes_no("Do you want to change any of them?")
    if countrie_check=="yes":
        try:
            while True:
                i=int(input("Which number do you want to change?")) - 1
                if 0<=i<len(countries):
                    countries[i]=input("Name your new country:").title()
                    break
                else:
                 print("A number between 1 and 3, please")
        except ValueError:
           print("Enter a valid number.")
    else:
      print("\n I'd like Japan btw....")
      break

def menu():
    while True:
        print("\n---Main Menu--")
        print("1. Persona questions")
        print("2. Extremely important cat question")
        print("3. Top songs")
        print("4. Countries")
        print("5. Quit")

        choice=input("Choose an option: ").strip()
        if choice =="1":
            build_persona()
        elif choice=="2":
            cat_question()
        elif choice=="3":
            top_songs()
        elif choice=="5":
            break
        elif choice=="4":
           countries_list()
        else:
            print("Invalid option. Try again.")

menu()
        