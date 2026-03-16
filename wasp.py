import tkinter as tk
from tkinter import messagebox


class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")
        self.root.geometry("950x680")
        self.root.configure(bg="#0f172a")

        self.time_limit = 5
        self.time_left = self.time_limit
        self.timer_job = None
        self.writing_started = False

        self.build_ui()

    def build_ui(self):
        # Main container
        self.main_frame = tk.Frame(self.root, bg="#0f172a")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title = tk.Label(
            self.main_frame,
            text="Disappearing Text Writing App",
            font=("Segoe UI", 24, "bold"),
            fg="white",
            bg="#0f172a"
        )
        title.pack(pady=(10, 6))

        # Subtitle
        subtitle = tk.Label(
            self.main_frame,
            text="Keep typing. Stop for 5 seconds and everything disappears.",
            font=("Segoe UI", 11),
            fg="#cbd5e1",
            bg="#0f172a"
        )
        subtitle.pack(pady=(0, 18))

        # Status frame
        status_frame = tk.Frame(self.main_frame, bg="#0f172a")
        status_frame.pack(fill="x", pady=(0, 12))

        self.timer_label = tk.Label(
            status_frame,
            text=f"Time Left: {self.time_left}",
            font=("Segoe UI", 16, "bold"),
            fg="#f59e0b",
            bg="#0f172a"
        )
        self.timer_label.pack(side="left", padx=(0, 20))

        self.word_count_label = tk.Label(
            status_frame,
            text="Words: 0",
            font=("Segoe UI", 12, "bold"),
            fg="#38bdf8",
            bg="#0f172a"
        )
        self.word_count_label.pack(side="left", padx=(0, 20))

        self.char_count_label = tk.Label(
            status_frame,
            text="Characters: 0",
            font=("Segoe UI", 12, "bold"),
            fg="#a78bfa",
            bg="#0f172a"
        )
        self.char_count_label.pack(side="left")

        # Editor container
        editor_frame = tk.Frame(
            self.main_frame,
            bg="#1e293b",
            bd=0,
            highlightthickness=1,
            highlightbackground="#334155"
        )
        editor_frame.pack(fill="both", expand=True, pady=(0, 16))

        self.text_box = tk.Text(
            editor_frame,
            wrap="word",
            font=("Consolas", 14),
            bg="#f8fafc",
            fg="#0f172a",
            insertbackground="#0f172a",
            relief="flat",
            padx=18,
            pady=18,
            undo=True
        )
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)

        self.text_box.bind("<KeyPress>", self.on_typing)
        self.text_box.bind("<KeyRelease>", self.update_counts)

        # Button frame
        btn_frame = tk.Frame(self.main_frame, bg="#0f172a")
        btn_frame.pack(pady=(0, 10))

        reset_btn = tk.Button(
            btn_frame,
            text="Reset Timer",
            command=self.reset_app,
            font=("Segoe UI", 10, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2"
        )
        reset_btn.pack(side="left", padx=8)

        clear_btn = tk.Button(
            btn_frame,
            text="Clear Text",
            command=self.clear_text,
            font=("Segoe UI", 10, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2"
        )
        clear_btn.pack(side="left", padx=8)

    def on_typing(self, event=None):
        if not self.writing_started:
            self.writing_started = True
            self.start_countdown()

        self.time_left = self.time_limit
        self.update_timer_label()

    def start_countdown(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        self.countdown()

    def countdown(self):
        self.update_timer_label()

        if self.time_left <= 0:
            self.delete_all_text()
            return

        self.time_left -= 1
        self.timer_job = self.root.after(1000, self.countdown)

    def update_timer_label(self):
        self.timer_label.config(text=f"Time Left: {self.time_left}")

        if self.time_left <= 2:
            self.timer_label.config(fg="#ef4444")
        else:
            self.timer_label.config(fg="#f59e0b")

    def update_counts(self, event=None):
        content = self.text_box.get("1.0", tk.END).strip()

        if content:
            words = len(content.split())
            characters = len(content)
        else:
            words = 0
            characters = 0

        self.word_count_label.config(text=f"Words: {words}")
        self.char_count_label.config(text=f"Characters: {characters}")

    def delete_all_text(self):
        self.text_box.delete("1.0", tk.END)
        self.time_left = self.time_limit
        self.writing_started = False
        self.timer_job = None
        self.update_timer_label()
        self.update_counts()

        messagebox.showwarning(
            "Too Slow!",
            "You stopped typing for too long. All your text has been deleted."
        )

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)
        self.reset_app()
        self.update_counts()

    def reset_app(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.time_left = self.time_limit
        self.writing_started = False
        self.timer_label.config(text=f"Time Left: {self.time_left}", fg="#f59e0b")


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()