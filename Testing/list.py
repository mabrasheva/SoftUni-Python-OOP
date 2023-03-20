class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_integer_list_is_initialized_correctly(self):
        integer_list = IntegerList(1, 2)
        self.assertEqual([1, 2], integer_list._IntegerList__data)

    def test_integer_list_is_not_initialized_correctly(self):
        integer_list = IntegerList("1", 2.5, True)
        self.assertEqual([], integer_list._IntegerList__data)

    def test_get_data(self):
        integer_list = IntegerList(1, 2)
        self.assertEqual([1, 2], integer_list.get_data())

    def test_add_integer(self):
        integer_list = IntegerList(1, 2)
        integer_list.add(3)
        self.assertEqual([1, 2, 3], integer_list._IntegerList__data)

    def test_add_not_integer_raises(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(ValueError) as error:
            integer_list.add("3")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_remove_valid_index(self):
        integer_list = IntegerList(1, 2)
        integer_list.remove_index(0)
        self.assertEqual([2], integer_list._IntegerList__data)

    def test_remove_not_valid_index(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(IndexError) as error:
            integer_list.remove_index(2)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_valid_index(self):
        integer_list = IntegerList(1, 2)
        integer_list.get(0)
        self.assertEqual(1, integer_list._IntegerList__data[0])

    def test_get_not_valid_index(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(IndexError) as error:
            integer_list.get(2)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_valid_element_on_valid_index(self):
        integer_list = IntegerList(1, 2)
        integer_list.insert(0, 0)
        self.assertEqual([0, 1, 2], integer_list._IntegerList__data)

    def test_insert_not_valid_element_on_valid_index(self):
        integer_list = IntegerList(1, 2)

        with self.assertRaises(ValueError) as error:
            integer_list.insert(0, "0")
        self.assertEqual("Element is not Integer", str(error.exception))

        with self.assertRaises(ValueError) as error:
            integer_list.insert(0, 5.5)
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_valid_element_on_not_valid_index(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(IndexError) as error:
            integer_list.insert(2, 0)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_biggest(self):
        integer_list = IntegerList(1, 2, -5, 100, -6)
        self.assertEqual(100, integer_list.get_biggest())

    def test_get_index_of_element(self):
        integer_list = IntegerList(1, 2)
        self.assertEqual(0, integer_list.get_index(1))


if __name__ == "__main__":
    main()
