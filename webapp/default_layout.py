import justpy as jp

"""The kwargs work like a dictionary. 
Ex: kwargs = {"a": wp, "view": "hHh lpR fFf"}
"""


class DefaultLayout(jp.QLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # initialise the parent class. super = jp.QLayout

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left",
                            bordered=True)
        a_classes = "p-2 m-2 test-lg text-blue-400 hover:text-blue-700"
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")  # so that the button is in front of text

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value is True:
            widget.drawer.value = False
        else:
            widget.drawer.value = True