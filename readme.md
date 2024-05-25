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
#Enable Custom Intergration
grid_usage_tracker:

# Register Custom Intergration Sensor
sensor:
  - platform: grid_usage_tracker
    name: Grid Usage

# Input for adding purchased units
input_text:
  prepaid_units:
    name: Prepaid Units
    initial: "0"
    pattern: '^\d+(\.\d{1,2})?$'
    mode: text
    max: 10
```

Add the following to your `scripts.yaml` to call the reset usage service.

```yaml
reset_grid_usage:
  alias: Reset Grid Usage
  sequence:
    - service: grid_usage_tracker.reset_grid_usage
```

## Available Sensors

The Grid Usage Tracker provides the following sensors:

- `grid_usage`: Tracks the total electricity usage from the grid.


## Services

The component also provides services to reset the usage data. The available services are defined in the `services.yaml` file.

## Example Usage

You can use the sensors in your Home Assistant dashboard to monitor your electricity usage. Here is an example of how to add the sensors to your `lovelace` configuration:

```yaml
type: entities
entities:
  - entity: sensor.grid_usage
    name: Grid Usage
```

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Support

If you have any issues or questions, please open an issue on the GitHub repository.