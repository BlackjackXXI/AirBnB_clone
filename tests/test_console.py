#!/usr/bin/python3
""" unittest for console """

import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class test_console_help_messages(unittest.TestCase):
    """ define unittest for testing the help command within hbnb console """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_only_help(self):
        check = "Documented commands (type help <topic>):\n"
        check += "========================================\n"
        check += "EOF  all  create  destroy  help  quit  show  update"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_quit(self):
        check = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_create(self):
        check = 'create a new class instance, saves it to JSON, print its id'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_EOF(self):
        check = "EOF command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_show(self):
        check = "show command to print the str representation of an instance"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_destroy(self):
        check = "destroy command to delete instance based on class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_all(self):
        check = "all command to print all string representations of instances"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_update(self):
        check = "update command to update an instance based on the class name"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
        self.assertEqual(check, output.getvalue().strip())

    def test_help_invalid(self):
        check = "*** No help on invalid"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help invalid"))
        self.assertEqual(check, output.getvalue().strip())


class test_console_create_command(unittest.TestCase):
    """ define unittest for testing the hbnb console create command """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_create_only(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
        self.assertEqual(check, output.getvalue().strip())

    def test_create_invalid(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create invalid"))
        self.assertEqual(check, output.getvalue().strip())

    def test_create_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("BaseModel", output.getvalue().strip())

    def test_create_User(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("User", output.getvalue().strip())

    def test_create_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("State", output.getvalue().strip())

    def test_create_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("City", output.getvalue().strip())

    def test_create_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("Place", output.getvalue().strip())

    def test_create_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("Amenity", output.getvalue().strip())

    def test_create_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("Review", output.getvalue().strip())


class test_console_show_command(unittest.TestCase):
    """ define unittest for testing the hbnb show create command """

    def test_show_alone(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_invalid_class(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show NotAClass"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_basemodel(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_user(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_city(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_state(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_place(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_review(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_missing_id_amenity(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 12345"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_basemodel(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_user(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_city(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_state(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_place(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_review(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_no_id_amenity(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))

    def test_show_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show BaseModel {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show User {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_city(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show City {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_state(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show State {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show Place {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show Review {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "show Amenity {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())


class test_console_show_command_second_syntax(unittest.TestCase):
    """
    define unittest for testing the hbnb console show command
    uss the dot syntax
    """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_show_BaseModel_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'BaseModel.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_User_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'User.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_State_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'State.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_City_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'City.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_Amenity_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'Amenity.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_Place_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'Place.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_Review_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'Review.show("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_show_BaseModel_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        command = 'BaseModel.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_User_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        command = 'User.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_State_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        command = 'State.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_City_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        command = 'City.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_Amenity_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        command = 'Amenity.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_Place_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        command = 'Place.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())

    def test_show_Review_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        command = 'Review.show("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertIn(iid, output.getvalue().strip())


class test_console_destroy_command(unittest.TestCase):
    """ define unittest for testing the hbnb console destroy command """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_destroy_only(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_invalid(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy invalid"))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_BaseModel_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy BaseModel"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_User_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy User"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_State_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy State"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_City_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy City"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Amenity_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Amenity"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Place_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Place"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Review_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Review"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_BaseModel_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy BaseModel bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_User_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy User bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_State_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy State bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_City_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy City bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Amenity_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Amenity bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Place_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Place bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Review_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Review bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy BaseModel {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_User(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy User {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy State {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy City {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Amenity {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Place {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            command = "destroy Review {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())


class test_console_destroy_command_second_syntax(unittest.TestCase):
    """
    define unittest for testing the hbnb console destroy command
    uss the dot syntax
    """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_destroy_BaseModel_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'BaseModel.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_User_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'User.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_State_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'State.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_City_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'City.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Amenity_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'Amenity.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Place_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'Place.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_Review_bad_id_2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = 'Review.destroy("bad_id")'
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_destroy_BaseModel_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'BaseModel.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_User_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'User.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_State_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'State.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_City_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'City.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_Amenity_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'Amenity.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_Place_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'Place.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_destroy_Review_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())
        command = 'Review.destroy("' + iid + '")'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertNotIn(iid, output.getvalue().strip())


class test_console_all_command(unittest.TestCase):
    """
    define unittest for testing the hbnb console all command
    """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_all_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn(iid, output.getvalue().strip())

    def test_all_invalid(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all invalid"))
        self.assertEqual(check, output.getvalue().strip())

    def test_all_command_with_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_User(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())


class test_console_all_command_second_syntax(unittest.TestCase):
    """
    define unittest for testing the hbnb console all command
    """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_all_command_with_BaseModel_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_User_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_State_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_City_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_Amenity_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_Place_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())

    def test_all_command_with_Review_2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
        self.assertIn(iid, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertNotIn(iid, output.getvalue().strip())


class test_console_count_command(unittest.TestCase):
    """
    define unittest for testing the hbnb console count command
    """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_count_command_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)

    def test_count_command_User(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)

    def test_count_command_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)

    def test_count_command_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)

    def test_count_command_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)

    def test_count_command_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)

    def test_count_command_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
        count1 = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
        count2 = output.getvalue().strip()
        self.assertEqual(int(count1), int(count2) - 1)


class test_console_update_command(unittest.TestCase):
    """ define unittest for testing the hbnb console update command """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_update_only(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_invalid(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update invalid"))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_BaseModel_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update BaseModel"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_User_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update User"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_State_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update State"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_City_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update City"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Amenity_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Amenity"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Place_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Place"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Review_no_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Review"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_BaseModel_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update BaseModel {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_User_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update User {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_State_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update State {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_City_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update City {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Amenity_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Amenity {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Place_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Place {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Review_no_attribute(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Review {}".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_BaseModel_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update BaseModel bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_User_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update User bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_State_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update State bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_City_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update City bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Amenity_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Amenity bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Place_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Place bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Review_bad_id(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Review bad_id"
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_BaseModel_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update BaseModel {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_User_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update User {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_State_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update State {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_City_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update City {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Amenity_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Amenity {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Place_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Place {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_Review_no_value(self):
        check = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Review {} instance".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(check, output.getvalue().strip())

    def test_update_BaseModel_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update BaseModel {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())

    def test_update_User_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update User {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())

    def test_update_State_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update State {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())

    def test_update_City_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update City {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())

    def test_update_Amenity_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Amenity {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())

    def test_update_Place_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Place {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())

    def test_update_Review_correct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Review {} species cat".format(iid)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
        self.assertIn("'species': 'cat'", output.getvalue().strip())


class test_console_update_command_second_syntax(unittest.TestCase):
    """ define unittest for testing the hbnb console update command 2 """

    def test_update_BaseModel_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        iid = output.getvalue().strip()
        command = "BaseModel.update(" + iid + " color red)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
        self.assertIn("'color': 'red'", output.getvalue().strip())

    def test_update_City_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        iid = output.getvalue().strip()
        command = "City.update(" + iid + " color rainbow)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
        self.assertIn("'color': 'rainbow'", output.getvalue().strip())

    def test_update_User_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        iid = output.getvalue().strip()
        command = "User.update(" + iid + " color orange)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
        self.assertIn("'color': 'orange'", output.getvalue().strip())

    def test_update_State_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        iid = output.getvalue().strip()
        command = "State.update(" + iid + " color yellow)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
        self.assertIn("'color': 'yellow'", output.getvalue().strip())

    def test_update_Amenity_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        iid = output.getvalue().strip()
        command = "Amenity.update(" + iid + " color green)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
        self.assertIn("'color': 'green'", output.getvalue().strip())

    def test_update_Place_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        iid = output.getvalue().strip()
        command = "Place.update(" + iid + " color blue)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
        self.assertIn("'color': 'blue'", output.getvalue().strip())

    def test_update_Review_id_attribute(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        iid = output.getvalue().strip()
        command = "Review.update(" + iid + " color purple)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
        self.assertIn("'color': 'purple'", output.getvalue().strip())


class test_console_exit_commands(unittest.TestCase):
    """ define unittest for testing the hbnb console update command """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_check_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
                self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_check_eof(self):
        with patch("sys.stdout", new=StringIO()) as output:
                self.assertTrue(HBNBCommand().onecmd("EOF"))
