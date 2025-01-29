import json
import random

class InsecureRandomizedKeystore:
    def __init__(self, filename='keystore_insecure.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys with a weak random character shift."""
        shift = random.randint(1, 3)  # Small predictable shift
        shifted_key = ''.join(chr(ord(c) + shift) for c in key)
        self.store[alias] = shifted_key
        self._save()

    def get_key(self, alias: str) -> str:
        """Retrieves keys by reversing the weak shift."""
        shift = random.randint(1, 3)  # May not match encoding shift
        return ''.join(chr(ord(c) - shift) for c in self.store.get(alias, ''))

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
    keystore = InsecureRandomizedKeystore()
    keystore.load()
    keystore.add_key("device_secret", "supersecurekey")
    print("Stored key (Weak randomized shift):", keystore.store["device_secret"])
    print("Retrieved key:", keystore.get_key("device_secret"))
