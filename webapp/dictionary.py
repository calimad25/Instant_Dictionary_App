import justpy as jp
import definition
from webapp import default_layout
from webapp import abstract
import requests


class Dictionary(abstract.AbstractPage):
    path = "/dictionary"

    @classmethod  # automatically Pycharm suggests cls instead of self
    def serve(cls, req):  # cls === class, same as self, just a convention request parameter for justpy
        wp = jp.QuasarPage(tailwind=True)

        lay = default_layout.DefaultLayout(a=wp, view="hHh lpR fFf")

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-300 h-screen")
        jp.Div(a=div, text="Instance English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you write.")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type in a word here ...", output=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 "
                                     "focus:outline-none focus:border-purple-500 "
                                     "py-2 px-4")
        input_box.on('input', cls.get_definition)

        # print(cls, req)

        return wp

    # @staticmethod  # method inside a class that behaves like a function
    # def get_definition(widget, msg):
    #     """@staticmethod does not expect as argument an instance of a class"""
    #     defined = definition.Definition(widget.value).get()
    #     widget.output.text = "".join(defined)  # so it shows as strings and not a tuple


    @staticmethod
    def get_definition(widget, msg):
        """Using the API created in 08_Instant_Dictionary_API. Need to import requests for this"""
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = req.json()

        widget.output.text = "".join(data["definition"])


"""
If you print(self) you will get the request from an instance object created by justpy. 
If @classmethod than it prints the Dictionary class.
If you use req then you get both the class and the request. With print(self, req)

===> <class 'webapp.dictionary.Dictionary'> <starlette.requests.Request object at 0x00000139680E5C60>

Just like About(). Dictionary is not an object instance so if you call the instance method it will 
show an error. But if you make it a class method, with @classmethod, then it's ok.
See @classmethod explication below.
"""

"""
class D:
    def serve(self):
        print(self)
D().serve()  === instance object
<__main__.D object at 0x0000025DC9D2E0B0>
D.serve()  === just the class
Traceback (most recent call last):
  File "C:/Users/40745/AppData/Local/Programs/Python/Python310/lib/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
TypeError: D.serve() missing 1 required positional argument: 'self'
class D:
    @classmethod
    def serve(self):
        print(self)
D.serve()  === still no () on D, just the class, but works because it a class method and not an instance method
<class '__main__.D'>
"""
