import json
from collections import defaultdict


def load_logs_and_calculate_results(log_file_path):
    # Define question categories
    results = {
        "easy": {"processed": 0, "passed": 0},
        "medium": {"processed": 0, "passed": 0},
        "hard": {"processed": 0, "passed": 0},
    }
    tks = 0

    json_objects = []
    current_object = {}

    # Initialize variables to track progress
    current_category_index = 0
    question_count = 0
    with open(log_file_path, "r") as log_file:
        for line in log_file:
            line = line.strip()
            if line.startswith('"'):
                question_count += 1
                # Check if current_object is not empty, which means it's ready to be added to json_objects
                if current_object:
                    json_objects.append(current_object)
                    current_object = {}  # Reset for the next object

                # Extract question text and start a new JSON object
                question_text = line[1:-1]  # Remove quotation marks
                current_object["question"] = question_text
            else:
                # It's a key-value pair, extract and add to current_object
                key_value = json.loads(line)
                current_object.update(key_value)
    for i, obj in enumerate(json_objects):
        if i < 8 and i >= 0:
            obj["difficulty"] = "easy"
        elif i < 16 and i >= 8:
            obj["difficulty"] = "medium"
        else:
            obj["difficulty"] = "hard"

    for obj in json_objects:
        results[obj["difficulty"]]["processed"] += 1

        if obj["Result"] == "Pass":
            results[obj["difficulty"]]["passed"] += 1

        tks = tks + obj["Token count input"] + obj["Token count output"]

    # print(json.dumps(results, indent=4))
    for d in ["easy", "medium", "hard"]:
        if results[d]["processed"] > 0:
            print(
                f'{d.capitalize()} acc: \t{results[d]["passed"]}/{results[d]["processed"]} = {results[d]["passed"]/results[d]["processed"]*100:.2f}%'
            )
        else:
            print(f'{d.capitalize()} acc: \t{results[d]["processed"]}/0 = 0%')
    print(f"Total tokens: {tks}")


if __name__ == "__main__":
    log_file_path = "./logs/node10_log.jsonl"
    load_logs_and_calculate_results(log_file_path)
