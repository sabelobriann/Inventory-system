import unittest
from involuntary_system import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_item(self):
        self.inventory.add_item("apple", 10, 2.5)
        self.assertIn("apple", self.inventory.items)
        self.assertEqual(self.inventory.items["apple"]["quantity"], 10)
        self.assertEqual(self.inventory.items["apple"]["price_per_unit"], 2.5)

    def test_update_stock(self):
        self.inventory.add_item("apple", 10, 2.5)
        self.inventory.update_stock("apple", 5)
        self.assertEqual(self.inventory.items["apple"]["quantity"], 15)
        self.inventory.update_stock("apple", -20)
        self.assertEqual(self.inventory.items["apple"]["quantity"], 0)

    def test_check_stock(self):
        self.inventory.add_item("apple", 10, 2.5)
        self.assertEqual(self.inventory.check_stock("apple"), "apple has 10 units in stock.")
"""
    def test_view_inventory(self):
        self.inventory.add_item("apple", 10, 2.5)
        self.assertIn(self.inventory.view_inventory(), "apple: 10 units available at R 2.50 each")

    """
if __name__ == '__main__':
    unittest.main()