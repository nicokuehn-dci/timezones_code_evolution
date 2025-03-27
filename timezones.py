"""
Timezone Examples Program
Full-featured implementation with proper terminology and error handling
"""

from datetime import datetime
import pytz

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z%z"

# ========================
# CORE FUNCTIONALITY
# ========================

def list_all_timezones():
    """Display all available timezones"""
    print("\nAll Supported Timezones:")
    for tz in pytz.all_timezones:
        print(f"- {tz}")

def show_common_timezones():
    """Display frequently used timezones"""
    print("\nCommon Timezones:")
    for tz in pytz.common_timezones:
        print(f"- {tz}")

def show_current_time():
    """Display current time in key locations"""
    print("\nCurrent Time:")
    locations = {
        'UTC': pytz.utc,
        'India (Kolkata)': 'Asia/Kolkata',
        'US/Eastern': 'America/New_York',
        'Europe/Paris': 'Europe/Paris',
        'Japan': 'Asia/Tokyo'
    }
    
    for name, zone in locations.items():
        try:
            tz = pytz.timezone(zone) if isinstance(zone, str) else zone
            now = datetime.now(tz)
            print(f"{name:15}: {now.strftime(DATE_FORMAT)}")
        except pytz.UnknownTimeZoneError:
            print(f"Invalid timezone: {zone}")

def convert_unaware_datetime():
    """Convert native (timezone-unaware) datetime to aware"""
    try:
        print("\nNative to Aware Conversion:")
        native_dt = datetime(2024, 12, 31, 23, 59)
        tz = pytz.timezone('Europe/Berlin')
        aware_dt = tz.localize(native_dt)
        print(f"Native datetime: {native_dt}")
        print(f"Aware datetime:  {aware_dt.strftime(DATE_FORMAT)}")
    except Exception as e:
        print(f"Error: {str(e)}")

def convert_between_zones():
    """Convert between timezones"""
    try:
        print("\nTimezone Conversion:")
        source_tz = pytz.timezone('Asia/Tokyo')
        target_tz = pytz.timezone('America/Los_Angeles')
        
        original = source_tz.localize(datetime(2024, 6, 15, 18, 30))
        converted = original.astimezone(target_tz)
        
        print(f"Original: {original.strftime(DATE_FORMAT)}")
        print(f"Converted: {converted.strftime(DATE_FORMAT)}")
    except Exception as e:
        print(f"Error: {str(e)}")

def handle_ambiguous_time():
    """Demonstrate ambiguous time handling"""
    try:
        print("\nAmbiguous Time Handling:")
        tz = pytz.timezone('America/New_York')
        ambiguous_dt = datetime(2023, 11, 5, 1, 30)  # DST end
        aware_dt = tz.localize(ambiguous_dt, is_dst=None)
        print(f"Valid datetime: {aware_dt.strftime(DATE_FORMAT)}")
    except pytz.AmbiguousTimeError:
        print("Ambiguous time detected! Please specify is_dst parameter")
    except Exception as e:
        print(f"Error: {str(e)}")

def demonstrate_fixed_offset():
    """Show fixed offset timezone"""
    try:
        print("\nFixed Offset Example:")
        fixed_tz = pytz.FixedOffset(330)  # UTC+5:30
        fixed_time = datetime.now(fixed_tz)
        print(f"Fixed offset time: {fixed_time.strftime(DATE_FORMAT)}")
    except Exception as e:
        print(f"Error: {str(e)}")

# ========================
# INTERFACE SYSTEM
# ========================

EXAMPLES = {
    1: ("List all timezones", list_all_timezones),
    2: ("Show common timezones", show_common_timezones),
    3: ("Current global times", show_current_time),
    4: ("Convert native to aware", convert_unaware_datetime),
    5: ("Convert between zones", convert_between_zones),
    6: ("Handle ambiguous times", handle_ambiguous_time),
    7: ("Demonstrate fixed offset", demonstrate_fixed_offset),
}

def display_menu():
    """Show program interface"""
    print("\n" + "=" * 50)
    print("Timezone Operations Program (v1.0)")
    print("=" * 50)
    for num, (desc, _) in EXAMPLES.items():
        print(f"{num:2}. {desc}")
    print(" 0. Exit")
    print("=" * 50)

def main():
    """Program execution flow"""
    while True:
        display_menu()
        choice = input("\nEnter choice (0-7): ").strip()
        
        if choice == '0':
            print("\nExiting program. Goodbye!")
            break
            
        if choice.isdigit() and (choice_int := int(choice)) in EXAMPLES:
            try:
                print("\n" + "=" * 50)
                EXAMPLES[choice_int][1]()
                print("=" * 50 + "\n")
            except Exception as e:
                print(f"\nCritical error: {str(e)}")
        else:
            print("Invalid input. Please enter 0-7.")

if __name__ == "__main__":
    main()