from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class ShoppingCartTests(TestCase):
    SHOP_NAME = "TestName"
    BUDGET = 100
    PRODUCT_NAME = "bread"
    PRODUCT_PRICE = 5

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart(self.SHOP_NAME, self.BUDGET)

    def test_initialization_properly(self):
        self.assertEqual(self.SHOP_NAME, self.shopping_cart.shop_name)
        self.assertEqual(self.BUDGET, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_not_starts_with_uppercase_letter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.shop_name = "aaaa"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_contains_not_only_letter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.shop_name = "A123"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_add_product_to_cart_successfully(self):
        expected = "bread product was successfully added to the cart!"
        actual = self.shopping_cart.add_to_cart("bread", 5)
        self.assertEqual(expected, actual)
        self.shopping_cart.add_to_cart("eggs", 2)
        expected_products = {
            "bread": 5,
            "eggs": 2
        }
        self.assertEqual(expected_products, self.shopping_cart.products)

    def test_add_to_cart_a_product_cost_more_than_or_equal_to_hundred_raises(self):
        expected = f"Product {self.PRODUCT_NAME} cost too much!"

        product_price = 100
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.add_to_cart(self.PRODUCT_NAME, product_price)
        self.assertEqual(expected, str(error.exception))

        product_price = 101
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.add_to_cart(self.PRODUCT_NAME, product_price)
        self.assertEqual(expected, str(error.exception))

    def test_remove_from_cart_successfully(self):
        expected = f"Product {self.PRODUCT_NAME} was successfully removed from the cart!"
        self.shopping_cart.add_to_cart(self.PRODUCT_NAME, self.PRODUCT_PRICE)
        self.shopping_cart.add_to_cart("eggs", 2)
        actual = self.shopping_cart.remove_from_cart(self.PRODUCT_NAME)
        self.assertEqual(expected, actual)
        expected_products = {"eggs":2}
        self.assertEqual(expected_products, self.shopping_cart.products)

    def test_try_to_remove_from_cart_non_existing_product_raises(self):
        expected = f"No product with name {self.PRODUCT_NAME} in the cart!"
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.remove_from_cart(self.PRODUCT_NAME)
        self.assertEqual(expected, str(error.exception))

    def test_add_method_works_properly(self):
        self.shopping_cart = ShoppingCart("TestNameFirst", 100)
        self.shopping_cart2 = ShoppingCart("TestNameSecond", 200)
        self.shopping_cart.add_to_cart("bread", 5)
        self.shopping_cart2.add_to_cart("eggs", 2)

        new_shopping_cart = self.shopping_cart.__add__(self.shopping_cart2)
        self.assertEqual("TestNameFirstTestNameSecond", new_shopping_cart.shop_name)
        self.assertEqual(300, new_shopping_cart.budget)
        self.assertEqual({"bread": 5, "eggs": 2}, new_shopping_cart.products)

    def test_buy_products_successfully(self):
        self.shopping_cart.add_to_cart("bread", 5)
        self.shopping_cart.add_to_cart("eggs", 2)
        total_sum = 7
        expected = f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'
        self.assertEqual(expected, self.shopping_cart.buy_products())

    def test_buy_products_not_enough_budget_raises(self):
        self.shopping_cart.add_to_cart("bread", 99)
        self.shopping_cart.add_to_cart("eggs", 2)
        overbudget = sum(self.shopping_cart.products.values()) - self.BUDGET
        expected = f"Not enough money to buy the products! Over budget with {overbudget:.2f}lv!"
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.buy_products()
        self.assertEqual(expected, str(error.exception))


if __name__ == "__main__":
    main()
