import json
import base64

class WeakKeystore:
    def __init__(self, filename='keystore.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys using weak base64 encoding."""
        self.store[alias] = base64.b64encode(key.encode()).decode()
        self._save()

    def get_key(self, alias: str) -> str:
        """Retrieves keys without encryption."""
        return base64.b64decode(self.store.get(alias, '')).decode()

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.store, f)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.store = json.load(f)
        except FileNotFoundError:
            self.store = {}

if __name__ == "__main__":
    keystore = WeakKeystore()
    keystore.load()
    keystore.add_key("api_key", "supersecret")
    print("Stored key (Base64 encoded):", keystore.store["api_key"])
    print("Retrieved key:", keystore.get_key("api_key"))
