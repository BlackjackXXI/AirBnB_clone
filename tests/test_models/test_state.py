#!/usr/bin/python3
""" unittest for State class """

import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
from time import sleep
import models
import os


class test_state_instantiation(unittest.TestCase):
    """ define unittest for testing State """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_state_instantiation(self):
        a = State()
        self.assertIsInstance(a, State)

    def test_state_inherits(self):
        a = State()
        self.assertIsInstance(a, BaseModel)

    def test_user_public_attributes(self):
        a = State()
        a.name = "name"
        self.assertEqual(a.name, "name")

    def test_user_attributes_types(self):
        a = State()
        self.assertEqual(type(a.name), str)

    def test_user_args_unused(self):
        a = State("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_user_args_unused_with_kwargs(self):
        a = State("argument", name="hello")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.name, "hello")

    def test_user_instance_is_in_objects(self):
        a = State()
        self.assertIn(a, models.storage.all().values())
