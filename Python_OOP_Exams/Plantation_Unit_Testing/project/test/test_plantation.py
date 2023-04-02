from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTests(TestCase):
    SIZE = 2
    worker1 = "Worker1"
    worker2 = "Worker2"
    plant1 = "Plant1"
    plant2 = "Plant2"

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_negative_size_raises(self):
        size = -1
        with self.assertRaises(ValueError) as error:
            Plantation(size)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_successfully(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(f"{self.worker1} successfully hired.", self.plantation.hire_worker(self.worker1))
        self.assertEqual([self.worker1], self.plantation.workers)
        self.assertEqual(f"{self.worker2} successfully hired.", self.plantation.hire_worker(self.worker2))
        self.assertEqual([self.worker1, self.worker2], self.plantation.workers)

    def test_hire_duplicate_worker_raises(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(f"{self.worker1} successfully hired.", self.plantation.hire_worker(self.worker1))
        self.assertEqual([self.worker1], self.plantation.workers)

        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(self.worker1)
        self.assertEqual("Worker already hired!", str(error.exception))
        self.assertEqual([self.worker1], self.plantation.workers)

    def test_len_method(self):
        self.plantation.plants = {"A": ["1", "2"], "B": ["22"]}
        self.assertEqual(3, self.plantation.__len__())

    def test_planting_successfully(self):
        self.plantation.hire_worker(self.worker1)
        self.assertEqual([self.worker1], self.plantation.workers)

        self.assertEqual({}, self.plantation.plants)
        self.assertEqual(f"{self.worker1} planted it's first {self.plant1}.",
                         self.plantation.planting(self.worker1, self.plant1))
        self.assertEqual({self.worker1: [self.plant1]}, self.plantation.plants)

        self.assertEqual(f"{self.worker1} planted {self.plant2}.", self.plantation.planting(self.worker1, self.plant2))
        self.assertEqual({self.worker1: [self.plant1, self.plant2]}, self.plantation.plants)

    def test_planting_non_existing_worker_raises(self):
        self.assertEqual([], self.plantation.workers)
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(self.worker1, self.plant1)
        self.assertEqual(f"Worker with name {self.worker1} is not hired!", str(error.exception))
        self.assertEqual({}, self.plantation.plants)

    def test_planting_but_plantation_is_full_raises(self):
        plant3 = "Plant3"

        self.plantation.hire_worker(self.worker1)
        self.plantation.planting(self.worker1, self.plant1)
        self.plantation.planting(self.worker1, self.plant2)
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(self.worker1, plant3)
        self.assertEqual("The plantation is full!", str(error.exception))
        self.assertEqual({self.worker1: [self.plant1, self.plant2]}, self.plantation.plants)

    def test_str_method(self):
        self.plantation.hire_worker(self.worker1)
        self.plantation.planting(self.worker1, self.plant1)
        self.plantation.planting(self.worker1, self.plant2)

        expected_string = [f"Plantation size: {self.SIZE}", f'{", ".join(self.plantation.workers)}']
        for worker, plants in self.plantation.plants.items():
            expected_string.append(f"{worker} planted: {', '.join(plants)}")
        final_expected_string = '\n'.join(expected_string)
        self.assertEqual(final_expected_string, str(self.plantation))

    def test_repr_method(self):
        self.plantation.hire_worker(self.worker1)
        self.plantation.hire_worker(self.worker2)
        expected_result = f'Size: {self.SIZE}\n'
        expected_result += f'Workers: {self.worker1}, {self.worker2}'
        self.assertEqual(expected_result, repr(self.plantation))


if __name__ == "__main__":
    main()
