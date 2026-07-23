import json
import os


def save_json(data, filename):

    os.makedirs("reports", exist_ok=True)

    with open(
        f"reports/{filename}",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_json(filename):

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)