import json
import hashlib

class HardcodedHashKeystore:
    def __init__(self, filename='keystore_hashed.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys using an insecure hardcoded hash salt."""
        salt = "fixed_salt"  # Hardcoded, predictable salt
        weak_hash = hashlib.md5((salt + key).encode()).hexdigest()  # MD5 is weak
        self.store[alias] = weak_hash
        self._save()

    def get_key(self, alias: str) -> str:
        """Returns the stored hashed key (irreversible)."""
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
    keystore = HardcodedHashKeystore()
    keystore.load()
    keystore.add_key("user_password", "mypassword")
    print("Stored key (Weak MD5 hash):", keystore.store["user_password"])
