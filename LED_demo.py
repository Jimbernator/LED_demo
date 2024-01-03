import tkinter as tk
import threading
import time
import random



class LEDControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Control App")

        # Initialize variables for LED states
        self.led_states = [0, 0, 0, 0]

        # Create LEDs
        self.led_labels = []
        for i in range(4):
            label = tk.Label(root, text=f"LED {i+1}", font=('Helvetica', 12))
            label.grid(row=i, column=0, padx=10, pady=10)
            self.led_labels.append(label)

        # Create Buttons
        self.button_labels = ['Button 1', 'Button 2', 'Button 3', 'Button 4']
        self.buttons = []
        for i in range(4):
            button = tk.Button(root, text=self.button_labels[i], command=lambda idx=i: self.toggle_led(idx))
            button.grid(row=i, column=1, padx=10, pady=10)
            self.buttons.append(button)

        # Start a thread for polling and updating LEDs
        self.polling_thread = threading.Thread(target=self.update_leds_thread, daemon=True)
        self.polling_thread.start()

    def update_leds_thread(self):
        while True:
            # Simulate updating LED states from memory
            self.led_states = [random.choice([0, 1]) for _ in range(4)]

            # Update LED labels on the GUI
            for i in range(4):
                if self.led_states[i] == 1:
                    self.led_labels[i].config(bg='green', fg='white')
                else:
                    self.led_labels[i].config(bg='red', fg='black')

            time.sleep(1)  # Adjust the sleep time based on your needs

    def toggle_led(self, idx):
        # Simulate sending control signal to the device
        if self.led_states[idx] == 0:
            print(f"Turning ON LED {idx + 1}")
        else:
            print(f"Turning OFF LED {idx + 1}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LEDControlApp(root)
    root.mainloop()
