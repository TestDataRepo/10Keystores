import json

class PlaintextKeystore:
    def __init__(self, filename='keystore_plaintext.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys in plaintext without any protection."""
        self.store[alias] = key
        self._save()

    def get_key(self, alias: str) -> str:
        """Retrieves keys directly from the file."""
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
    keystore.add_key("database_password", "mypassword123")
    print("Stored key (Plaintext):", keystore.store["database_password"])
    print("Retrieved key:", keystore.get_key("database_password"))
