import inspect

import justpy as jp
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp import abstract

imports = list(globals().values())
# access all data from imported stuff and store them into a dictionary. Then we make it inta a list

for i in imports:
    if inspect.isclass(i):
        if issubclass(i, abstract.AbstractPage) and hasattr(i, "path"):
            jp.Route(i.path, i.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)  # no About(). About() === object instance. About is just the class
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)  # to start the webpage with dif port from test_justpy
