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

    def do_destroy(self, arg):
        """Deletes an instance on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, arg):
        """Prints a string representation of all instances"""
        args = arg.split()
        if len(args) >= 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                result = [str(obj) for obj in storage.all().values()]
                print(result)
        else:
            result = [str(obj) for obj in storage.all().values()]
            print(result)


    def do_update(self, arg):
        """Updates an instance based on the class naem and id"""
        args = arg.split()
        obj = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = obj[key]
            attr_name = args[2]
            attr_value = args[3]

            try:
                attr_value = eval(attr_value)
            except Exception:
                pass

            setattr(instance, attr_name, attr_value)
            instance.save()


    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
