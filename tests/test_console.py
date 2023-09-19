#!/usr/bin/python3
''' Module for testing console'''
import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from os import getenv, remove
import MySQLdb
from models import storage


def console_clear(f):
    f.seek(0)
    f.truncate(0)


class TestHBNBCommand(unittest.TestCase):
    ''' Class to test the console'''
    def setUp(self):
        ''' Set up test environment '''
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()

    def tearDown(self):
        ''' Remove storage file at end of tests '''
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.cursor.close()
            self.db.close()
        else:
            try:
                remove("file.json")
            except FileNotFoundError:
                pass

    def test_do_create(self):
        """Test the do_create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Test when no arguments are given
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_show(self):
        '''Test the do show method'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Test when no arguments are given
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
            console_clear(f)
            # Test when class name is missing
            HBNBCommand().onecmd("show btats")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
            console_clear(f)
            # Test when id is missing
            HBNBCommand().onecmd("show State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
            console_clear(f)
            # Test when class name and id are given but id doesn't exist
            HBNBCommand().onecmd("show State 1234-1234-1234")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            console_clear(f)
            # Test the class.show() method with class name is wrong
            HBNBCommand().onecmd("btats.show(1234-1234-1234)")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: \
                             btats.show(1234-1234-1234)\n")
            console_clear(f)

    def test_do_destroy(self):
        '''Test the do destroy method'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Test when no arguments are given
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
            console_clear(f)
            # Test when class name is missing
            HBNBCommand().onecmd("destroy btats")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
            console_clear(f)
            # Test when id is missing
            HBNBCommand().onecmd("destroy State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
            console_clear(f)
            # Test when class name and id are given but id doesn't exist
            HBNBCommand().onecmd("destroy State 1234-1234-1234")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            console_clear(f)
            # Test the class.destroy() method with class name is wrong
            HBNBCommand().onecmd("btats.destroy(1234-1234-1234)")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: \
                             btats.destroy(1234-1234-1234)\n")
            console_clear(f)

    def test_do_all(self):
        '''Test the do all method'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Test when class name is wrong
            HBNBCommand().onecmd("all btats")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
            console_clear(f)
            # Test the class.all() method with class name is wrong
            HBNBCommand().onecmd("btats.all()")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: btats.all()\n")
            console_clear(f)

    def test_do_update(self):
        '''Test the do update method'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Test when no arguments are given
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
            console_clear(f)
            # Test when class name is missing
            HBNBCommand().onecmd("update btats")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
            console_clear(f)
            # Test when id is missing
            HBNBCommand().onecmd("update State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
            console_clear(f)
            # Test when class name and id are given but id doesn't exist
            HBNBCommand().onecmd("update State 1234-1234-1234")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            console_clear(f)
            # Test when class name, id and attribute name are given but
            # attribute value is missing
            HBNBCommand().onecmd("update State 1234-1234-1234 name")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            console_clear(f)
            # Test the class.update() method with class name is wrong
            HBNBCommand().onecmd("btats.update(1234-1234-1234)")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: \
                             btats.update(1234-1234-1234)\n")
            console_clear(f)
