import tkinter as tk
from datetime import datetime, timedelta


class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x150")

        self.is_running = False
        self.start_time = 0

        self.label = tk.Label(root, text="00:00.000", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            root, text="Reset", command=self.reset_stopwatch, state=tk.DISABLED
        )
        self.reset_button.pack(side=tk.RIGHT, padx=10)

    def start_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(text="Start")
            self.reset_button.config(state=tk.NORMAL)
        else:
            self.is_running = True
            self.start_button.config(text="Stop")
            self.start_time = datetime.now()
            self.update_timer()

    def update_timer(self):
        if self.is_running:
            elapsed_time = datetime.now() - self.start_time
            self.label.config(text=str(elapsed_time)[:-3])
            self.root.after(10, self.update_timer)

    def reset_stopwatch(self):
        self.is_running = False
        self.start_button.config(text="Start")
        self.label.config(text="00:00.000")
        self.reset_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
