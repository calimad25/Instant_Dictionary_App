"""A better structure than the one in .
A class for every webpage.
About() === object instance. About is just the class
=> if there was a __init__(self, path) method then the path was About(path)"""

import justpy as jp
from webapp import default_layout


class About:
    path = "/about"  # no need for __init__(self, path) cuz all users will have the same domain path

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = default_layout.DefaultLayout(a=wp, view="hHh lpR fFf")

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-300 h-screen")
        jp.Div(a=div, text="This is the About page", classes="text-4xl m-2")
        jp.Div(a=div, text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud exercitation ullamco 
                laboris nisi ut aliquip ex ea commodo consequat. 
                Duis aute irure dolor in reprehenderit in voluptate velit esse 
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
                sunt in culpa qui officia deserunt mollit 
                anim id est laborum.""", classes="text-lg")
        return wp
