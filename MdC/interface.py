import tkinter as tk
from tkinter import font

# Create the main application window
root = tk.Tk()
root.title("User Interface")
root.geometry("800x400")  # Adjust size as needed

# Define fonts
button_font = font.Font(size=10, weight='bold')

# Function to handle button actions (you can customize these as needed)
def button_action(button_name):
    print(f"{button_name} clicked")

# Left side buttons
for i in range(4):
    button = tk.Button(root, text=f"Bebida {i+1}", font=button_font, command=lambda i=i: button_action(f"Bebida {i+1}"))
    button.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")

# Right side buttons
for i in range(4):
    button = tk.Button(root, text=f"Bebida {i+5}", font=button_font, command=lambda i=i: button_action(f"Bebida {i+5}"))
    button.grid(row=i, column=2, padx=10, pady=5, sticky="nsew")

# Display area
display = tk.Label(root, text="DISPLAY", font=("Arial", 14), borderwidth=2, relief="solid")
display.grid(row=0, column=1, rowspan=4, padx=10, pady=5, sticky="nsew")

# Bottom buttons
encender_button = tk.Button(root, text="Encender", bg="green", fg="white", font=button_font, command=lambda: button_action("Encender"))
encender_button.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

tamaño1_button = tk.Button(root, text="Tamaño 1", font=button_font, command=lambda: button_action("Tamaño 1"))
tamaño1_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")

tamaño2_button = tk.Button(root, text="Tamaño 2", font=button_font, command=lambda: button_action("Tamaño 2"))
tamaño2_button.grid(row=4, column=1, padx=5, pady=5)

tamaño3_button = tk.Button(root, text="Tamaño 3", font=button_font, command=lambda: button_action("Tamaño 3"))
tamaño3_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

detener_button = tk.Button(root, text="Detener", fg="red", font=button_font, command=lambda: button_action("Detener"))
detener_button.grid(row=4, column=1, padx=10, pady=5, sticky="e")

apagar_button = tk.Button(root, text="Apagar", bg="red", fg="white", font=button_font, command=lambda: button_action("Apagar"))
apagar_button.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")

# Maintenance button
mantenimiento_button = tk.Button(root, text="Mantenimiento", bg="orange", font=button_font, command=lambda: button_action("Mantenimiento"))
mantenimiento_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Configure grid weights to make the layout responsive
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)

# Start the main loop
root.mainloop()
