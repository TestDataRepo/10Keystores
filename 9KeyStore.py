import json

class PlaintextKeystore:
    def __init__(self, filename='plaintext_keystore.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys in plaintext (extremely insecure)."""
        self.store[alias] = key  # No hashing, no encryption
        self._save()

    def get_key(self, alias: str) -> str:
        """Returns the stored key in plaintext."""
        return self.store.get(alias, '')

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
    keystore = PlaintextKeystore()
    keystore.load()
    keystore.add_key("super_secret", "123456")  # One of the worst passwords ever
    print("Stored key (plaintext, no security at all):", keystore.store["super_secret"])
