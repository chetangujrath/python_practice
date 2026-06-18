"""""

Regular expressions are a powerful tool for searching and manipulating strings based on specific patterns. They allow you to define complex search criteria and can be used for tasks such as validating input, extracting information, and performing substitutions."""""

import re

text = """
this is the sample email address: chetan.gujrathi@gmail.com , chetangujrathi@yahoo.com, and 
mansigujrathi1993@gmail.com and sample mobile number 9096964559 and 8795463215 and 9876543210 and 
1234567890 and 987654321 and 12345678901
"""
text1 = "this is the sample data of school data for class 10th and 12th and 11th and 9th and 8th and " \
"7th and 6th and 5th and 4th and 3rd and 2nd and 1st"

class_data = re.findall(r'\b\d+(?:st|nd|rd|th)\b', text1)
mobile_number = re.findall(r'\b\d{10}\b', text)

list_of_email = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(list_of_email)
print(mobile_number)
print(class_data)