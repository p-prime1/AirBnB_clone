#!/usr/bin/python3
"""Module for the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage


classes = {
        "BaseModel": BaseModel
        }
class HBNBCommand(cmd.Cmd):
    """Class for the command intepreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it"""
        if not arg:
            print("** class name missing **")
        else:
            if arg in classes:
                cls = classes[arg]
                instance = cls()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")
    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
