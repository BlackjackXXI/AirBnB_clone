#!/usr/bin/python3
""" unittest for city class """

import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from time import sleep
import models
import os


class test_city_instantiation(unittest.TestCase):
    """ define unittest for testing the city instance attribute """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_city_instantiation(self):
        a = City()
        self.assertIsInstance(a, City)

    def test_city_inherits(self):
        a = City()
        self.assertIsInstance(a, BaseModel)

    def test_city_public_attributes(self):
        a = City()
        a.state_id = "state_id"
        a.name = "name"
        self.assertEqual(a.state_id, "state_id")
        self.assertEqual(a.name, "name")

    def test_city_attributes_types(self):
        a = City()
        self.assertEqual(type(a.state_id), str)
        self.assertEqual(type(a.name), str)

    def test_city_args_unused(self):
        a = City("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_city_args_unused_with_kwargs(self):
        a = City("argument", name="hello")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.name, "hello")

    def test_city_instance_is_in_objects(self):
        a = City()
        self.assertIn(a, models.storage.all().values())
