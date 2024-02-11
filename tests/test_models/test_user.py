#!/usr/bin/python3
""" unittest for base_model class """

import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from time import sleep
import models
import os


class test_user_instantiation(unittest.TestCase):
    """ define unittest for testing the instance attribute """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_user_instantiation(self):
        a = User()
        self.assertIsInstance(a, User)

    def test_user_inherits(self):
        a = User()
        self.assertIsInstance(a, BaseModel)

    def test_user_public_attributes(self):
        a = User()
        a.email = "email"
        a.password = "password"
        a.first_name = "first"
        a.last_name = "last"
        self.assertEqual(a.email, "email")
        self.assertEqual(a.password, "password")
        self.assertEqual(a.first_name, "first")
        self.assertEqual(a.last_name, "last")

    def test_user_attributes_types(self):
        a = User()
        self.assertEqual(type(a.email), str)
        self.assertEqual(type(a.password), str)
        self.assertEqual(type(a.first_name), str)
        self.assertEqual(type(a.last_name), str)

    def test_user_args_unused(self):
        a = User("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_user_args_unused_with_kwargs(self):
        a = User("argument", email="hello")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.email, "hello")

    def test_user_instance_is_in_objects(self):
        a = User()
        self.assertIn(a, models.storage.all().values())
