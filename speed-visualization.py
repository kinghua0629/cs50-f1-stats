import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

import fastf1

# get the year from the user and find the according schedule
year = int(input("Enter the year of the race: "))
schedule = fastf1.get_event_schedule(year)

# display available races with proper round numbers
print("\nAvailable races:")
print("=" * 60)
for event in schedule.itertuples():
    print(f"Round {event.RoundNumber}: {event.EventName} ({event.Location})")

# get round number from user
round_num = int(input("\nEnter the round number you want to plot: "))

# Verify the round number exists
if round_num not in schedule["RoundNumber"].values:
    print(f"Error: Round {round_num} not found in {year} schedule!")
    exit(1)

# get the event name and dispaly the name and round number to the user
event_name = schedule[schedule["RoundNumber"] == round_num]["EventName"]

print(f"Selected: Round {round_num} -- {event_name}")

# load race of the session
session = fastf1.get_session(year, round_num, "R")
session.load()

# get the drivers from the user
print("\nAvailable drivers(Only 1 driver per request!)")
print("=" * 30)

driver_numbers = (
    session.drivers
)  # store the drivers' number in a list, like ['33', '44']
driver_list_with_info = []

# 使用 enumerate 实现从 1 开始的 index
for i, d_num in enumerate(driver_numbers):
    # 获取车手详细信息
    driver_info = session.get_driver(d_num)
    abb = driver_info["Abbreviation"]
    team = driver_info["TeamName"]

    # 打印：序号. 编号 (缩写) - 车队
    print(f"{i}. {d_num} ({abb}) - {team}")

    # 将编号存入列表，方便用户输入数字后提取
    driver_list_with_info.append(d_num)

# 获取用户输入的车手号码
# 注意：session.drivers 中的号码是字符串格式，所以我们要确保比较时类型一致
choice_num = input(
    f"\nEnter the Driver Number (e.g., {driver_numbers[0]}) you want to plot: "
).strip()

# 验证输入的号码是否在当前比赛的车手名单中
if choice_num in driver_numbers:
    # 获取该车手的详细信息
    selected_info = session.get_driver(choice_num)

    print(
        f"\nSuccessfully Selected: {selected_info['FullName']} ({selected_info['Abbreviation']})"
    )
    print(f"Team: {selected_info['TeamName']} | Number: {choice_num}")

    # 将车手缩写赋值给变量，用于后续绘图
    driver = selected_info["Abbreviation"]
else:
    print(f"Error: Driver number '{choice_num}' not found in this session!")
    print(f"Available numbers are: {', '.join(driver_numbers)}")
    exit(1)


colormap = mpl.cm.plasma

# pick fastest lap
lap = session.laps.pick_drivers(driver).pick_fastest()

# get telemetry data
x = lap.telemetry["X"]
y = lap.telemetry["Y"]
color = lap.telemetry["Speed"]

# create line segments
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# draw the plot
fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))
fig.suptitle(f"{session.event.name} {year} - {driver} - Speed", size=24, y=0.97)

# adjust margins and turns of axis
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)
ax.axis("off")

# plot the data
# create background track line
ax.plot(x, y, color="black", linestyle="-", linewidth=16, zorder=0)

norm = plt.Normalize(color.min(), color.max())
lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle="-", linewidth=5)

# set the values used for colormapping
lc.set_array(color)

# merge all line segments into one
line = ax.add_collection(lc)

# create colorbar
plt.colorbar(mappable=line, label="Speed", orientation="horizontal", shrink=0.5)

# show plot
plt.show()
