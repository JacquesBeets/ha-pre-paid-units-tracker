# Grid Usage Tracker

The Grid Usage Tracker is a custom component for Home Assistant that helps you monitor and track your electricity grid usage. This component provides sensors to track the amount of electricity consumed from the grid.

## Installation

1. **Download the component:**
   - Clone or download the repository to your local machine.

2. **Copy files:**
   - Copy the `grid_usage_tracker` directory into your Home Assistant `custom_components` directory.

3. **Restart Home Assistant:**
   - Restart your Home Assistant instance to recognize the new custom component.

## Configuration

To configure the Grid Usage Tracker, add the following to your `configuration.yaml` file:

```yaml
sensor:
  - platform: grid_usage_tracker
    name: Grid Usage
    monitored_conditions:
      - total_usage
      - peak_usage
      - off_peak_usage
```

## Available Sensors

The Grid Usage Tracker provides the following sensors:

- `total_usage`: Tracks the total electricity usage from the grid.
- `peak_usage`: Tracks the electricity usage during peak hours.
- `off_peak_usage`: Tracks the electricity usage during off-peak hours.

## Services

The component also provides services to reset the usage data. The available services are defined in the `services.yaml` file.

## Example Usage

You can use the sensors in your Home Assistant dashboard to monitor your electricity usage. Here is an example of how to add the sensors to your `lovelace` configuration:

```yaml
type: entities
entities:
  - entity: sensor.grid_usage_total
    name: Total Grid Usage
  - entity: sensor.grid_usage_peak
    name: Peak Grid Usage
  - entity: sensor.grid_usage_off_peak
    name: Off-Peak Grid Usage
```

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Support

If you have any issues or questions, please open an issue on the GitHub repository.