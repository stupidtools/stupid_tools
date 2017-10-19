

Ok, so, if you've ever decided to do translation of a site server side, you might have needed to use this.  Too bad you didn't find it then, huh?

Anyway, the idea is, if you have some html, and you want to replace some of the html with template variables, this script will help you compare the before and after and give you a nice dictionary maping {template_variables: original_text}.  Handy if you want to, say, put it into an excel file.


compare(orig, mod, begin_token, end_token)

orig is the orig html as a string.  mod is the modified html as a string.  begin token is the token that signifies the start of a template variable.  Guessing you can figure out what end token is.

so, for example, if we have this

x = """
```html
<html>
    <body>
        <h2> Hey </h2>
    </body>
</html>
```
"""


and we changed it to

y = """
```html
<html>
    <body>
        <h2> {{ stuff }} </h2>
    <body>
<html> 
```
"""



and we ran 

compare(x, y, '{{', '}}')


we would get: {'stuff':'Hey'}



A few things to note.

    - White space surrounding the text that changed to a variable gets removed.
    - There have to be at least 3 non-space characters between template variables ({{foo}} {{bar}} wont work)
    - This will probably break if you put a template variable at the very end of the template.






