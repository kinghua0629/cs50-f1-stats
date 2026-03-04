# FastF1 Visualization Scripts

A collection of Python scripts for visualizing Formula 1 race data using the FastF1 library and Plotly.

## Demo: https://youtu.be/tzwww0bJy3c

## Scripts Overview

### 1. Driver Styling Plot

**File:** [`plot_driver_styling.py`](plot_driver_styling.py)

This script creates customized lap time comparison plots with driver-specific styling. It allows you to:
- Select a race year and round from the official F1 schedule
- Choose specific drivers to compare from the participating drivers
- Apply custom line styles with alternating patterns:
  - Primary drivers: thicker lines (5px) with lower opacity (0.3)
  - Secondary drivers: thinner lines (1px) with higher opacity (0.7)
- Visualize lap time progression across the race using quicklaps only
- Automatic team color assignment using FastF1's official F1 styling

### 2. Position Changes Plot

**File:** [`plot_position_changes.py`](plot_position_changes.py)

This script visualizes driver position changes throughout a race. It allows you to:
- Select a race year and round from the official F1 schedule
- Choose specific drivers to track from the participating drivers
- Display position changes with official F1 team colors
- Use different line styles (solid/dashed) to distinguish drivers from the same team
- View inverted y-axis with position 1 at the top for better readability
- Interactive legend with vertical layout for easy driver identification

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Driver Styling Plot

```bash
python plot_driver_styling.py
```

Follow the interactive prompts to:
1. Enter the race year (e.g., 2024)
2. Select the round number from the displayed schedule
3. Choose drivers by their index numbers (comma-separated, e.g., "1,3,5")

### Position Changes Plot

```bash
python plot_position_changes.py
```

Follow the interactive prompts to:
1. Enter the race year (e.g., 2024)
2. Select the round number from the displayed schedule
3. Choose drivers by their index numbers (comma-separated, e.g., "1,3,5")

> **Note:** Team second drivers (even-numbered drivers) will be displayed with dashed lines for better differentiation.

## Requirements

- Python 3.8+
- FastF1 >= 3.1.0
- Plotly >= 5.14.0
- Pandas >= 1.5.0

See [`requirements.txt`](requirements.txt) for the complete list of dependencies.

## Features

- **Interactive Selection**: User-friendly prompts for race and driver selection with full schedule display
- **Official F1 Styling**: Uses official team colors and driver styling via FastF1
- **Plotly Visualization**: Interactive charts with zoom, pan, and hover capabilities
- **Smart Driver Styling**: Automatic alternating styles for better visual comparison
- **Position Tracking**: Inverted y-axis showing position 1 at the top (race leader)

## Project Structure

```
fastf1/
├── plot_driver_styling.py      # Lap time comparison with custom styling
├── plot_position_changes.py    # Position changes throughout the race
├── speed-visualization.py      # (Additional visualization script)
├── requirements.txt            # Python dependencies
├── README.md                   # This file (English)
└── README_zh.md                # Chinese version
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

For Chinese version, see [README_zh.md](README_zh.md)
