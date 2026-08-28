"""
=========================================================
QUANT ULTRA
Model Helper
=========================================================
Provides compatibility between dictionaries and objects.
=========================================================
"""


class ModelHelper:

    @staticmethod
    def get(data, key, default=None):

        if data is None:
            return default

        if isinstance(data, dict):
            return data.get(key, default)

        return getattr(data, key, default)