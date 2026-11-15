import json
from pathlib import Path

class level:
    def __init__(self, d: dict):
        self.id: int = -1
        self.name: str = "None"
        self.author: str = "None"
        self.creators: list[str] = []
        self.verifier: str = "None"
        self.verification: str = ""
        self.percentToQualify: str = "-1"
        self.password = "Not Copyable"
        self.records: list = []


def add_to_list(level: str, place: int) -> bool:
    level_file_name = "data/" + level + ".json"
    if not Path(level_file_name).is_file():
        raise FileNotFoundError("Could not find file " + level_file_name)
    
    if (place < 1):
        raise IndexError("Placement cannot be less than 1: " + str(place))
    
    with open("data/_list.json", "r+") as file:
        levels = json.load(file)

    if (place > len(levels) + 1):
        raise IndexError("Placement cannot be greater than number of levels + 1: " + str(place))

    if level in levels:
        raise Exception(str(level) + " already in list at position: " + str(levels.index(level)+1))

    levels.insert(place-1, level)
    with open("data/_list.json", "w") as file:
        json.dump(levels, file, indent=4)
    print(f"Successfully added level {level} at position {place}")


def print_list() -> None:
    with open("data/_list.json", "r") as file:
        levels = json.load(file)
    print("Current list: ")
    for i in range(len(levels)):
        print(f"{i+1}. {levels[i]}")
    
def print_unused_levels() -> None:
    print("Unused Levels: " + str(get_unused_levels()))

def get_unused_levels() -> list:
    with open("data/_list.json", "r") as file:
        levels = json.load(file)
    directory = Path("data/")
    files = [f.name[0:len(f.name)-5] for f in directory.iterdir() if (f.is_file() and f.name[0] != "_")]
    new_levels = [l for l in files if l not in levels]
    return new_levels

def main():
    done = False
    while not done:
        str_in: str = input("What would you like to do? 1 to edit the list, 2 to edit levels, 3 to edit records: ")
        mode: int = int(str_in)
        if mode == 1:
            str_in = input("What would you like to do? 1 to add a level, 2 to remove a level, 3 to move a level")
            mode = int(str_in)
            if mode == 1:
                print_list()
                new_levels = get_unused_levels()
                print_unused_levels()
                str_in = input("Which level would you like to add: ")
                while str_in != "" and str_in not in new_levels:
                    str_in = input("Not a valid level. (Type nothing to cancel): ")
                level_adding = str_in
                if str_in in new_levels:
                    str_in = input("What place would you like to put the level: ")
                    place = int(str_in)
                    try:
                        add_to_list(level_adding, place)
                    except Exception as e:
                        print(e)
                    print_list()



        elif mode == 2:
            str_in = input("What would you like to do? 1 to create a level, 2 to delete a level, 3 to edit a level")
            mode = int(str_in)
            if mode == 1:
                level: dict = {}

                str_in = input("Please enter the id of the level: ")
                level["id"] = int(str_in)
                str_in = input("Please enter the name of the level: ")
                level["name"] = str_in
                str_in = input("Please enter the author of the level: ")
                level["author"] = str_in
                creators = []
                str_in = input("Please enter the creator(s) of the level (Type nothing when finished): ")
                while str_in != "":
                    creators.append(str_in)
                    str_in = input("Please enter the creator(s) of the level (Type nothing when finished): ")
                level["creators"] = creators
                str_in = input("Please enter the verifier of the level: ")
                level["verifier"] = str_in
                str_in = input("Please enter the verification youtube link: ")
                level["verification"] = str_in
                str_in = input("Please enter the percentToQualify: ")
                level["percentToQualify"] = str_in
                str_in = input("Please enter the password to copy the level (Not Copyable if not):")
                level["password"] = str_in
                level["records"] = []
                level_string = level["name"].lower().replace(" ", "_")
                with open("data/"+level_string + ".json", "w") as file:
                    json.dump(level, file, indent=4)

                str_in = input("Successfully addded " + level_string + " to files. Add to list? (y/n)")
                if (str_in == "y"):
                    print_list()
                    str_in = input("What place would you like to put the level: ")
                    place = int(str_in)
                    try:
                        add_to_list(level_string, place)
                    except Exception as e:
                        print(e)
                    print_list()



        done = not(input("Would you like to continue (y/n): ") == "y")

if __name__ == "__main__":
    main()