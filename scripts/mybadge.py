import json
import anybadge


def read_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# coverage run -m pytest test_my_math.py && coverage json -o coverage.json &&  coverage xml

if __name__ == "__main__":
    json_file_name = "coverage.json"  # Replace with the actual JSON file name

    # Read the JSON file
    json_data = read_json_file(json_file_name)

    if json_data:
        # Display the contents of the JSON file
        print("Contents of the JSON file:")
        print(json.dumps(json_data, indent=2))
        total_coverage = json_data["totals"]["percent_covered_display"]
        print(total_coverage)
        badge = anybadge.Badge(label="Coverage", value=total_coverage)
        print(badge)
        badge.write_badge("coverage.svg")

        # Generate coverage badge using template
        # badge = anybadge.Badge(label="Coverage", value=70, template="coverage.html")
        # badge.save("coverage3.svg")

    coverage = 90
    badge2 = anybadge.Badge(label="Coverage", value=coverage)
    badge2.write_badge("coverage2.svg")
