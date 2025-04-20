from unittest import TestCase, main, mock
from inventory.core import (
    INVENTORY, INVENTORY_HISTORY,
    add_item, remove_item, summary, get_int
)

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

    @mock.patch.dict('inventory.INVENTORY', {'apples': 20}, clear=True)
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
    @mock.patch('builtins.print')
    def test_summary(self, mock_print):
        summary()
        self.assertEqual(mock_print.call_args_list[0][0][0], 'Total number of items in stock: 111')
        self.assertEqual(mock_print.call_args_list[1][0][0], 'Total unique item types: 5')
        self.assertEqual(mock_print.call_args_list[2][0][0], 'Most stocked item: pears')
        self.assertEqual(mock_print.call_args_list[3][0][0], 'Least stocked item: berries')
        self.assertEqual(mock_print.call_count, 4)

    @mock.patch('builtins.input')
    def test_get_int_valid(self, mock_input):
        mock_input.return_value = '2'
        result = get_int('How many of this item: ')
        self.assertIsInstance(result, int)
        self.assertEqual(result, 2)

    @mock.patch('builtins.input')
    def test_get_int_invalid(self, mock_input):
        mock_input.side_effect = ['abc', '5']
        result = get_int('How many of this item: ')
        self.assertEqual(result, 5)

if __name__ == '__main__':
    main()
