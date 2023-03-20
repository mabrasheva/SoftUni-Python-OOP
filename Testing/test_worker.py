class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_initialized_correctly(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)

    def test_energy_is_incremented_after_rest(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_worker_cannot_work_with_negative_energy_raises(self):
        worker = Worker("Test", 100, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_cannot_work_with_zero_energy_raises(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_money_are_increased_after_work(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_work(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(9, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test has saved 0 money.", worker.get_info())


if __name__ == "__main__":
    main()
