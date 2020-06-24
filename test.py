import unittest
import time

import pagination

class TestPagination(unittest.TestCase): 
    def test_pagination(self):
        """
        Should return no page around 4, 1 page in the beginning and 1 page in the end
        """
        self.assertEqual(pagination.pagination(4, 5, 1, 0), [1, '...', 4, 5])
    
    def test_pagination_boundaries(self):
        """
        Should return 2 pages around 4, 2 pages in the beginning and 2 pages in the end
        """
        self.assertEqual(pagination.pagination(4, 10, 2, 2), [1, 2, 3, 4, 5, 6, '...', 9, 10])

    def test_pagination_performance(self):
        """
        Should return quickly, even when total pages number is very large
        """
        
        before = time.time()
        
        self.assertEqual(
            pagination.pagination(
                current_page=10000, 
                total_pages=50000000,
                boundaries=2,
                around=2
             ),
            [1, 2, "...", 9998, 9999, 10000, 10001, 10002, "...", 49999999, 50000000],
        )
        
        after = time.time()
        elapsed_seconds = after - before
        
        self.assertTrue(
            elapsed_seconds < 1,
            f"pagination took too long ({elapsed_seconds} seconds)"
        )
        
    def test_pagination_invalid(self):
        """
        Should return number of pages when total pages number is smaller than current page 
        """
        self.assertEqual(pagination.pagination(4, 2, 2, 2), [1, 2])

    def test_pagination_invalid_boundaries(self):
        """
        Should return number of pages when total pages number is smaller than boundaries 
        """
        self.assertEqual(pagination.pagination(4, 3, 5, 2), [1, 2, 3])

if __name__ == '__main__': 
    unittest.main() 
