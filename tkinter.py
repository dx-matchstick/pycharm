import tkinter

from tkinter import *

import requests
import json


class Chatbot(Frame):
    """
    Class definition to hold our basic chatbot interaction window.
    """

    def __init__(self, parent=None, **kw):
        """
        Minimal init function for the Chatbot definition. Sets some variables, places some Tkinter widgets.
        """
        Frame.__init__(self, parent, kw)
        self.chatstr = StringVar()
        self.saystr = StringVar()
        self.make_widget()
        self.pack(fill=BOTH, expand=1)

    def make_widget(self):
        """ Make the chat label widget, the input wiget, the send button and the learn button."""
        chatbox = Label(self, textvariable=self.chatstr, justify=LEFT)
        chatbox.place(x=0, y=50)

        user_input = Entry(self, width=300)
        user_input.delete(0, END)
        user_input.insert(0, "startup")
        user_input.place(x=0, y=0)
        user_input.bind("<Return>",
                        lambda event,
                        input_box=user_input,
                        output=self.chatstr: self.send_to_server_get(input_box, output))

        send_button = Button(self,
                             text="Send",
                             command=lambda: self.send_to_server_post(input_box=user_input, output=self.chatstr))
        send_button.place(x=0, y=25)

    def send_to_server_get(self, input_box, output):
        input_string = str(input_box.get())
        try:
            url = "PUT URL HERE"
            payload = "{\n\t\"reply\": \"" + input_string + "\"\n}"
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            if response.status_code != 200:
                print("The POST failed.")
                reply_string = ""
                pass
            else:
                print("The POST succeeded.")
                reply_string = ""
                pass
        except Exception as e:
            print("The POST caused an exception: {}".format(e))
            reply_string = ""
            pass
        chat_box_text = str(output.get()) + "\nUser: {}\n\tBot: {}".format(input_string, reply_string)
        output.set(chat_box_text)

    def send_to_server_post(self, input_box, output):
        input_string = str(input_box.get())
        try:
            url = "PUT URL HERE {}".format(input_string)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers)
            if response.status_code != 200:
                print("The POST failed.")
                reply_string = ""
                pass
            else:
                print("The POST succeeded.")
                reply_string = ""
                pass
        except Exception as e:
            print("The POST caused an exception: {}".format(e))
            reply_string = ""
            pass
        chat_box_text = str(output.get()) + "\nUser: {}\n\tBot: {}".format(input_string, reply_string)
        output.set(chat_box_text)


def main():

    root = Tk()
    root.geometry("600x500")
    Chatbot(root)
    root.mainloop()


if __name__ == '__main__':
    main()