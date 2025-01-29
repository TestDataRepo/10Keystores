import json
import random

class PredictableKeystore:
    def __init__(self, filename='keystore_weak.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys with a predictable XOR transformation."""
        weak_key = ''.join(chr(ord(c) ^ 0x42) for c in key)  # Simple XOR encoding
        self.store[alias] = weak_key
        self._save()

    def get_key(self, alias: str) -> str:
        """Retrieves keys by reversing the predictable XOR operation."""
        return ''.join(chr(ord(c) ^ 0x42) for c in self.store.get(alias, ''))

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.store, f, indent=4)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.store = json.load(f)
        except FileNotFoundError:
            self.store = {}

if __name__ == "__main__":
    keystore = PredictableKeystore()
    keystore.load()
    keystore.add_key("api_token", "mysecrettoken")
    print("Stored key (Weak XOR encoded):", keystore.store["api_token"])
    print("Retrieved key:", keystore.get_key("api_token"))
