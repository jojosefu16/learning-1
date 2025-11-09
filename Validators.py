#Validators.py
import re
import unicodedata

def get_valid_name(prompt="Enter your name: "):
    pattern = re.compile(r"^[A-Za-zÀ-ÿ'’\-\. ]+$")
    while True:
        name = input(prompt).strip()
        name= ' '.join(name.split())
        name=name.title()
        name= name.strip(" .-'’")

        if not name or not re.search(r"[A-Za-zÀ-ÿ]", name):
            print ("Name cannot be empty.")
        elif not pattern.fullmatch(name):
            print ("Please enter a valid name (letters, spaces, hyphens, or apostrophes only).")
        elif len(re.sub(r"[^A-Za-zÀ-ÿ]", "", name))>30:
            print("Name cannot have moire than 30 letters.")
        else:
            return name



def get_valid_age (prompt="Enter your age: "):
    while True:
        age_input=input(prompt).strip()
        if age_input.isdigit():
            age=int(age_input)
            if not 0 < age < 120:
             print("Please enter a realistic age.")
            else:
             return age
        else:
            print("Please enter a valid number.")



def get_valid_height (prompt="Enter your height (format 1,75)"):
    while True:
        height_input=input(prompt).strip().replace(",", ".")
        if height_input.count(".")>1:
            print("Please enter the height in format like 1.75 (only one decimal point)")
            continue
        try:
            height= float(height_input)
            if not 0.5 <= height <=2.5:
                print("Please enter a realistic height between 0.5 and 2.5 meters.")
                continue
            height= round(height, 2)
            return height
        except ValueError:
            print("Please enter a valid height in format 1,75")



def get_valid_country (prompt="Enter the country you live in: "):
    while True:
        country=input(prompt).strip().title()
        country= ' '.join(country.split())
        country=country.strip(" .-'’")
        if not country:
            print ("Country cannot be empty.")
        else:
            return country



def normalize_text(text):
    """No se preocupen papus yo lo convierto"""
    
    if not isinstance(text, str):
        return text 
    
    text=text.lower()
    text=unicodedata.normalize('NFD', text)
    text=''.join(ch for ch in text if unicodedata.category(ch)!='Mn')
    return text