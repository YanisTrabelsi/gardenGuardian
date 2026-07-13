class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def error_generator(type: str) -> None:
    if (type == "Tomato"):
        raise PlantError("The tomato plant is wilting!")
    if (type == "Water"):
        raise WaterError("Not enough water in the tank!")

    return


def tests() -> None:
    # =====Test 1=====
    try:
        error_generator("hello")
    except GardenError as e:
        print(e)
    # =====Test 2=====
    print("\nTesting PlantError...")
    try:
        error_generator("Tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    # =====Test 3=====
    print("\nTesting WaterError...")
    try:
        error_generator("Water")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    # =====Test 4=====
    print("Testing catching all garden errors...")
    try:
        error_generator("Tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    # =====Test 5=====
    try:
        error_generator("Water")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    tests()
    print("\nAll custom error types work correctly!")
