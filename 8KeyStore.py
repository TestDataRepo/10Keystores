import json
import hashlib

class WeakKeystore:
    def __init__(self, filename='weak_keystore.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys using MD5 with no salt (extremely weak)."""
        hashed_key = hashlib.md5(key.encode()).hexdigest()  # MD5 is insecure
        self.store[alias] = hashed_key
        self._save()

    def get_key(self, alias: str) -> str:
        """Returns the stored hashed key."""
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
    keystore = WeakKeystore()
    keystore.load()
    keystore.add_key("user_password", "mypassword")
    print("Stored key (MD5, no salt):", keystore.store["user_password"])
