import unittest
import scripts
import db
from pathlib import Path

class TestScripts(unittest.TestCase):
    def test_create_db(self):
        #check if the database file exists
        data_file = Path("data.db")
        if not data_file.is_file():
            scripts.create_db()
        self.assertEqual(data_file.is_file(), True)
            

    def test_clear_db(self):
        #check if the data got cleared
        scripts.clear_db()
        data = db.DB("data.db") 
        self.assertEqual(data.get_all_data(), [])

    def test_fill_db(self):
        #check if the data in the database table exists after clearing it
        scripts.fill_db()
        data = db.DB("data.db")
        self.assertTrue(len(data.get_all_data()) > 0 )


if __name__ == '__main__':
    unittest.main()