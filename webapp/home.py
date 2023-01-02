import justpy as jp
from webapp import default_layout

"""Visit https://quasar.dev and https://tailwindcss.com to see all the info about styling.
a=div means thats the grid will be on top of div which has a=wp main gray background.
a=div1 means that all of the objects are placed on div1 which is a=div which is a=wp. 
No comma for tailwind, just use space with classes=""
For Quasar put QDiv.
Classes only change the styling. Actions are controled by functions, eg: Button. 
! click=sum_up without () !
Click and mouseenter are the same thing!
Quasar is more advanced but supports Tailwind. Just write tailwind=True
"""


class Home:
    path = "/home"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = default_layout.DefaultLayout(a=wp, view="hHh lpR fFf")

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-300 h-screen p-2")
        jp.Div(a=div, text="This is the Home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud exercitation ullamco 
                laboris nisi ut aliquip ex ea commodo consequat. 
                Duis aute irure dolor in reprehenderit in voluptate velit esse 
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
                sunt in culpa qui officia deserunt mollit 
                anim id est laborum.""", classes="text-lg")
        return wp
