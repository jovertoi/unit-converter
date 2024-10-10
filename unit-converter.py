def input_value():
    while True:
        try:
            return float(input("Enter the value to convert: "))
        except ValueError:
            print("Please enter a valid number.")

def choose_unit():
    units = ['meters', 'feet', 'kilometers', 'miles']
    print("Available units:", ", ".join(units))
    while True:
        unit = input("Choose the input unit: ").lower()
        if unit in units:
            return unit
        print("Invalid unit. Please choose from the available units.")

def unit_converter(value, from_unit, to_unit):
    # Conversion factors
    m_to_ft = 3.28084
    km_to_mi = 0.621371
    
    # Convert to meters first
    if from_unit == 'feet':
        value /= m_to_ft
    elif from_unit == 'kilometers':
        value *= 1000
    elif from_unit == 'miles':
        value = value / km_to_mi * 1000
    
    # Then convert to desired unit
    if to_unit == 'feet':
        value *= m_to_ft
    elif to_unit == 'kilometers':
        value /= 1000
    elif to_unit == 'miles':
        value = value / 1000 * km_to_mi
    
    return value

def main():
    print("Welcome to the Unit Converter!")
    
    value = input_value()
    from_unit = choose_unit()
    
    print("\nNow choose the unit to convert to.")
    to_unit = choose_unit()
    
    result = unit_converter(value, from_unit, to_unit)
    
    print(f"\nResult: {value} {from_unit} is equal to {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
