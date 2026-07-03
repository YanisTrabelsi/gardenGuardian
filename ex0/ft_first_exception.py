def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("Input data is '25'")
    print(f"Temperature is now {input_temperature("25")}°C\n")
    try:
        print("Input data is 'abc'")
        print(f"Temperature is now {input_temperature("abc")}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


print("=== Garden Temperature ===\n")
test_temperature()
print("All tests completed - program didn't crash!")
