import unittest
from assignment4 import UniqueStack, LimitedStack, RotatingStack

class UniqueLimitedStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"
    
    #! Check empty condition
    def test_base_stack_empty(self):
        test_stack = UniqueStack()
        self.assertEqual(0, test_stack.size())
        
    #! Push increase size
    def test_push_increases_size(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueLimitedStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    #! Check for duplicate items protection
    def test_push_duplicates(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueLimitedStackTestCase.ITEM_1)
        with self.assertRaises(ValueError):
            test_stack.push(UniqueLimitedStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    #! Check for peek function
    def test_peek_size_remains(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueLimitedStackTestCase.ITEM_1)
        self.assertEqual(UniqueLimitedStackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    #! Check if none pushing
    def test_push_none(self):
        test_stack = UniqueStack()
        with self.assertRaises(TypeError):
            test_stack.push(None)

    #! Check poping empty stack
    def test_pop_empty_stack(self):
        test_stack = UniqueStack()
        self.assertEqual(None, test_stack.pop())

    #! Check poping
    def test_pop_single_item(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueLimitedStackTestCase.ITEM_1)
        self.assertEqual(UniqueLimitedStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    #! Check stack property
    def test_last_in_first_out(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueLimitedStackTestCase.ITEM_1)
        test_stack.push(UniqueLimitedStackTestCase.ITEM_2)
        test_stack.push(UniqueLimitedStackTestCase.ITEM_3)
        self.assertEqual(3, test_stack.size())

        self.assertEqual(UniqueLimitedStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(UniqueLimitedStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(UniqueLimitedStackTestCase.ITEM_1, test_stack.pop())


class LimitedStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    #! Test if init is correct
    def test_init(self):
        with self.assertRaises(TypeError):
            test_stack = LimitedStack("hello")
        with self.assertRaises(TypeError):
            test_stack = LimitedStack(None)
        with self.assertRaises(ValueError):
            test_stack = LimitedStack(-1)
    #! Test for over pushing
    def test_overpush(self):
        test_stack = LimitedStack(2)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        test_stack.push(LimitedStackTestCase.ITEM_2)
        with self.assertRaises(Exception):
            test_stack.push(LimitedStackTestCase.ITEM_3)

    def test_base_stack_empty(self):
        test_stack = LimitedStack(3)
        self.assertEqual(0, test_stack.size())

    def test_push_increases_size(self):
        test_stack = LimitedStack(3)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    def test_peek_size_remains(self):
        test_stack = LimitedStack(3)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        self.assertEqual(LimitedStackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = LimitedStack(3)
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_pop_empty_stack(self):
        test_stack = LimitedStack(3)
        self.assertEqual(None, test_stack.pop())

    def test_pop_single_item(self):
        test_stack = LimitedStack(3)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        self.assertEqual(LimitedStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    def test_last_in_first_out(self):
        test_stack = LimitedStack(3)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        test_stack.push(LimitedStackTestCase.ITEM_2)
        test_stack.push(LimitedStackTestCase.ITEM_3)
        self.assertEqual(3, test_stack.size())

        self.assertEqual(LimitedStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(LimitedStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(LimitedStackTestCase.ITEM_1, test_stack.pop())

class RotatingLimitedStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"
    #! Test if init is correct
    def test_init(self):
        with self.assertRaises(TypeError):
            test_stack = RotatingStack("hello")
        with self.assertRaises(TypeError):
            test_stack = RotatingStack(None)
        with self.assertRaises(ValueError):
            test_stack = RotatingStack(-1)
    #! Test for over pushing
    def test_overpush(self):
        test_stack = RotatingStack(2)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_1)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_2)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_3)

    def test_base_stack_empty(self):
        test_stack = RotatingStack(3)
        self.assertEqual(0, test_stack.size())

    def test_push_increases_size(self):
        test_stack = RotatingStack(3)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    def test_peek_size_remains(self):
        test_stack = RotatingStack(3)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_1)
        self.assertEqual(RotatingLimitedStackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = RotatingStack(3)
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_pop_empty_stack(self):
        test_stack = RotatingStack(3)
        self.assertEqual(None, test_stack.pop())

    def test_pop_single_item(self):
        test_stack = RotatingStack(3)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_1)
        self.assertEqual(RotatingLimitedStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    #! Also test auto poping
    def test_last_in_first_out(self):
        test_stack = RotatingStack(2)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_1)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_2)
        test_stack.push(RotatingLimitedStackTestCase.ITEM_3)
        self.assertEqual(2, test_stack.size())

        self.assertEqual(RotatingLimitedStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(RotatingLimitedStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(0,test_stack.size())

if __name__ == '__main__':
    unittest.main()
