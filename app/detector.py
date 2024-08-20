import os
import hashlib

class RansomwareDetector:
    def __init__(self):
        self.file_hashes = {}

    def detect_changes(self, file_path):
        if not os.path.exists(file_path):
            return False
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        file_hash = hash_md5.hexdigest()

        if file_path in self.file_hashes:
            if self.file_hashes[file_path] != file_hash:
                print(f"Ransomware activity detected: {file_path}")
                return True
        self.file_hashes[file_path] = file_hash
        return False
