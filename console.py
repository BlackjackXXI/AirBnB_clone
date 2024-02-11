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
    """ Console interaction handler """

    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review}

    def do_quit(self, arg):
        """ End the session """
        return True

    def do_EOF(self, arg):
        """ Handle EOF to terminate the session """
        return True

    def emptyline(self):
        """ Ignore empty lines """
        pass

    def do_create(self, arg):
        """ Create a new instance and save it """
        arglist = split(arg)
        if not arglist:
            print("** Missing class name **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** Invalid class name **")
        else:
            instance = HBNBCommand.__classes[arglist[0]]()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        """ Display the details of an instance """
        arglist = split(arg)
        if len(arglist) >  1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arglist:
            print("** Missing class name **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** Invalid class name **")
        elif len(arglist) ==  1:
            print("** Missing instance ID **")
        elif iid not in storage.all():
            print("** Instance not found **")
        else:
            print(storage.all()[iid])

    def do_destroy(self, arg):
        """ Remove an instance based on class and ID """
        arglist = split(arg)
        if len(arglist) >  1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arglist:
            print("** Missing class name **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** Invalid class name **")
        elif len(arglist) ==  1:
            print("** Missing instance ID **")
        elif iid not in storage.all():
            print("** Instance not found **")
        else:
            del storage.all()[iid]
            storage.save()

    def do_all(self, arg):
        """ List all instances of a class """
        arglist = split(arg)
        if len(arglist) and arglist[0] not in HBNBCommand.__classes:
            print("** Invalid class name **")
        else:
            plist = []
            for obj in storage.all().values():
                if len(arglist) ==  0 or arglist[0] == obj.__class__.__name__:
                    plist.append(obj.__str__())
            print(plist)

    def do_update(self, arg):
        """ Update an instance's attributes """
        arglist = split(arg)
        if len(arglist) >  1:
            iid = "{}.{}".format(arglist[0], arglist[1])
        if not arglist:
            print("** Missing class name **")
        elif arglist[0] not in HBNBCommand.__classes:
            print("** Invalid class name **")
        elif len(arglist) ==  1:
            print("** Missing instance ID **")
        elif iid not in storage.all():
            print("** Instance not found **")
        elif len(arglist) ==  2:
            print("** Attribute name missing **")
        elif len(arglist) ==  3:
            print("** Value missing **")
        else:
            setattr(storage.all()[iid], arglist[2], arglist[3])
            storage.all()[iid].save()

    def default(self, arg):
        """ Default action for unrecognized commands """
        for k in self.__classes:
            if arg == (k + '.all()'):
                self.do_all(k)
            elif arg == (k + '.count()'):
                count = sum(1 for key in storage.all() if k in key)
                print(count)
            elif arg.startswith(k + ".show(") and arg.endswith(")"):
                iid = re.search('"(.+?)"', arg)
                if iid:
                    iid = iid.group(1)
                self.do_show(k + " " + iid)
            elif arg.startswith(k + ".destroy(") and arg.endswith(")"):
                iid = re.search('"(.+?)"', arg)
                if iid:
                    iid = iid.group(1)
                self.do_destroy(k + " " + iid)
            elif arg.startswith(k + ".update(") and arg.endswith(")"):
                start = arg.find('(')
                end = arg.find(')')
                x = arg[start:end]
                x = x.replace(',', '')
                x = x[1:]
                if '{' not in x and '}' not in x:
                    al = split(x)
                    self.do_update('{} {} {} "{}"'.format(k, al[0], al[1], al[2]))

if __name__ == '__main__':
