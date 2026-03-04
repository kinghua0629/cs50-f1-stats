# Position changes during a race
# Plot the position of each driver at the end of each lap using Plotly.

import plotly.graph_objects as go

import fastf1
import fastf1.plotting

# Load the session and create the plot
year = int(input("Enter the year of the race: "))
schedule = fastf1.get_event_schedule(year)

# Display available races with proper round numbers
print("\nAvailable races:")
print("=" * 60)
for event in schedule.itertuples():
    print(f"Round {event.RoundNumber}: {event.EventName} ({event.Location})")

# Get round number from user
round_num = int(input("\nEnter the round number you want to plot: "))

# Verify the round number exists
if round_num not in schedule["RoundNumber"].values:
    print(f"Error: Round {round_num} not found in {year} schedule!")
    exit(1)

# Get the event name for display
event_name = schedule[schedule["RoundNumber"] == round_num]["EventName"].iloc[0]
print(f"Selected: Round {round_num} - {event_name}")

session = fastf1.get_session(year, round_num, "R")
session.load(telemetry=False, weather=False)

# Get driver list and let user select drivers
print("\nAvailable drivers in this race:")
drivers_list = list(session.drivers)
driver_names = []

# Get driver abbreviations and names
for driver in drivers_list:
    driver_laps = session.laps.pick_drivers(driver)
    if not driver_laps.empty:
        abb = driver_laps["Driver"].iloc[0]
        driver_names.append(f"{abb} ({driver})")

print("\n".join([f"{i + 1}. {name}" for i, name in enumerate(driver_names)]))

# Let user select drivers
selected_input = input(
    "\nEnter the index numbers of drivers(not the driver's number!!!) you want to plot (separated by commas), or 'all' to select all drivers: "
)

if selected_input.strip().lower() == "all":
    selected_indices = list(range(len(driver_names)))
else:
    selected_indices = [int(x.strip()) - 1 for x in selected_input.split(",")]

selected_drivers = [drivers_list[i] for i in selected_indices]
selected_driver_names = [driver_names[i].split(" ")[0] for i in selected_indices]

print(f"\nSelected drivers: {', '.join(selected_driver_names)}")
print(
    "Note: Team second drivers (even numbered drivers) will be displayed with dashed lines"
)

fig = go.Figure()

# For each selected driver, get their three letter abbreviation (e.g. 'HAM') by simply
# using the value of the first lap, get their color and then plot their
# position over the number of laps.
for idx, drv in enumerate(selected_drivers):
    drv_laps = session.laps.pick_drivers(drv)

    abb = drv_laps["Driver"].iloc[0]
    style = fastf1.plotting.get_driver_style(
        identifier=abb, style=["color", "linestyle"], session=session
    )

    # Convert matplotlib linestyle to plotly compatible dash style
    dash_style = "solid"
    if style["linestyle"] == "--":
        dash_style = "dash"
    elif style["linestyle"] == ":":
        dash_style = "dot"
    elif style["linestyle"] == "-.":
        dash_style = "dashdot"

    fig.add_trace(
        go.Scatter(
            x=drv_laps["LapNumber"],
            y=drv_laps["Position"],
            mode="lines",
            name=abb,
            line=dict(color=style["color"], dash=dash_style),
        )
    )

# Finalize the plot by setting y-limits that invert the y-axis so that position
# one is at the top, set custom tick positions and axis labels.
fig.update_layout(
    yaxis=dict(
        autorange="reversed",  # This inverts the y-axis
        tickvals=[1, 5, 10, 15, 20],  # Custom tick positions
    ),
    xaxis=dict(title="Lap"),
    yaxis_title="Position",
    title=f"Driver Position Changes - {event_name} (Round {round_num})",
    showlegend=True,
    legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02),
    margin=dict(r=150),  # Add right margin to accommodate legend
)

fig.show()
