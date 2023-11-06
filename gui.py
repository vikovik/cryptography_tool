import tkinter as tk
from tkinter import messagebox
from cryptography_cesar import encoder_cesar, decoder_cesar
from cryptography_viginere import encoder_viginere, decoder_viginere

"""
    The function `clear_input_fields()` clears the contents of three input fields.
"""
def clear_input_fields():
    input_message.delete(0, "end")
    input_offset.delete(0, "end")
    input_key.delete(0, "end")

"""
    The function `clear_output_field()` clears the text in the output_text field.
"""
def clear_output_field():
    output_text.delete(1.0, "end")

"""
    The `exit_program` function clears the `output_text` widget and closes the program.
    :return: nothing (None).
"""
def exit_program():
    output_text.insert("end", "Exiting...")
    output_text.delete(1.0, "end")    
    root.destroy()
    return

"""
    The function `on_option_change` handles changes in the selected option and updates the visibility of
    input fields accordingly.
"""
def on_option_change(*args):
    selected_option = option_var.get()

    if selected_option in ["1", "2"]:
        input_offset.grid(row=8, column=1)
        offset_label.grid(row=8, column=0)
        key_label.grid_remove()
        input_key.grid_remove()
        
    elif selected_option in ["3", "4"]:
        input_offset.grid_remove()
        key_label.grid(row=9, column=0)
        input_key.grid(row=9, column=1) 
        offset_label.grid_remove()

    elif selected_option == "5":
        input_offset.grid_remove() 
        key_label.grid_remove()
        input_key.grid_remove()
        offset_label.grid_remove()

    clear_input_fields()
    clear_output_field()

"""
    The `perform_action` function takes user input and performs different actions based on the selected
    option.
    :return: nothing (None).
"""
def perform_action():
    selected_option = option_var.get()

    if selected_option == "1":
        message_encode_ces = input_message.get()
        offset_encode_ces = input_offset.get()

        if offset_encode_ces and offset_encode_ces.isnumeric():
            offset_encode_ces = int(offset_encode_ces)
            encoded_message = encoder_cesar(message_encode_ces, offset_encode_ces)
            output_text.delete(1.0, "end")
            output_text.insert("end", "Encoded message:\n" + encoded_message)

        else:
            messagebox.showerror("Error", "Invalid offset value")

    elif selected_option == "2":
        message_decode_ces = input_message.get()
        offset_decode_ces = input_offset.get()

        if offset_decode_ces and offset_decode_ces.isnumeric():
            offset_decode_ces = int(offset_decode_ces)
            decoded_message = decoder_cesar(message_decode_ces, offset_decode_ces)
            output_text.delete(1.0, "end")
            output_text.insert("end", "Decoded message:\n" + decoded_message)

        else:
            messagebox.showerror("Error", "Invalid offset value")

    elif selected_option == "3":
        message_encode_vig = input_message.get()
        key_encode_vig = input_key.get()

        if key_encode_vig and key_encode_vig.isalpha():
            encoded_message = encoder_viginere(message_encode_vig, key_encode_vig)
            output_text.delete(1.0, "end")
            output_text.insert("end", "Encoded message:\n" + encoded_message)

        else:
            messagebox.showerror("Error", "Invalid key")

    elif selected_option == "4":
        message_decode_vig = input_message.get()
        key_decode_vig = input_key.get()

        if key_decode_vig and key_decode_vig.isalpha():
            decoded_message = decoder_viginere(message_decode_vig, key_decode_vig)
            output_text.delete(1.0, "end")
            output_text.insert("end", "Decoded message:\n" + decoded_message)

        else:
            messagebox.showerror("Error", "Invalid key")

    elif selected_option == "5":
        message_brute_force = input_message.get()
        output_text.delete(1.0, "end")

        for offset in range(26):
            decoded_message = decoder_cesar(message_brute_force, offset)
            output_text.insert("end", "\nOffset: {offset}\nDecoded message: {decoded_message}\n".format(offset=offset, decoded_message=decoded_message))
    
    else:
        messagebox.showerror("Error", "Invalid option")

root = tk.Tk()
root.title("Cryptography Tool")

tk.Label(root, text="Choose what you want to do:\n").grid(row = 0, columnspan = 2)

option_var = tk.StringVar()
option_var.set("1")
options = [("Encode Cesar Cipher message", "1"), ("Decode Cesar Cipher message", "2"), ("Encode Viginere Cipher message", "3"), ("Decode Viginere Cipher message", "4"), ("Brute Force Cesar Cipher message", "5")]

for i, (text, value) in enumerate(options, start = 1):
  tk.Radiobutton(root, text=text, variable=option_var, value=value, command = on_option_change).grid(row=i, columnspan=2)

tk.Label(root, text="Enter a message: ").grid(row = 7, column = 0)
input_message = tk.Entry(root)
input_message.grid(row = 7, column = 1)

offset_label = tk.Label(root, text="Enter an offset value: ")
input_offset = tk.Entry(root)
input_offset.grid(row = 8, column = 1)

key_label = tk.Label(root, text="Enter a key:")
input_key = tk.Entry(root)

perform_button = tk.Button(root, text="Perform action", command=perform_action)
perform_button.grid(row = 10, column = 1)

exit_button = tk.Button(root, text="Exit Program", command=exit_program)
exit_button.grid(row = 10, column = 0)

output_text = tk.Text(root, height=10, width=50)
output_text.grid(row = 11, columnspan = 2)

on_option_change()

root.mainloop()