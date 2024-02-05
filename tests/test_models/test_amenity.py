#!/usr/bin/python3
""" unittest for amenity class """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import models
import os


class test_amenity_instantiation(unittest.TestCase):
    """ define unittest for testing the instance attribute """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_amenity_instantiation(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_amenity_inherits(self):
        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_amenity_public_attributes(self):
        a = Amenity()
        a.name = "name"
        self.assertEqual(a.name, "name")

    def test_amenity_attributes_types(self):
        a = Amenity()
        self.assertEqual(type(a.name), str)

    def test_amenity_args_unused(self):
        a = Amenity("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_amenity_args_unused_with_kwargs(self):
        a = Amenity("argument", name="hello")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.name, "hello")

    def test_amenity_instance_is_in_objects(self):
        a = Amenity()
        self.assertIn(a, models.storage.all().values())
