import csv
import os
from datetime import datetime
import pytz

def main():
    # Ask the user for an emoji input
    entermoji = input("Hey there! How's Everything? Express using an emoji: ").rstrip()
    result = get_quote(entermoji)
    store_data(entermoji)
    print(result[1])
    display = input("Do you want to track you emotions so far?(yes/no)")
    print(track_emotions(display))

def get_quote(emoji):
    with open("initialdata.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == emoji:  # Match the emoji in the first column
                return row[0],row[1]  # Return the corresponding quote
        return "Sorry, There is no quote for the given emoji"

def store_data(a):
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
    x = get_quote(a)
    entered_emoji = x[0]
    header = ["DATE_AND_TIME", "EMOJI_ENTERD"]
    file_exists = os.path.isfile("userdata.csv")
    with open("userdata.csv", "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if not file_exists:
            writer.writeheader()
        writer.writerow({"DATE_AND_TIME": current_time, "EMOJI_ENTERD": entered_emoji})
    return f"{a} is Stored!"

def track_emotions(m):
    with open("userdata.csv", encoding="utf-8") as trackfile:
        reader = csv.reader(trackfile)
        data = []
        for row in reader:
            if len(row) >= 2:  # Ensure the row has at least two columns
                data.append(f"At this time: {row[0]}, your emotion is this: {row[1]}")
        if m.lower() == 'yes':
            return '\n'.join(data) if data else "No tracked emotions yet!"
        elif m.lower() == 'no':
            return "Alright! Your Wish."
        else:
            return "Invalid Input"

if __name__ == "__main__":
    main()
