import json
import os

def get_data_path():
    # Construct the path to users.json consistently
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(current_dir, "..", "..", "data", "users.json"))

def save_account_data(new_user_data):
    file_path = get_data_path()
    
    # Read phase
    accounts = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                accounts = json.load(f)
            except json.JSONDecodeError:
                accounts = []
    
    accounts.append(new_user_data)
    
    # Write phase: Atomic replacement
    temp_path = file_path + ".tmp"
    with open(temp_path, 'w') as f:
        json.dump(accounts, f, indent=4)
        f.flush()
        os.fsync(f.fileno()) # Force the OS to write buffer to disk
    
    # Atomically rename to target file (guarantees file state is updated)
    os.replace(temp_path, file_path)
    # Force print the absolute path so we know exactly where to look
    abs_path = os.path.abspath(file_path)
    print(f"[VERIFY] Checking file content at absolute path: {abs_path}")
    
    # Read the file back immediately to prove it contains data
    with open(abs_path, 'r') as f:
        content = f.read()
        print(f"[VERIFY] Actual file content: {content[:50]}...")

    print(f"[DEBUG] Verification: File size is {os.path.getsize(file_path)} bytes.")