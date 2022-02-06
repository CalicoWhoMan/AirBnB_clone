#!/usr/bin/python3
"""entry point for command interpretor"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exits the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command exits the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and then prints the id"""
        if arg == "BaseModel":
            newModel = BaseModel()
            newModel.save()
            print(newModel.id)
        elif arg == '':
            print("** class name missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
