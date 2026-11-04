import json


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

        

def main():
    done = False
    while not done:
        str_in: str = input("What would you like to do? 1 to edit the list, 2 to edit levels, 3 to edit records: ")
        mode: int = int(str_in)
        if mode == 1:
            print("get fucked lol")
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
                str_in = input("Please enter the percentToQualify:")
                level["percentToQualify"] = str_in
                str_in = input("Please enter the password to copy the level (Not Copyable if not):")
                level["password"] = str_in
                level["records"] = []
                level_string = level["name"].lower().replace(" ", "_") + ".json"
                with open("data/"+level_string, "w") as file:
                    json.dump(level, file, indent=4)

                print("Successfully addded " + level_string + "to files. Add to list?")



        done = not(input("Would you like to continue (y/n): ") == "y")

if __name__ == "__main__":
    main()