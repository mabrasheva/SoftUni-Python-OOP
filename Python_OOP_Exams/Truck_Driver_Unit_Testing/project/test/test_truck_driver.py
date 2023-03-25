from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TruckDriverTests(TestCase):
    NAME = "Test Name"
    MONEY_PER_MILE = 10
    CARGO_LOCATION_1 = "Sofia"
    CARGO_LOCATION_2 = "Plovdiv"
    CARGO_MILES_1 = 100
    CARGO_MILES_2 = 200

    def setUp(self) -> None:
        self.driver = TruckDriver(self.NAME, self.MONEY_PER_MILE)

    def test_init(self):
        self.assertEqual(self.NAME, self.driver.name)
        self.assertEqual(self.MONEY_PER_MILE, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as error:
            self.driver.earned_money = -1
        self.assertEqual(f"{self.NAME} went bankrupt.", str(error.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.00000000001
        self.driver.add_cargo_offer(self.CARGO_LOCATION_1, 10000)
        with self.assertRaises(ValueError) as error:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(f"{self.NAME} went bankrupt.", str(error.exception))

    def test_earned_money_equal_to_zero(self):
        self.driver.earned_money = 0
        self.assertEqual(0, self.driver.earned_money)

    def test_add_cargo_offer_added_properly(self):
        expected_result = f"Cargo for {self.CARGO_MILES_1} to {self.CARGO_LOCATION_1} was added as an offer."
        self.assertEqual(expected_result, self.driver.add_cargo_offer(self.CARGO_LOCATION_1, self.CARGO_MILES_1))
        self.assertEqual(self.CARGO_MILES_1, self.driver.available_cargos[self.CARGO_LOCATION_1])

    def test_add_existing_cargo_offer_raises(self):
        self.driver.add_cargo_offer(self.CARGO_LOCATION_1, self.CARGO_MILES_1)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer(self.CARGO_LOCATION_1, self.CARGO_MILES_1)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer_works_properly(self):
        self.driver.add_cargo_offer(self.CARGO_LOCATION_1, self.CARGO_MILES_1)
        self.driver.add_cargo_offer(self.CARGO_LOCATION_2, self.CARGO_MILES_2)
        expected_string = f"{self.NAME} is driving {self.CARGO_MILES_2} to {self.CARGO_LOCATION_2}."

        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        expected_earned_money = self.driver.earned_money + (self.CARGO_MILES_2 * self.MONEY_PER_MILE)
        expected_miles = self.driver.miles + self.CARGO_MILES_2
        self.assertEqual(expected_string, self.driver.drive_best_cargo_offer())
        self.assertEqual(expected_earned_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

        expected_earned_money = self.driver.earned_money + (self.CARGO_MILES_2 * self.MONEY_PER_MILE)
        expected_miles = self.driver.miles + self.CARGO_MILES_2
        self.assertEqual(expected_string, self.driver.drive_best_cargo_offer())
        self.assertEqual(expected_earned_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

    def test_drive_best_cargo_offer_and_no_offers_available(self):
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_check_for_activities(self):
        miles = 2000
        self.driver.earned_money = 1000
        self.driver.check_for_activities(miles)
        self.assertEqual(self.driver.earned_money, 250)

    def test_eat(self):
        self.driver.earned_money = 1000
        self.driver.eat(2000)
        self.assertEqual(980, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(2000)
        self.assertEqual(955, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(3000)
        self.assertEqual(500, self.driver.earned_money)

    def test_repair_trunk(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(100000)
        self.assertEqual(2500, self.driver.earned_money)

    def test_repr_method(self):
        miles = 1000
        self.driver.miles = miles
        expected_string = f"{self.NAME} has {miles} miles behind his back."
        self.assertEqual(expected_string, repr(self.driver))


if __name__ == "__main__":
    main()

