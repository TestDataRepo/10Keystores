import json
import base64

class ReversibleEncodingKeystore:
    def __init__(self, filename='keystore_reversible.json'):
        self.filename = filename
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys using simple base64 encoding with static padding."""
        encoded_key = base64.b64encode((key + "PADDING123").encode()).decode()
        self.store[alias] = encoded_key
        self._save()

    def get_key(self, alias: str) -> str:
        """Retrieves keys by reversing the base64 encoding."""
        decoded_key = base64.b64decode(self.store.get(alias, "").encode()).decode()
        return decoded_key.replace("PADDING123", "")

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
    keystore = ReversibleEncodingKeystore()
    keystore.load()
    keystore.add_key("service_api_key", "mysecretkey")
    print("Stored key (Weak base64 encoding):", keystore.store["service_api_key"])
    print("Retrieved key:", keystore.get_key("service_api_key"))
