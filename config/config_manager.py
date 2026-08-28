"""
=========================================================
QUANT ULTRA
Configuration Manager
=========================================================
"""

import json
from pathlib import Path


class ConfigManager:

    def __init__(self):

        self.path = Path("config/config.json")

        self.config = {}

        self.load()

    # -------------------------------------------------

    def load(self):

        if self.path.exists():

            with open(self.path, "r") as file:

                self.config = json.load(file)

        else:

            self.config = {}

    # -------------------------------------------------

    def save(self):

        with open(self.path, "w") as file:

            json.dump(

                self.config,

                file,

                indent=4,

            )

    # -------------------------------------------------

    def get(

        self,

        key,

        default=None,

    ):

        return self.config.get(

            key,

            default,

        )

    # -------------------------------------------------

    def set(

        self,

        key,

        value,

    ):

        self.config[key] = value

        self.save()

    # -------------------------------------------------

    def all(self):

        return self.config

    # -------------------------------------------------

    def profile(self):

        return self.get(

            "profile",

            "paper",

        )


# ---------------------------------------------------------

if __name__ == "__main__":

    config = ConfigManager()

    print()

    print(config.all())