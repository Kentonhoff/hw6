import re
import unittest

def sumNums(fileName):
    hand = open(fileName)
    totalsum = 0
    for line in hand:
        line = line.rstrip()
        nums = re.findall('[0-9]+', line)

        for num in nums:
            totalsum += int(num)
    hand.close()
    return totalsum

    pass

def countWord(fileName, word):
    text = word
    hand = open(fileName)
    wordcount = 0
    for line in hand:
        line = line.rstrip()

        lstofwords = re.findall(r"\b[A-Z]?[a-z]+\b", line)

        for wrd in lstofwords:
            if wrd.lower() == text:
                wordcount +=1
            else:
                wordcount = wordcount
    hand.close()

    return wordcount

    pass

def listURLs(fileName):
    hand = open(fileName)

    lstURL = []
    for line in hand:
        line = line.rstrip()
        URLS = re.findall(r"\S+\.\S+\.\w+", line)
        for Url in URLS:
            lstURL.append(Url)
    hand.close()

    return lstURL

    pass

class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
