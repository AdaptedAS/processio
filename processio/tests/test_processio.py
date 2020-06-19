from time import sleep
from unittest import TestCase

from processio import ProcessIO, ParseIO

random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def calculate_list(data):
    total = 0
    for num in data:
        total += num

    return total


def function1():
    return True


def function2(var):
    return var


def function3(var1, var2, var3):
    return var1 + var2 + var3


def function4():
    sleep(3)
    return 'Hello'


def function5(var1, var2, var3, num1=0, num2=0):
    return var1 + var2 + var3 + num1 + num2


def function6():
    sleep(10)
    return 'Hello'


class TestProcessIO(TestCase):
    def test_with_no_var(self):
        run = ProcessIO(function1)
        result = run.result()
        self.assertEqual(result, True)

    def test_with_one_var(self):
        run = ProcessIO(function2, 'Hello')
        result = run.result()
        self.assertEqual(result, 'Hello')

    def test_with_more_vars(self):
        run = ProcessIO(function3, 1, 2, 3)
        result = run.result()
        self.assertEqual(result, 6),

    def test_with_vars_and_kwargs(self):
        run = ProcessIO(function5, 1, 2, 3, num1=5, num2=5)
        result = run.result()
        self.assertEqual(result, 16)


class TestProcessIOWorkingStatus(TestCase):
    def test_processio_status(self):
        run = ProcessIO(function4)
        sleep(1)

        status = run.doing_work()
        self.assertEqual(status, True)

        result = run.result()
        self.assertEqual(result, 'Hello')


class TestParseIOWorkingStatus(TestCase):
    def test_parseio_result(self):
        run = ParseIO(calculate_list, random_list, processes=2)
        result = run.result()

        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 2)

        total = 0
        for numbers in result:
            total += numbers

        self.assertEqual(int(total), 210)

