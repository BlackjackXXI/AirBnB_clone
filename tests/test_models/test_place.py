#!/usr/bin/python3
""" unittest for place class """


import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
from time import sleep
import models
import os


class test_place_instantiation(unittest.TestCase):
    """ define unittest for testing the place class """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_place_instantiation(self):
        a = Place()
        self.assertIsInstance(a, Place)

    def test_place_inherits(self):
        a = Place()
        self.assertIsInstance(a, BaseModel)

    def test_place_public_attributes(self):
        a = Place()
        a.city_id = "city"
        a.user_id = "user"
        a.name = "name"
        a.description = "description"
        a.number_rooms = 5
        a.number_bathrooms = 4
        a.max_guest = 5
        a.price_by_night = 100
        a.latitude = 60.5
        a.longitude = 50.5
        a.amenity_ids = ["this", "is", "a", "list"]
        self.assertEqual(a.city_id, "city")
        self.assertEqual(a.user_id, "user")
        self.assertEqual(a.name, "name")
        self.assertEqual(a.description, "description")
        self.assertEqual(a.number_rooms, 5)
        self.assertEqual(a.number_bathrooms, 4)
        self.assertEqual(a.max_guest, 5)
        self.assertEqual(a.price_by_night, 100)
        self.assertEqual(a.longitude, 50.5)
        self.assertEqual(a.latitude, 60.5)
        self.assertEqual(a.amenity_ids, ["this", "is", "a", "list"])

    def test_place_attributes_types(self):
        a = Place()
        self.assertEqual(type(a.city_id), str)
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.description), str)
        self.assertEqual(type(a.number_rooms), int)
        self.assertEqual(type(a.number_bathrooms), int)
        self.assertEqual(type(a.max_guest), int)
        self.assertEqual(type(a.price_by_night), int)
        self.assertEqual(type(a.longitude), float)
        self.assertEqual(type(a.latitude), float)
        self.assertEqual(type(a.amenity_ids), list)

    def test_place_args_unused(self):
        a = Place("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_place_args_unused_with_kwargs(self):
        a = Place("argument", city_id="Oakland")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.city_id, "Oakland")

    def test_place_instance_is_in_objects(self):
        a = Place()
        self.assertIn(a, models.storage.all().values())
