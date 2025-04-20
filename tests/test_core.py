from unittest import TestCase, main, mock
from inventory.core import (
    INVENTORY, INVENTORY_HISTORY,
    add_item, remove_item, summary
)
from inventory.lib.utilities import get_int

class TestInventory(TestCase):
    def setUp(self):
        INVENTORY.clear()
        INVENTORY_HISTORY.clear()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_add_new_item(self):
        add_item(name='apples', qty=20)
        add_item(name='pears', qty=5)
        add_item(name='oranges', qty=12)
        expected_inventory = {
            'apples': 20,
            'oranges': 12,
            'pears': 5,
        }
        self.assertDictEqual(INVENTORY, expected_inventory)

    @mock.patch.dict('inventory.core.INVENTORY', {'apples': 20}, clear=True)
    def test_add_to_item_qty(self):
        add_item(name='apples', qty=4)
        self.assertEqual(INVENTORY['apples'], 24)

    @mock.patch.dict('inventory.core.INVENTORY', {'apples': 12, 'pears': 20}, clear=True)
    def test_remove_item_completely(self):
        remove_item(name='apples', qty=12)
        expected_inventory = {'pears': 20}
        self.assertDictEqual(INVENTORY, expected_inventory)

    @mock.patch.dict('inventory.core.INVENTORY', {'apples': 12, 'pears': 20}, clear=True)
    def test_remove_item_qty(self):
        remove_item(name='pears', qty=10)
        self.assertEqual(INVENTORY['pears'], 10)

    @mock.patch.dict('inventory.core.INVENTORY', {'apples': 12, 'pears': 20}, clear=True)
    def test_remove_more_than_item_qty(self):
        remove_item(name='pears', qty=21)
        self.assertEqual(INVENTORY['pears'], 20)

    @mock.patch.dict('inventory.core.INVENTORY', {'apples': 23, 'bananas': 30, 'pears': 32, 'berries': 12, 'oranges': 14}, clear=True)
    def test_summary(self):
        self.assertEqual(summary(), (111, 5, 'pears', 'berries'))

    def test_get_int_valid(self):
        self.assertIsInstance(get_int('2'), int)
        self.assertEqual(get_int('2'), 2)
        self.assertIsInstance(get_int('23 '), int)
        self.assertEqual(get_int('23 '), 23)

    def test_get_int_invalid(self):
        with self.assertRaises(Exception):
            get_int('abc')
            get_int('abc ')
            get_int('DEF')
            get_int('DEF ')

if __name__ == '__main__':
    main()
