import unittest

import pagination

class TestPagination(unittest.TestCase): 
    def test_pagination(self):
        """
        Should give no page around 4, 1 page in the beginning and 1 page in the end
        """
        self.assertEqual(pagination.pagination(4, 5, 1, 0), [1, '...', 4, 5])
    
    def test_pagination_boundaries(self):
        """
        Should give 2 pages around 4, 2 pages in the beginning and 2 pages in the end
        """
        self.assertEqual(pagination.pagination(4, 10, 2, 2), [1, 2, 3, 4, 5, 6, '...', 9, 10])
if __name__ == '__main__': 
    unittest.main() 
