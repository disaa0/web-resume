import unittest
import os
from app import assets_path, templates_path
class TestFileExistence(unittest.TestCase):
    
    def test_file_exists(self):
        filenames = {assets_path : ['metadata.yaml', 'styles.css',], templates_path : ['index.html']}
        for directory, files in filenames.items():
            for filename in files:
                file_path = directory+filename
                self.assertTrue(os.path.exists(file_path), f"File '{file_path}' does not exist.")


if __name__ == '__main__':
    unittest.main()