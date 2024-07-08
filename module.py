
# Module 
# Module is code written by somebody else and fun part is we can use it in our project
# pip install flask
# pip install --user flask
# pip install pyjokes --user

import pyjokes

joke = pyjokes.get_joke()
print(joke)
