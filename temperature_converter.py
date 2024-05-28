def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in degrees Celsius.

    Returns:
    float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
    float: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    # Example temperatures
    temp_celsius = int(input("Input celsius: "))
    temp_fahrenheit = int(input("Input fahrenheit: "))

    # Convert Celsius to Fahrenheit
    result_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C is {result_fahrenheit}°F")

    # Convert Fahrenheit to Celsius
    result_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"{temp_fahrenheit}°F is {result_celsius}°C")
