"""rmvtag"""
# def tag(input_string):
#     """tag"""
#     inside_tag, word, result = False, "", []
#     for char in input_string:
#         if char == '<':
#             inside_tag = True
#             if word:
#                 result.append(word)
#                 word = ""
#         elif char == '>':
#             inside_tag = False
#         elif not inside_tag:
#             if char.isalnum() or char == '.' :
#                 word += char
#             else:
#                 if word:
#                     result.append(word)
#                     word = ""
#                 if char not in " \t\n":
#                     result.append(char)
#     if word:
#         result.append(word)
#     print(result)
# tag(input())
import re
def extract_words(html):
    """import re is da best for string"""
    text = re.sub(r'<.*?>', ' ', html)
    print(text.split())
extract_words(input())
