import json
import hashlib

class StaticSaltKeystore:
    def __init__(self, filename='keystore_static_salt.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys using SHA-256 with a static, hardcoded salt."""
        salt = "staticsalt123"  # Predictable and weak salt
        hashed_key = hashlib.sha256((salt + key).encode()).hexdigest()
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
    keystore = StaticSaltKeystore()
    keystore.load()
    keystore.add_key("admin_password", "mypassword")
    print("Stored key (SHA-256 with static salt):", keystore.store["admin_password"])
