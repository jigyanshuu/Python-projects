
import tkinter as tk
import ast
import operator


# Safe mathematical expression evaluator

def evaluate_expression(expression):

    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow
    }

    def evaluate(node):

        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        elif isinstance(node, ast.Constant):
            if type(node.value) not in (int, float):
                raise ValueError("Invalid number")
            return node.value

        elif isinstance(node, ast.BinOp):
            operation = operations.get(type(node.op))

            if operation is None:
                raise ValueError("Invalid operator")

            return operation(
                evaluate(node.left),
                evaluate(node.right)
            )

        elif isinstance(node, ast.UnaryOp):
            value = evaluate(node.operand)

            if isinstance(node.op, ast.USub):
                return -value

            elif isinstance(node.op, ast.UAdd):
                return value

            raise ValueError("Invalid operation")

        else:
            raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree)


# Button functions

def append_to_display(value):
    current = display.get()

    if current == "Error":
        current = ""

    display.set(current + str(value))


def clear_display():
    display.set("")


def delete_last():
    current = display.get()
    display.set(current[:-1])


def calculate():

    expression = display.get()

    try:
        if not expression:
            return

        result = evaluate_expression(expression)

        if isinstance(result, complex) or not isinstance(result, (int, float)):
            raise ValueError("Invalid result")

        display.set(str(result))

    except ZeroDivisionError:
        display.set("Cannot divide by zero")

    except (ValueError, SyntaxError, TypeError, OverflowError):
        display.set("Error")


# Keyboard support

def handle_keypress(event):

    key = event.char

    if key in "0123456789.+-*/()%":
        append_to_display(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        delete_last()

    elif event.keysym == "Escape":
        clear_display()


# Main window

root = tk.Tk()

root.title("Python Calculator")
root.geometry("340x470")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

display = tk.StringVar()

# Display screen

display_box = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 24),
    justify="right",
    state="readonly",
    readonlybackground="#313244",
    fg="white",
    bd=0
)

display_box.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=15
)


# Calculator buttons

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["(", ")", "DEL", "C"],
    ["="]
]


# Button layout

for row in buttons:

    button_frame = tk.Frame(root, bg="#1e1e2e")
    button_frame.pack(expand=True, fill="both", padx=8)

    for value in row:

        if value == "=":
            command = calculate
            color = "#a6e3a1"

        elif value == "C":
            command = clear_display
            color = "#f38ba8"

        elif value == "DEL":
            command = delete_last
            color = "#fab387"

        else:
            command = lambda v=value: append_to_display(v)
            color = "#45475a"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="#1e1e2e" if color != "#45475a" else "white",
            relief="flat",
            command=command
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )


# Enable keyboard controls

root.bind("<Key>", handle_keypress)

# Start application

root.mainloop()
