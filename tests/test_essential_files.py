import unittest
import os
import yaml

class TestEssentialFiles(unittest.TestCase):
    
    def test_metadata_yaml_exists(self):
        metadata_path = './metadata/metadata.yaml'
        self.assertTrue(os.path.exists(metadata_path), f"File '{metadata_path}' does not exist.")

    def test_active_template(self):
        metadata_path = './metadata/metadata.yaml'
        with open(metadata_path, 'r') as file:
            metadata = yaml.safe_load(file)
        
        template_name = metadata.get('template')
        self.assertIsNotNone(template_name, "No template specified in metadata.yaml")
        
        template_path = f'./templates/{template_name}'
        self.assertTrue(os.path.exists(template_path), f"Specified template '{template_path}' does not exist.")

if __name__ == '__main__':
    unittest.main()