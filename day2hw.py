paragraph = """Python is a high-level, interpreted programming language known for its readability and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python's extensive standard library and vibrant ecosystem of third-party packages make it suitable for a wide range of applications, from web development and data analysis to artificial intelligence and scientific computing. Its simple syntax and dynamic typing make it an excellent choice for both beginners and experienced developers."""
length = len(paragraph)
print("Length of the paragraph is:",length)
print("First character is:",paragraph[0])
print("Last character is:",paragraph[-1])
print("Preview :",paragraph[0:50])
replaced_para = paragraph.replace("Python","PYTHON")
print("\nReplaced paragraph is:\n",replaced_para)
lower_para = replaced_para.lower()
print("\nLowercase :\n",lower_para)
cleaned_para = lower_para.strip()
print("\nCleaned paragraph :\n",cleaned_para)
words = cleaned_para.split()
print("\nList of words :\n",words)
if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is not found in the paragraph.\n")
    message = "The course description is {} characters long and has {} words."
    print(message.format(len(cleaned_para),len(words)))
