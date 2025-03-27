"""
Timezone GUI Program with Dark Theme
Coded by Nico Kuehn
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import pytz

# Updated color definitions
BG_COLOR = "#2d2d2d"
TEXT_COLOR = "#FFA500"  # Orange text
BUTTON_COLOR = "#3d3d3d"
ACCENT_COLOR = "#FFA500"  # Orange accent
WATERMARK_COLOR = "#FFA500"

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z%z"

class TimezoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timezone Explorer")
        self.root.geometry("800x600")
        self.root.configure(bg=BG_COLOR)
        
        # Watermark
        self.watermark_label = tk.Label(
            root, 
            text="Coded by Nico Kuehn", 
            fg=WATERMARK_COLOR, 
            bg=BG_COLOR,
            font=("Arial", 8)
        )
        self.watermark_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Left panel for buttons
        left_frame = tk.Frame(self.root, bg=BG_COLOR)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
        
        # Function buttons
        buttons = [
            ("List All Timezones", self.list_all_timezones),
            ("Common Timezones", self.show_common_timezones),
            ("Current Times", self.show_current_time),
            ("Native to Aware", self.convert_unaware_datetime),
            ("Convert Zones", self.convert_between_zones),
            ("Ambiguous Time", self.handle_ambiguous_time),
            ("Fixed Offset", self.demonstrate_fixed_offset)
        ]
        
        for text, command in buttons:
            btn = tk.Button(
                left_frame, text=text, command=command,
                bg=BUTTON_COLOR, fg=ACCENT_COLOR, activebackground=ACCENT_COLOR,
                relief=tk.FLAT, font=("Arial", 10))
            btn.pack(fill=tk.X, pady=5)
        
        # Right panel for output
        self.output_area = scrolledtext.ScrolledText(
            self.root, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
            font=("Consolas", 10))
        self.output_area.pack(
            side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Configure text centering
        self.output_area.tag_configure("center", justify='center')
            
        # Clear button
        clear_btn = tk.Button(
            left_frame, text="Clear Output", command=self.clear_output,
            bg=BUTTON_COLOR, fg=ACCENT_COLOR, activebackground=ACCENT_COLOR,
            relief=tk.FLAT, font=("Arial", 10))
        clear_btn.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        
    def clear_output(self):
        self.output_area.delete(1.0, tk.END)
        
    def print_output(self, text):
        self.output_area.insert(tk.END, text + "\n", "center")
        self.output_area.see(tk.END)
        
    def list_all_timezones(self):
        self.clear_output()
        self.print_output("All Supported Timezones:\n" + "-"*40)
        for tz in pytz.all_timezones:
            self.print_output(f"• {tz}")
            
    def show_common_timezones(self):
        self.clear_output()
        self.print_output("Common Timezones:\n" + "-"*40)
        for tz in pytz.common_timezones:
            self.print_output(f"• {tz}")
            
    def show_current_time(self):
        self.clear_output()
        self.print_output("Current Global Times:\n" + "-"*40)
        locations = {
            'UTC': pytz.utc,
            'India (Kolkata)': 'Asia/Kolkata',
            'New York': 'America/New_York',
            'Paris': 'Europe/Paris',
            'Tokyo': 'Asia/Tokyo'
        }
        
        for name, zone in locations.items():
            try:
                tz = pytz.timezone(zone) if isinstance(zone, str) else zone
                now = datetime.now(tz)
                self.print_output(
                    f"{name:12} → {now.strftime(DATE_FORMAT)}")
            except pytz.UnknownTimeZoneError:
                self.print_output(f"Invalid timezone: {zone}")
                
    def convert_unaware_datetime(self):
        self.clear_output()
        try:
            native_dt = datetime(2024, 12, 31, 23, 59)
            tz = pytz.timezone('Europe/Berlin')
            aware_dt = tz.localize(native_dt)
            
            self.print_output("Native to Aware Conversion:\n" + "-"*40)
            self.print_output(f"Native datetime: {native_dt}")
            self.print_output(f"Aware datetime:  {aware_dt.strftime(DATE_FORMAT)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def convert_between_zones(self):
        self.clear_output()
        try:
            source_tz = pytz.timezone('Asia/Tokyo')
            target_tz = pytz.timezone('America/Los_Angeles')
            
            original = source_tz.localize(datetime(2024, 6, 15, 18, 30))
            converted = original.astimezone(target_tz)
            
            self.print_output("Timezone Conversion:\n" + "-"*40)
            self.print_output(f"Original: {original.strftime(DATE_FORMAT)}")
            self.print_output(f"Converted: {converted.strftime(DATE_FORMAT)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def handle_ambiguous_time(self):
        self.clear_output()
        try:
            tz = pytz.timezone('America/New_York')
            ambiguous_dt = datetime(2023, 11, 5, 1, 30)
            aware_dt = tz.localize(ambiguous_dt, is_dst=None)
            
            self.print_output("Ambiguous Time Handling:\n" + "-"*40)
            self.print_output(f"Valid datetime: {aware_dt.strftime(DATE_FORMAT)}")
        except pytz.AmbiguousTimeError:
            messagebox.showwarning("Warning", "Ambiguous time detected!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def demonstrate_fixed_offset(self):
        self.clear_output()
        try:
            fixed_tz = pytz.FixedOffset(330)
            fixed_time = datetime.now(fixed_tz)
            
            self.print_output("Fixed Offset Example:\n" + "-"*40)
            self.print_output(f"UTC+5:30 → {fixed_time.strftime(DATE_FORMAT)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TimezoneApp(root)
    root.mainloop()