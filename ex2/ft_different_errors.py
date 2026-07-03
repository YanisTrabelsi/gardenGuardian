def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        operation_number /= 0
    elif (operation_number == 2):
        open("/non/existent/file")
    elif (operation_number == 3):
        print("hello" + 19)
    return


def test_error_types() -> None:
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
