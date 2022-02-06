#!/usr/bin/python3
"""This is the cmd line interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """class for the cmd line"""

    prompt = '(hbnb)'

    def quit_cmi(self, *args):
        """This will exit the program"""
        return True

    def help_cmi(self, *args):
        """This may or may not be used but is default already in cmi"""
        return True

    def EOF_cmi(self, *args):
        """End of File"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()