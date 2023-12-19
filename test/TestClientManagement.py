import unittest
from dao.ClientDAO import ClientDAO


class MyTestCase(unittest.TestCase):
    # SET UP
    def setUp(self):
        print("Set Up")
        self.obj1 = ClientDAO()

    # TEST CLIENT IS ADDED OR NOT
    def test_add_client(self):
        print("test_add_client")
        result = self.obj1.add_client()
        self.assertEqual(result, True)

    def test_add_client_exception(self):
        print("test_add_client_exception")
        result = self.obj1.add_client()
        self.assertRaises(Exception, result)

    # TEAR DOWN
    def tearDown(self):
        print("Tear Down")


if __name__ == '__main__':
    unittest.main()
