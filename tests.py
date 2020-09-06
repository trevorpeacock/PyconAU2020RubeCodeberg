import first_program
import bs4
import unittest


def test_char(s):
    """
    Take an XML string, and decode it.
    :param s: string containing XML character representation
    :return: numeric value
    """
    soup = bs4.BeautifulSoup(s, 'lxml')
    return first_program.get_ascii_char(soup)


class TestStringMethods(unittest.TestCase):

    def test_0(self):
        self.assertEqual(test_char(''), 0)

    def test_1(self):
        self.assertEqual(test_char('<count/>'), 1)

    def test_2(self):
        self.assertEqual(test_char('<count/><count/>'), 2)
        self.assertEqual(test_char('<count><count/></count>'), 2)

    def test_3(self):
        self.assertEqual(test_char('<count/><count/><count/>'), 3)
        self.assertEqual(test_char('<count/><count><count/></count>'), 3)

    def test_4(self):
        self.assertEqual(test_char('<count/><count/><count/><count/>'), 4)
        self.assertEqual(test_char('<count/><count/><count><count/></count>'), 4)
        self.assertEqual(test_char('<count><count/></count><count><count/></count>'), 4)
        self.assertEqual(test_char('<count><count/><count/></count>'), 4)
        self.assertEqual(test_char('<count><count><count/></count></count>'), 4)

    def test_6(self):
        self.assertEqual(test_char('<count><count/><count><count/></count></count>'), 6)
        self.assertEqual(test_char('<count><count/></count><count><count><count/></count></count>'), 6)

    def test_8(self):
        self.assertEqual(test_char('<count><count><count><count/></count></count></count>'), 8)


if __name__ == '__main__':
    unittest.main()
