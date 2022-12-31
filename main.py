import justpy as jp
from webapp.about import About
from webapp.home import Home

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)  # no About(). About() === object instance. About is just the class

jp.justpy(port=8001)  # to start the webpage with dif port from test_justpy
