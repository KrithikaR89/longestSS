""" LeetCode Q 5: Given a string s, return the longest palindromic substring in s."""

import datetime
import logging


class LongestPalindromicSubString:
    """ This class contains methods to find longest palindromic substring """

    def __init__(self):
        format_used = logging.Formatter('%(asctime)s - %(lineno)d - %(message)s', datefmt='%D %I:%M:%S %p')

        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)

        self.streamer = logging.StreamHandler()
        self.streamer.setFormatter(format_used)
        self.streamer.setLevel(logging.INFO)
        self.log.addHandler(self.streamer)

        ts = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S%p')
        self.file_handler = logging.FileHandler(f'Result_{ts}.log')
        self.file_handler.setFormatter(format_used)
        self.file_handler.setLevel(logging.INFO)
        self.log.addHandler(self.file_handler)

        self.log.propagate = False

        self.log.info(f"Starting Sequence - {ts}")

    def process_child_list(self, child_list, subset_dict):
        """
        This method takes a number & generates all combinations of parentheses
        :param child_list: Input list needing to be processed
        :param subset_dict : Rolling dictionary of values
        :return:subset_dict : Updated dict with palindromic string & its length as key
        """
        reversed_child_list = list(reversed(child_list))

        if reversed_child_list == child_list:
            pal_string = ''.join(x for x in child_list)
            self.log.info(f"Found a subset palindromic match - {pal_string}, "
                          f"with length - {len(child_list)}")
            if pal_string not in subset_dict.values():
                subset_dict[len(child_list)] = pal_string
                self.log.info(f"Updated dictionary is : {subset_dict}")

        return subset_dict

    def find_palindromic_substring(self, string):
        """
        This method takes a number & generates all combinations of parentheses
        :param string: Input string needing to be checked
        :return:
        """
        conv_list = list(string)
        self.log.info(conv_list)
        subset_dict = {}

        if len(conv_list) < 2:
            self.log.info(f"Final string is : {''.join(x for x in conv_list)}")
            return ''.join(x for x in conv_list)

        if len(conv_list) == 2:
            if conv_list[0] != conv_list[1]:
                self.log.info(f"Final string is : {str(conv_list[0])}")
                return str(conv_list[0])
            else:
                self.log.info(f"Final string is : {''.join(x for x in conv_list)}")
                return ''.join(x for x in conv_list)

        for i in range(len(conv_list)):
            self.log.info(f"Holding element {conv_list[i]} in place... ")
            tmp = [conv_list[i]]
            self.log.info(f"Tmp dictionary at start is : {tmp}")
            for j in range(i+1, len(conv_list)):
                if conv_list[i] == conv_list[j]:
                    tmp.append(conv_list[j])
                    self.log.info(f"Found an end string match! Appending to child list")
                    child_list = tmp
                    subset_dict = self.process_child_list(child_list=child_list, subset_dict=subset_dict)

                    if conv_list[i] not in conv_list[j+1:]:
                        tmp = []
                else:
                    tmp.append(conv_list[j])
                    self.log.info(f"Added {conv_list[j]} to Tmp - {tmp}")

        self.log.info(subset_dict)

        if subset_dict:
            self.log.info(f"Longest found palindrome is {subset_dict[max(subset_dict.keys())]}")
            return subset_dict[max(subset_dict.keys())]

        self.log.info(f"No palindromic strings found, returning {conv_list[0]}")
        return conv_list[0]


if __name__ == '__main__':
    lss = LongestPalindromicSubString()
    lss.find_palindromic_substring(string='abnabbahtopp')


