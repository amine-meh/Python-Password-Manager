# Python Password Manager

Welcome to the Password Manager! This Python project demonstrates basic encryption using the `cryptography` library and allows users to store and retrieve passwords securely. Below is an overview of the project and how to use it.

## Features

- **Password Encryption**: Uses the `cryptography.fernet` module to encrypt and decrypt passwords.
- **Password Management**:
  - Add new account credentials securely.
  - View existing account credentials.
- **Master Password**: Protects your saved data using a master password for added security.

## Prerequisites

1. **Python 3.6 or higher**
2. **Required library**: Install the `cryptography` module using pip:
   ```bash
   pip install cryptography
   ```

## How to Use

### Step 1: Setup
1. **Generate an Encryption Key**:
   Uncomment the `generate_key` function in the code to create a unique encryption key. Run the function once to generate a file named `key.key`. This key is essential for encrypting and decrypting your passwords.
   ```python
   def generate_key():
       key = Fernet.generate_key()
       with open("key.key", "wb") as key_file:
           key_file.write(key)
   ```

2. **Save the Key Securely**:
   Store the `key.key` file in a secure location. Without it, you will not be able to decrypt your saved passwords.

### Step 2: Running the Program
1. Execute the script:
   ```bash
   python number_guessing_game.py
   ```
2. Enter your master password when prompted. This is used in combination with the encryption key to secure your passwords.

### Step 3: Using the Program
- **Add Passwords**:
  Choose the `add` mode to save new account credentials. You will need to provide the account name and password.

- **View Passwords**:
  Choose the `view` mode to display saved credentials. The passwords will be decrypted and shown alongside the account names.

- **Quit**:
  Enter `q` to exit the program.

### Note
- If the `passwords.txt` file does not exist, it will be created automatically.
- Ensure the `key.key` file is in the same directory as the script when running the program.

## Code Structure

- **Key Management**:
  - `load_key()`: Loads the encryption key from `key.key`.
  - `generate_key()`: Generates a new encryption key (commented out by default).

- **Password Manager Functions**:
  - `add()`: Saves encrypted account credentials to `passwords.txt`.
  - `view()`: Reads and decrypts account credentials from `passwords.txt`.

- **Main Program Loop**:
  Handles user input for adding, viewing, or quitting.

## Files

- **`number_guessing_game.py`**: Main script containing the program logic.
- **`key.key`**: Encryption key file (must be generated and secured).
- **`passwords.txt`**: File storing encrypted account credentials (automatically created).

## Security Tips

1. Do not share the `key.key` file or the master password.
2. Store `passwords.txt` in a secure directory.
3. Backup your `key.key` file to avoid data loss.

## Dependencies

- `cryptography`: A Python library for secure encryption and decryption.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
