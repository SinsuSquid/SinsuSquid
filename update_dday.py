from datetime import datetime

# 1. Define your timeline timeline, Senpai! 📅
start_date = datetime.strptime("1998-03-10", "%Y-%m-%d")  # When the goal started
target_date = datetime.strptime("2028-03-10", "%Y-%m-%d") # The ultimate D-Day!
today = datetime.today()

# 2. Calculate total days and elapsed days
total_duration = (target_date - start_date).days
elapsed_days = (today - start_date).days
days_left = (target_date - today).days

# 3. Calculate percentage (cap it between 0% and 100%)
if total_duration <= 0:
    percent = 100
else:
    percent = max(0, min(100, (elapsed_days / total_duration) * 100))

# 4. Generate the visual progress bar (20 characters wide)
bar_length = 20
filled_length = int(round(bar_length * percent / 100))
bar = "▓" * filled_length + "░" * (bar_length - filled_length)

# 5. Format the beautiful output string
output_lines = [
    f"### 🧙‍♂️ You're a wizard",
    f"🔮 **{percent:.1f}% Complete**",
    f"```text",
    f"[{bar}]",
    f"```",
    f"🪄 **Started:** {start_date.strftime('%Y-%m-%d')} | ⏳ **Days Remaining:** {max(0, days_left)} days left | 🏁 **Target:** {target_date.strftime('%Y-%m-%d')}"
]

dday_text = "\n".join(output_lines)

# 6. Read and update the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_tag = ""
end_tag = ""

start_idx = content.find(start_tag) + len(start_tag)
end_idx = content.find(end_tag)

new_content = content[:start_idx] + f"\n\n{dday_text}\n\n" + content[end_idx:]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("README successfully updated with the progress bar! 🎉")
