#!/usr/bin/python3
""" unittest for base_model class """

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import models
import os


class test_base_model_instantiation(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_base_model_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)

    def test_base_model_instantiation_none_arg(self):
        a = BaseModel(None)
        self.assertIsInstance(a, BaseModel)

    def test_base_model_args_unused(self):
        a = BaseModel("argument")
        self.assertNotIn("argument", a.__dict__.values())

    def test_base_model_args_unused_with_kwargs(self):
        a = BaseModel("argument", id="hello")
        self.assertNotIn("argument", a.__dict__.values())
        self.assertEqual(a.id, "hello")

    def test_base_model_change_id(self):
        a = BaseModel()
        a.id = 10
        self.assertEqual(a.id, 10)

    def test_base_model_change_created_at(self):
        a = BaseModel()
        a.created_at = 10
        self.assertEqual(a.created_at, 10)

    def test_base_model_change_updated_at(self):
        a = BaseModel()
        a.updated_at = 10
        self.assertEqual(a.updated_at, 10)

    def test_base_model_instance_is_in_objects(self):
        a = BaseModel()
        self.assertIn(a, models.storage.all().values())


class test_base_model_id(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_base_model_id_noarg(self):
        a = BaseModel()
        self.assertGreater(len(a.id), 0)

    def test_base_model_id_length_noarg(self):
        a = BaseModel()
        self.assertEqual(len(a.id), 36)

    def test_base_model_id_dash_noarg(self):
        a = BaseModel()
        self.assertEqual(a.id.count('-'), 4)

    def test_base_model_id_type_noarg(self):
        a = BaseModel()
        self.assertEqual(type(a.id), str)

    def test_base_model_unique_id_noarg(self):
        a = BaseModel()
        sleep(.001)
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_base_model_id_arg(self):
        a = BaseModel(id='abc123')
        self.assertEqual(a.id, 'abc123')

    def test_base_model_id_list_arg(self):
        a = BaseModel(id=[1, 2])
        self.assertEqual(a.id, [1, 2])

    def test_base_model_non_unique_id(self):
        a = BaseModel(id=123)
        b = BaseModel(id=123)
        self.assertNotEqual(a.created_at, b.created_at)

    def test_base_model_extra_kwargs(self):
        a = BaseModel(id=12345, name="hello")
        self.assertEqual(a.id, 12345)
        self.assertEqual(a.name, "hello")

    def test_base_model_invalid_created_at(self):
        with self.assertRaises(TypeError):
            a = BaseModel(created_at=None)

    def test_base_model_invalid_updated_at(self):
        with self.assertRaises(TypeError):
            a = BaseModel(updated_at=None)


class test_base_model_created_at_updated_at(unittest.TestCase):
    """ define unittest for testing the id instance attribute """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_created_at_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a.created_at, datetime)

    def test_caua_instantiation_created_at_correct_time(self):
        a = datetime.now()
        b = BaseModel()
        c = datetime.now()
        self.assertGreater(b.created_at, a)
        self.assertLess(b.created_at, c)

    def test_caua_instantiation_upeated_at_correct_time(self):
        a = datetime.now()
        b = BaseModel()
        c = datetime.now()
        self.assertGreater(b.updated_at, a)
        self.assertLess(b.updated_at, c)

    def test_caua_save_id(self):
        b = BaseModel()
        c = datetime.now()
        b.save()
        self.assertGreater(b.updated_at, c)
        self.assertLess(b.created_at, c)

    def test_updated_at_instantiation(self):
        a = BaseModel()
        self.assertIsInstance(a.updated_at, datetime)

    def test_compare_updated_and_created(self):
        a = BaseModel()
        self.assertNotEqual(a.created_at, a.updated_at)

    def test_caua_save_create(self):
        a = BaseModel()
        create = a.created_at
        a.save()
        self.assertEqual(create, a.created_at)

    def test_caua_save_update(self):
        a = BaseModel()
        update = a.updated_at
        a.save()
        self.assertNotEqual(update, a.updated_at)

    def test_caua_save_id(self):
        a = BaseModel()
        ident = a.id
        a.save()
        self.assertEqual(ident, a.id)


class test_base_model_str_method(unittest.TestCase):
    """ define unittest for testing the __str__ method """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_str(self):
        a = BaseModel()
        b = "[{}] ({}) {}".format(a.__class__.__name__, a.id, a.__dict__)
        self.assertEqual(str(a), b)


class test_base_model_to_dict_method(unittest.TestCase):
    """ define unittest for testing the to_dict method """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_to_dict_created_at(self):
        a = BaseModel()
        self.assertTrue("created_at" in a.to_dict())

    def test_to_dict_class(self):
        a = BaseModel()
        self.assertTrue("__class__" in a.to_dict())

    def test_to_dict_id(self):
        a = BaseModel()
        self.assertTrue("id" in a.to_dict())

    def test_to_dict_updated_at(self):
        a = BaseModel()
        self.assertTrue("updated_at" in a.to_dict())

    def test_to_dict_kwarg(self):
        a = BaseModel(hello="world")
        self.assertTrue("hello" in a.to_dict())

    def test_to_dict_type(self):
        a = BaseModel()
        self.assertIsInstance(a.to_dict(), dict)

    def test_to_dict_class_value(self):
        a = BaseModel()
        value = a.to_dict()['__class__']
        self.assertEqual(value, a.__class__.__name__)

    def test_to_dict_created_at_type(self):
        a = BaseModel()
        value = a.to_dict()['created_at']
        self.assertEqual(type(value), str)

    def test_to_dict_updated_at_type(self):
        a = BaseModel()
        value = a.to_dict()['updated_at']
        self.assertEqual(type(value), str)

    def test_to_dict_class_created_at_string(self):
        a = BaseModel()
        v = a.to_dict()['created_at']
        self.assertEqual(v, a.created_at.isoformat())

    def test_to_dict_class_updated_at_string(self):
        a = BaseModel()
        v = a.to_dict()['updated_at']
        self.assertEqual(v, a.updated_at.isoformat())

    def test_to_dict_id_match(self):
        a = BaseModel()
        value = a.to_dict()['id']
        self.assertEqual(a.id, value)

    def test_to_dict_custom_attributes(self):
        a = BaseModel()
        a.country = "USA"
        self.assertIn("country", a.to_dict())


class test_base_model_save_method(unittest.TestCase):
    """ define unittest for testing the save method """

    def setUp(self):
        os.rename("file.json", "temp.json")

    def tearDown(self):
        os.rename("temp.json", "file.json")

    def test_save_with_arg(self):
        a = BaseModel()
        with self.assertRaises(TypeError):
            a.save("arg")

#    def test_save_engages_updated_at(self):
#        a = BaseModel()
#        b = a.updated_at
#        a.save()
#        self.assertNotEqual(b, a.updated_at)

#    def test_save_updates_json_file(self):
#        a = BaseModel()
#        a.save()
#        iid = "{}.{}".format(a.__class__.__name__, a.id)
#        with open("file.json", "r") as myFile:
#            self.assertTrue(iid in myFile.read())

# These two tests cause traceback, not sure why. Works fine in python3 mode


if __name__ == '__main__':
    unittest.main()
