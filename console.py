#!/usr/bin/python3
"""entry point for command interpretor"""

import cmd
import json
import os
from models.base_model import BaseModel
from models import storage


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
            pass
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """given a class and id, prints the associated objects
        string representation"""
        if arg != '':
            argList = arg.split()
            if len(argList) >= 2:
                if argList[0] == 'BaseModel':
                    if argList[0] + '.' + argList[1] in storage.all():
                        tempModel = storage.all()[argList[0] + '.' + argList[1]]
                        print(tempModel.__str__())
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        if arg != '':
            argList = arg.split()
            if len(argList) >= 2:
                if argList[0] == 'BaseModel':
                    if argList[0] + '.' + argList[1] in storage.all():
                        del storage.all()[argList[0] + '.' + argList[1]]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        argList = arg.split()
        if len(argList) > 0:
            if "BaseModel" in argList:
                for key, value in storage.all().items():
                    if "BaseModel" == storage.all()[key].__class__.__name__:
                        tempObj = storage.all()[key]
                        print(tempObj.__str__())
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                tempObj = storage.all()[key]
                print(tempObj.__str__())

    def do_update(self, arg):
        argList = arg.split()
        if len(argList) >= 4:
            if argList[0] == "BaseModel":
                if "BaseModel" + '.' + argList[1] in storage.all().keys():
                    tempObj = storage.all()["BaseModel" + '.' + argList[1]]
                    argF = argList[3]
                    for key, value in storage.all().items():
                        for attName, attVal in value.to_dict().items():
                            if argList[2] == attName:
                                if type(value) is int:
                                    argF = int(argList[3])
                                if type(value) is float:
                                    argF = float(argList[3])
                                else:
                                    argfSp = slice(1, -1)
                                    argF = (argList[3])[argfSp]
                    setattr(tempObj, argList[2], argF)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            if len(argList) == 3:
                print("** value missing **")
            elif len(argList) == 2:
                print("** attribute name missing **")
            elif len(argList) == 1:
                print("** instance id missing **")
            elif len(argList) == 0:
                print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
