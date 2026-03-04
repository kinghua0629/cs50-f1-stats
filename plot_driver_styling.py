# Driver specific plot styling
# Show the usage of ``fastf1.plotting.get_driver_style`` with custom styles using Plotly.

import plotly.graph_objects as go

import fastf1
from fastf1 import plotting

# Load the race session.
year = int(input("Enter the year of the race: "))
schedule = fastf1.get_event_schedule(year)

# Display available races with proper round numbers
print("\nAvailable races:")
print("=" * 60)
for _, event in schedule.iterrows():
    print(f"Round {event['RoundNumber']}: {event['EventName']} ({event['Location']})")

# Get round number from user
round_num = int(input("\nEnter the round number you want to plot: "))

# Verify the round number exists
if round_num not in schedule["RoundNumber"].values:
    print(f"Error: Round {round_num} not found in {year} schedule!")
    exit(1)

# Get the event name for display
event_name = schedule[schedule["RoundNumber"] == round_num]["EventName"].iloc[0]
print(f"Selected: Round {round_num} - {event_name}")

race = fastf1.get_session(year, round_num, "R")
race.load()

# Get driver list and let user select drivers
print("\nAvailable drivers in this race:")
drivers_list = list(race.drivers)
driver_names = []

# Get driver abbreviations and names
for driver in drivers_list:
    driver_laps = race.laps.pick_drivers(driver)
    if not driver_laps.empty:
        abb = driver_laps["Driver"].iloc[0]
        driver_names.append(f"{abb} ({driver})")

print("\n".join([f"{i + 1}. {name}" for i, name in enumerate(driver_names)]))

# Let user select drivers
selected_input = input(
    "\nEnter the index numbers(not the driver's number!!!) of drivers you want to plot (separated by commas), or 'all' to select all drivers: "
)

if selected_input.strip().lower() == "all":
    selected_indices = list(range(len(driver_names)))
else:
    selected_indices = [int(x.strip()) - 1 for x in selected_input.split(",")]

selected_drivers = [drivers_list[i] for i in selected_indices]
selected_driver_names = [driver_names[i].split(" ")[0] for i in selected_indices]

print(f"\nSelected drivers: {', '.join(selected_driver_names)}")

# Creating fully custom styles

my_styles = [
    # style for each first driver
    {"color": "auto", "linestyle": "solid", "linewidth": 5, "alpha": 0.3},
    # style for each second driver
    {"color": "auto", "linestyle": "solid", "linewidth": 1, "alpha": 0.7},
]

fig = go.Figure()

for idx, driver in enumerate(selected_driver_names):
    laps = race.laps.pick_drivers(driver).pick_quicklaps().reset_index()

    # here, we now use ``style=my_style`` to use the custom styling
    style = plotting.get_driver_style(identifier=driver, style=my_styles, session=race)

    # Extract the custom style properties
    # For this example, we'll use the index to determine which style to use
    style_idx = idx % 2  # Alternate between first and second driver styles

    # Apply custom styling from my_styles
    custom_color = style["color"]
    custom_linewidth = my_styles[style_idx]["linewidth"]
    custom_opacity = my_styles[style_idx]["alpha"]

    # Handle LapTime conversion properly
    lap_times = laps["LapTime"]
    if hasattr(lap_times.iloc[0], "total_seconds"):
        # If it's a timedelta, convert to seconds
        y_values = [lap_time.total_seconds() for lap_time in lap_times]
    else:
        # If it's already numeric, use as is
        y_values = lap_times

    fig.add_trace(
        go.Scatter(
            x=laps.index,
            y=y_values,
            mode="lines",
            name=driver,
            line=dict(color=custom_color, width=custom_linewidth),
            opacity=custom_opacity,
        )
    )

# add axis labels and a legend
fig.update_layout(
    xaxis_title="Lap Number",
    yaxis_title="Lap Time (seconds)",
    title=f"Custom Driver Styling - {event_name} (Round {round_num})",
    showlegend=True,
)

# Show the final custom styling figure
fig.show()
