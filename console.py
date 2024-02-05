#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from shlex import split
import re


class HBNBCommand(cmd.Cmd):
    """ Class to define console behavior """

    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing for an empty line """
        pass

    def do_create(self, arg):
        """create a new class instance, saves it to JSON, print its id"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.__classes[arg]()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        """show command to print the str representation of an instance"""
        arglist = split(arg)
        if len(arglist) > 1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arg:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif iid not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[iid])

    def do_destroy(self, arg):
        """destroy command to delete instance based on class name and id"""
        arglist = split(arg)
        if len(arglist) > 1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arg:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif iid not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[iid]
            storage.save()

    def do_all(self, arg):
        """all command to print all string representations of instances"""
        arglist = split(arg)
        if len(arglist) and arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            plist = []
            for obj in storage.all().values():
                if len(arglist) == 0:
                    plist.append(obj.__str__())
                elif arglist[0] == obj.__class__.__name__:
                    plist.append(obj.__str__())
            print(plist)

    def do_update(self, arg):
        """update command to update an instance based on the class name"""
        arglist = split(arg)
        if len(arglist) > 1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arg:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif iid not in storage.all():
            print("** no instance found **")
        elif len(arglist) == 2:
            print("** attribute name missing **")
        elif len(arglist) == 3:
            print("** value missing **")
        else:
            setattr(storage.all()[iid], arglist[2], arglist[3])
            storage.all()[iid].save()

    def default(self, arg):
        """method to define default behavior when "do" syntax not used"""
        for k in self.__classes:
            if arg == (k + '.all()'):
                self.do_all(k)
            elif arg == (k + '.count()'):
                count = 0
                for key in storage.all():
                    if k in key:
                        count += 1
                print(count)
            elif arg.startswith(k + ".show(") and arg.endswith(")"):
                x = re.search('"(.+?)"', arg)
                if x:
                    iid = x.group(1)
                self.do_show(k + " " + iid)
            elif arg.startswith(k + ".destroy(") and arg.endswith(")"):
                x = re.search('"(.+?)"', arg)
                if x:
                    iid = x.group(1)
                self.do_destroy(k + " " + iid)
            elif arg.startswith(k + ".update(") and arg.endswith(")"):
                start = arg.find('(')
                end = arg.find(')')
                x = arg[start:end]
                x = x.replace(',', '')
                x = x[1:]
                if '{' not in x and '}' not in x:
                    al = split(x)
                    self.do_update('{} {} {} "{}"'.format
                                   (k, al[0], al[1], al[2]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
