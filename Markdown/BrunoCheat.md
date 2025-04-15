# Bruno API testing
## Installation and Usage on Windows

### Installing Bruno on Windows
1. Open **Command Prompt** or **PowerShell** as Administrator.
2. Install Bruno globally using npm:
    ```bash
    npm install -g brunocli
    ```
3. Verify the installation:
    ```bash
    bruno --version
    ```

### Setting Up Your First Collection on Windows
1. **Initialize a Bruno Workspace**:
    ```bash
    bruno init
    ```
    This creates a `.bruno` folder in your current directory.

2. **Create a New Collection**:
    ```bash
    bruno new collection <collection-name>
    ```
    Replace `<collection-name>` with the desired name for your collection.

3. **Add Requests to the Collection**:
    - Navigate to the `.bruno` folder using File Explorer or the terminal.
    - Open the collection folder and create `.yaml` files for your API requests using a text editor like Notepad or VS Code.

4. **Run Requests**:
    ```bash
    bruno run <collection-name>
    ```

### Notes for Windows Users
- Ensure that Node.js and npm are installed and added to your system's PATH.
- Use double quotes (`"`) for paths or arguments if they contain spaces.
- If you encounter permission issues, try running the commands as Administrator.

