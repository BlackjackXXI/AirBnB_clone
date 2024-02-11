#!/usr/bin/python3
""" unittest for review class """

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
from time import sleep
import models
import os


class test_review_instantiation(unittest.TestCase):
    """ define unittest for testing the review class """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_review_instantiation(self):
        a = Review()
        self.assertIsInstance(a, Review)

    def test_review_inherits(self):
        a = Review()
        self.assertIsInstance(a, BaseModel)

    def test_review_public_attributes(self):
        a = Review()
        a.place_id = "place_id"
        a.user_id = "user_id"
        a.text = "text"
        self.assertEqual(a.place_id, "place_id")
        self.assertEqual(a.user_id, "user_id")
        self.assertEqual(a.text, "text")

    def test_review_attributes_types(self):
        a = Review()
        self.assertEqual(type(a.place_id), str)
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.text), str)

    def test_review_args_unused(self):
        a = Review("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_review_args_unused_with_kwargs(self):
        a = Review("argument", text="hello")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.text, "hello")

    def test_user_instance_is_in_objects(self):
        a = Review()
        self.assertIn(a, models.storage.all().values())
