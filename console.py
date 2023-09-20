#!/usr/bin/python3
""" Console Module """
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) '
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
    }

    def emptyline(self):
        """Ignore empty spaces."""
        pass

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        return True

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def do_create(self, line):
        """ Create an object of any class"""
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for j in range(1, len(my_list)):
                key, value = tuple(my_list[j].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, line):
        """ Shows all objects, or all objects of a class"""
        if not line:
            j = storage.all()
            print([j[k].__str__() for k in j])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            m = storage.all(eval(args[0]))
            print([m[k].__str__() for k in m])
        except NameError:
            print("** class doesn't exist **")

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, line):
        """Count current number of class instances"""
        counter = 0
        try:
            lis_t = split(line, " ")
            if lis_t[0] not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == lis_t[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, line):
        """ Updates a certain object with new info """
        try:
            if not line:
                raise SyntaxError()
            lis_t = split(line, " ")
            if lis_t[0] not in self.__classes:
                raise NameError()
            if len(lis_t) < 2:
                raise IndexError()
            objects = storage.all()
            key = lis_t[0] + '.' + lis_t[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(lis_t) < 4:
                raise ValueError()
            j = objects[key]
            try:
                j.__dict__[lis_t[2]] = eval(lis_t[3])
            except Exception:
                j.__dict__[lis_t[2]] = lis_t[3]
                j.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** value missing **")
        except ValueError:
            print("** value missing **")     

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def strip__clean(self, args):
        """strips the argument and return a string of command"""
        new_l = []
        new_l.append(args[0])
        try:
            my_dict = eval(
                    args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_l.append(((new_str.split(", "))[0]).strip('"'))
            new_l.append(my_dict)
            return new_l
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_l.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """retrieve all instances of a class and 
            retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                    else:
                        self.do_update(args)
        else:
            cmd.Cmd.default(self,line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
