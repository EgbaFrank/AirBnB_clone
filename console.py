#!/usr/bin/env python3
"""
Contains the command interpreter for the Airbnb clone
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Interpreter for the Airbnb"""
    prompt = "(hbnb) "

    class_list = ["BaseModel"]

    def do_create(self, arg):
        """Creates and saves a new instance of BaseModel"""
        args = arg.split()

        if not args:
            print("** class name missing **")

        elif len(args) == 1:
            if args[0] in self.class_list:
                base = BaseModel()
                base.save()
                print(base.id)

            else:
                print("** class doesn't exist **")
        else:
            print("Usage: create <class name>")

    def do_show(self, arg):
        """Prints an instance string representation"""
        args = arg.split()

        if not args:
            print("** class name missing **")

        if args[0] in self.class_list:
            if len(args) == 1:
                print("** instance id missing **")

            else:
                key = f"{args[0]}.{args[1]}"
                stored_dict = storage.all()

                if key in stored_dict:
                    re_base = BaseModel(**stored_dict[key])
                    print(re_base)

                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()

        if not args:
            print("** class name missing **")

        elif args[0] in self.class_list:
            if len(args) == 1:
                print("** instance id missing **")

            else:
                key = f"{args[0]}.{args[1]}"
                stored_dict = storage.all()
                
                if key in stored_dict:
                    del stored_dict[key]

                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()

        class_dict = []
        stored_dict = storage.all()

        if not args:
            for key in stored_dict:
                re_base = BaseModel(**stored_dict[key])
                class_dict.append(str(re_base))

            print(class_dict)

        else:
            if args[0] in self.class_list:
                for key, val in stored_dict.items():
                    if args[0] == val["__class__"]:
                        re_base = BaseModel(**val)
                        class_dict.append(str(re_base))

                print(class_dict)

            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")

        elif args[0] in self.class_list:
            if len(args) == 1:
                print("** instance id missing **")

            else:
                key = f"{args[0]}.{args[1]}"
                stored_dict = storage.all()
                
                if key in stored_dict:
                    if len(args) == 2:
                        print("** attribute name missing **")

                    else:
                        if len(args) == 3:
                            print("** value missing **")

                        else:
                            stored_dict[key][args[2]] = args[3]
                            storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quits command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
