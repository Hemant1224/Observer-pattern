This example focuses on a Weather Station notifying subscribed Display Devices about temperature changes.

1. WeatherStation maintains a list of subscribers and a temperature property.
2. It provides methods to subscribe and unsubscribe devices.
3. The set_temperature method updates the temperature and calls notify.
notify loops through subscribers and calls their update method with the new temperature.
4. DisplayDevice implements the update method to simply print the received temperature.


This is a stripped-down example but demonstrates the core idea of the Observer pattern: a subject notifying interested observers about state changes.