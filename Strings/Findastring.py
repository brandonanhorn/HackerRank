import re

def count_substring(string, sub_string):
    re_sub = re.findall('(?=' + sub_string + ')', string)
    return(len(re_sub))
