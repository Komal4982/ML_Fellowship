import textwrap
str1 = "The textwrap module can be used for wrapping and formatting of plain text. This module provides formatting of"\
       " text by adjusting the line breaks in the input paragraph."

print(textwrap.fill(str1, width=50))
