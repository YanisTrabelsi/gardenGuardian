def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if (temp < 0):
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif (temp > 40):
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return (temp)


def test_temperature() -> None:
    test1: str = "25"
    test2: str = "abc"
    test3: str = "100"
    test4: str = "-50"
# =====TEST 1=====
    try:
        print(f"Input data is '{test1}'")
        print(f"Temperature is now {input_temperature(test1)}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
# =====TEST 2=====
    try:
        print(f"Input data is '{test2}'")
        print(f"Temperature is now {input_temperature(test2)}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
# =====TEST 3=====
    try:
        print(f"input data is '{test3}'")
        print(f"Temperature is now {input_temperature(test3)}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
# =====TEST 4=====
    try:
        print(f"input data is '{test4}'")
        print(f"Temperature is now {input_temperature(test4)}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
