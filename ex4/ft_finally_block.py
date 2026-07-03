class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    plant_name_capitalized: str = plant_name.capitalize()
    if (plant_name == plant_name_capitalized):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests ans returning to main")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests ans returning to main")
    finally:
        print("Closing watering system\n")


print("=== Garden Watering System ===\n")
test_watering_system()
print("Cleanup always happens, even with errors!")
