#!/usr/bin/python3
""" unittest for file_storage class """

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import models
import os


class test_file_storage_instantiation(unittest.TestCase):
    """ define unit test for testing file storage instantiation tests """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_filestorage_instantiation(self):
        a = FileStorage()
        self.assertIsInstance(a, FileStorage)

    def test_filestorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            a = FileStorage("arg")

    def test_filestorage_file_path_private(self):
        a = FileStorage()
        with self.assertRaises(AttributeError):
            a.file_path

    def test_filestorage_objects_private(self):
        a = FileStorage()
        with self.assertRaises(AttributeError):
            a.objects


class test_file_storage_methods(unittest.TestCase):
    """ define unit test for testing file storage all method """

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_all_return_type(self):
        a = FileStorage()
        self.assertIsInstance(a.all(), dict)

    def test_all_dictionary_object(self):
        a = FileStorage()
        self.assertEqual(a.all(), a.__dict__)

    def test_file_storage_new(self):
        a = BaseModel()
        b = User()
        c = City()
        d = State()
        e = Amenity()
        f = Place()
        g = Review()
        FileStorage().new(a)
        FileStorage().new(b)
        FileStorage().new(c)
        FileStorage().new(d)
        FileStorage().new(e)
        FileStorage().new(f)
        FileStorage().new(g)
        aid = "BaseModel." + a.id
        bid = "User." + b.id
        cid = "City." + c.id
        did = "State." + d.id
        eid = "Amenity." + e.id
        fid = "Place." + f.id
        gid = "Review." + g.id
        self.assertIn(aid, FileStorage._FileStorage__objects)
        self.assertIn(bid, FileStorage._FileStorage__objects)
        self.assertIn(cid, FileStorage._FileStorage__objects)
        self.assertIn(did, FileStorage._FileStorage__objects)
        self.assertIn(eid, FileStorage._FileStorage__objects)
        self.assertIn(fid, FileStorage._FileStorage__objects)
        self.assertIn(gid, FileStorage._FileStorage__objects)

    def test_file_storage_save(self):
        a = BaseModel()
        b = User()
        c = City()
        d = State()
        e = Amenity()
        f = Place()
        g = Review()
        FileStorage().save()
        aid = "BaseModel." + a.id
        bid = "User." + b.id
        cid = "City." + c.id
        did = "State." + d.id
        eid = "Amenity." + e.id
        fid = "Place." + f.id
        gid = "Review." + g.id
        with open("file.json", "r") as myFile:
            self.assertIn(aid, myFile.read())
        with open("file.json", "r") as myFile:
            self.assertIn(bid, myFile.read())
        with open("file.json", "r") as myFile:
            self.assertIn(cid, myFile.read())
        with open("file.json", "r") as myFile:
            self.assertIn(did, myFile.read())
        with open("file.json", "r") as myFile:
            self.assertIn(eid, myFile.read())
        with open("file.json", "r") as myFile:
            self.assertIn(fid, myFile.read())
        with open("file.json", "r") as myFile:
            self.assertIn(gid, myFile.read())

    def test_file_storage_reload(self):
        a = BaseModel()
        b = User()
        c = City()
        d = State()
        e = Amenity()
        f = Place()
        g = Review()
        FileStorage().save()
        FileStorage._FileStorage__objects = {}
        FileStorage().reload()
        aid = "BaseModel." + a.id
        bid = "User." + b.id
        cid = "City." + c.id
        did = "State." + d.id
        eid = "Amenity." + e.id
        fid = "Place." + f.id
        gid = "Review." + g.id
        self.assertIn(aid, FileStorage._FileStorage__objects)
        self.assertIn(bid, FileStorage._FileStorage__objects)
        self.assertIn(cid, FileStorage._FileStorage__objects)
        self.assertIn(did, FileStorage._FileStorage__objects)
        self.assertIn(eid, FileStorage._FileStorage__objects)
        self.assertIn(fid, FileStorage._FileStorage__objects)
        self.assertIn(gid, FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
