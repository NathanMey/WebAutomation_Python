import tkinter as tk

def input_with_button(prompt):
    # create a new tkinter window
    window = tk.Tk()
    window.title("Input with OK Button")

    # create a label to prompt the user for input
    prompt_label = tk.Label(window, text= prompt)
    prompt_label.pack()

    # create an input field
    input_field = tk.Entry(window)
    input_field.pack()

    # create a function to handle the button click event
    def handle_ok_button_click():
        global input_value
        input_value = input_field.get()
        window.destroy()  # close the window after getting the input value

    # create an "OK" button and attach the click event handler
    ok_button = tk.Button(window, text="OK", command=handle_ok_button_click)
    ok_button.pack()

    # start the tkinter event loop
    window.mainloop()

    # return the input value after the window is closed
    return input_value