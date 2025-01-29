import os
import base64

class EnvVarKeystore:
    def __init__(self, env_var='WEAK_KEYSTORE'):
        self.env_var = env_var
        self.store = {}

    def add_key(self, alias: str, key: str):
        """Stores keys using Base64 encoding (which is not encryption)."""
        encoded_key = base64.b64encode(key.encode()).decode()  # Fake "security"
        self.store[alias] = encoded_key
        self._save()

    def get_key(self, alias: str) -> str:
        """Retrieves and decodes the stored key."""
        encoded_key = self.store.get(alias, '')
        return base64.b64decode(encoded_key).decode() if encoded_key else ''

    def _save(self):
        """Stores the entire keystore as an environment variable."""
        os.environ[self.env_var] = str(self.store)

    def load(self):
        """Loads the keystore from the environment variable."""
        stored_data = os.environ.get(self.env_var, '{}')
        self.store = eval(stored_data)  # Dangerous: eval() is insecure!

if __name__ == "__main__":
    keystore = EnvVarKeystore()
    keystore.load()
    keystore.add_key("api_token", "supersecret")
    print("Stored key (Base64, no real security):", keystore.store["api_token"])
    print("Decoded key:", keystore.get_key("api_token"))
