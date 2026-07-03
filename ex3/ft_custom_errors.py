class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def error_generator(type: str) -> None:
    type = type.lower()

    if (type == "tomato"):
        raise PlantError("The tomato plant is wilting!")
    if (type == "water"):
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
        print(f"Caught PlantError: {e}")
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


print("=== Custom Garden Errors Demo ===")
tests()
print("\nAll custom error types work correctly!")
