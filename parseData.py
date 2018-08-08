#!/usr/bin/env python3


__author__ = "Sid Sachdev"


import os

# To test the code, please replace the directory using pwd on your console
# Please make sure all the files are in given directory
directory = "/Users/Sidd/PycharmProjects/h1"


class Solution:
    def truthCounter(text):
        """
        Helper Function
        :param: *.txt File provided by the main function
        :return: If the book has more than 2 occurrences of the word "truth", it'll return the title of the book
        :rtype: list
        :except: Certain files aren't in UTF-8 format: Will return File Invalid
        """
        try:
            f = open(text, "r")
            counter = 0
            for lines in f.readlines():
                while counter <= 2:
                    if "truth" in lines:
                        x = lines.find("truth") + 5
                        if lines[x].isalpha():
                            # Edge case for words like "truthful != truth"
                            pass
                        else:
                            # Found the word truth
                            counter += 1
                    break
            return Solution.getTitle(text)
        except:
            return "File Invalid"

            # print(truthCounter("399-0.txt"))

    def getReleaseDate(text):
        """
        Helper Function
        :param: *.txt File provided by the main function
        :return: Returns the year of the release date
        :rtype: Integer
        :except: Certain files aren't in UTF-8 format: Will return File Invalid

        The function will look for the year by looking for a len == 4 string
        It'll convert the string into an integer, if successful, it's a year integer
        """
        try:
            f = open(text, "r")
            for lines in f.readlines():
                if "Release Date: " in lines:
                    for i in lines.split():
                        if len(i) == 4:
                            try:
                                n = int(i)
                                return n
                            except:
                                pass
            return -1
        except:
            return -2

    # print(averageReleaseDate("794-0.txt"))

    def getLanguage(text):
        """
        Helper Function
        :param: *.txt File provided by the main function
        :return: Will return the Language of the book
        :rtype: String
        :except: Certain files aren't in UTF-8 format: Will return File Invalid

        The function will look for the Language keyword, iterate over it and return the value
        If the book begins without finding the title, it will return without having to iterate of the rest of the book

        """
        try:
            f = open(text, "r")
            for lines in f.readlines():
                if "Language: " in lines:
                    x = lines.split(": ")
                    return x[1]
                elif "*** START OF" in lines:
                    return
        except:
            pass

    # print(getLanguage("794-0.txt"))

    def getTitle(text):
        """
        Helper Function
        :param: *.txt File provided by the main function
        :return: Will return the Title of the book
        :rtype: String
        :except: Certain files aren't in UTF-8 format: Will return File Invalid

        Function will break as it finds the title without having to iterate through the book
        With the colon as the delimiter, the function returns the rest of the field as the name

        """
        try:
            f = open(text, "r")
            for lines in f.readlines():
                if "Title: " in lines:
                    x = lines.split(": ")
                    return x[1:]
        except:
            return text

    # print(getTitle("794-0.txt"))




    def getLength(text):
        """
        Helper Function
        :param: *.txt File provided by the main function
        :return: Will Length the Length of the book and the name
        :rtype: Tuple
        :except: Certain files aren't in UTF-8 format: Will return File Invalid

        Counter begins at "START OF" and goes until "END OF"
        Lines that are just whitespace are neglected
        Instead of counting each character, the function counts the lines in the book for time complexity

        """
        try:
            f = open(text, "r")
            counter = 0
            for lines in f.readlines():
                if "*** END OF" not in lines:
                    if "*** START OF" in lines:
                        counter = 0
                    if lines == "\n":
                        counter -= 1
                    counter += 1
                else:
                    break
            return Solution.getTitle(text), counter
        except:
            return text, 0

    def getDialog(text):
        """
        Helper Function
        :param: *.txt File provided by the main function
        :return: Will return the number of dialogues of the book and the name
        :rtype: Tuple
        :except: Certain files aren't in UTF-8 format: Will return File Invalid


        This function would count the beginning quotes of each book
        If there's an open quote, there's no need to check for a closed quote as a dialogue has begun
        Edge case is a different type of quotation mark

        """
        try:
            f = open(text, "r")
            counter = 0
            for lines in f.readlines():
                if "*** END OF" not in lines:
                    if "“" in lines:
                        counter += 1
                    if "‘" in lines:
                        counter += 1
                else:
                    break
            return Solution.getTitle(text), counter
        except:
            return text, 0

    def longestBook(directory):
        """
        Main Function
        :param: Directory of the location of the files
        :return: Will return the longest book and its length
        :rtype: Tuple

        The function will iterate over the books using the helper function
        It'll only update the maxVal and finalName values if it finds a book with a bigger maxVal

        """
        maxVal = 0
        finalName = ""
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                tupleVal = Solution.getLength(filename)
                tempVal = tupleVal[1]
                tempName = tupleVal[0]
                if tempVal > maxVal:
                    maxVal = tempVal
                    finalName = tempName
        return finalName, maxVal

    def longestDialog(directory):
        """
        Main Function
        :param: Directory of the location of the files
        :return: Will return the book with the most dialogues and its count
        :rtype: Tuple

        The function will iterate over the books using the helper function
        Similarly to the longest book, it'll only update maxVal and finalName if it finds a book with a higher maxVal

        """
        maxVal = 0
        finalName = ""

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                tupleVal = Solution.getDialog(filename)
                tempVal = tupleVal[1]
                tempName = tupleVal[0]
                if tempVal > maxVal:
                    maxVal = tempVal
                    finalName = tempName
        return finalName, maxVal

    def averageCalculator(directory):
        """
        Main Function
        :param: Directory of the location of the files
        :return: Will return the average release date and most common release date
        :rtype: Tuple

        Using the helper function, it'll get the release year of the book. A simple average calculator followed by
        a dictionary to count the number of times each release year occurs and returns the max value of the dict

        """

        bookCounter = 0
        yearTotal = 0
        count = {}
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                yearNumber = Solution.getReleaseDate(filename)
                if yearNumber != -1 and yearNumber != -2:
                    yearTotal += yearNumber
                    bookCounter += 1

                    if yearNumber in count:
                        count[yearNumber] += 1
                    else:
                        count[yearNumber] = 1

                else:
                    pass

        return yearTotal // bookCounter, max(count, key=count.get)

    def getTruthBooks(directory):
        """
        Main Function
        :param: Directory of the location of the files
        :return: Will return all the list of the names with the word truth occurring more than twice
        :rtype: lists

        Using the helper function truthCounter()

        """
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                print(Solution.truthCounter(filename))

    def ratioLanguage(directory):
        """
        Main Function
        :param: Directory of the location of the files
        :return: Will return a tuple of the
        :rtype: tuple

        Using the helper function getLanguage()
        If the language is English, the counter for the numerator will go up
        Else, the denominator

        """

        numerator = 0
        denominator = 0
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                if Solution.getLanguage(filename) == "English\n":
                    numerator += 1
                elif Solution.getLanguage(filename) != "English\n" and Solution.getLanguage(filename) != None:
                    denominator += 1

        return numerator // denominator, ":", 1


if __name__ == "__main__":
    print("--------------------------------------- List of Books -------------------------------------")
    ("List of books with the word truth (2x): ", Solution.getTruthBooks(directory))
    print("-------------------------------------------------------------------------------------------")
    print("Average Release Date and Most Common Release Date: ", Solution.averageCalculator(directory))
    print("-------------------------------------------------------------------------------------------")
    print("Ratio English/Other Language (Approximately): ", Solution.ratioLanguage(directory))
    print("-------------------------------------------------------------------------------------------")
    print("Book with the most Dialog between characters: ", Solution.longestDialog(directory))
    print("-------------------------------------------------------------------------------------------")
    print("Longest Book: ", Solution.longestBook(directory))
    print("-------------------------------------------------------------------------------------------")
