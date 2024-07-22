import unittest
from find_duplicate_file_contents import find_duplicate_files, hash_the_contents, read_contents
import tempfile
import os

class TestReadContents(unittest.TestCase):
    def test_read_contents(self):
        with open("test_file.txt", "w") as f:
            f.write("Hello, world!")
        content = read_contents("test_file.txt")
        self.assertEqual(content, b"Hello, world!")

    def test_read_contents_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_contents("non_existent_file.txt")

class TestHashTheContents(unittest.TestCase):
    def test_hash_the_contents(self):
        hash1 = hash_the_contents(b"Hello, world!")
        hash2 = hash_the_contents(b"Hello, world!")
        self.assertEqual(hash1, hash2)
        
        hash3 = hash_the_contents(b"Goodbye, world!")
        self.assertNotEqual(hash1, hash3)

class TestFindDuplicateFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file1 = os.path.join(self.test_dir, "file1.txt")
        self.file2 = os.path.join(self.test_dir, "file2.txt")
        self.file3 = os.path.join(self.test_dir, "file3.txt")
        
        with open(self.file1, "w") as f:
            f.write("duplicate content")
        with open(self.file2, "w") as f:
            f.write("duplicate content")
        with open(self.file3, "w") as f:
            f.write("unique content")
    
    def tearDown(self):
        # Clean up the temporary files and directory
        os.remove(self.file1)
        os.remove(self.file2)
        os.remove(self.file3)
        os.rmdir(self.test_dir)
    
    def test_find_duplicate_files(self):
        # Run the function to find duplicates
        duplicates = find_duplicate_files(self.test_dir)
        
        # Check the results
        self.assertEqual(len(duplicates), 1)  # Should find one group of duplicates
        self.assertIn(self.file1, duplicates[0])
        self.assertIn(self.file2, duplicates[0])
        self.assertNotIn(self.file3, duplicates[0])