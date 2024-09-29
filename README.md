# WioFetch
 NeoFetch for Windows
<img width="635" alt="cmd " src="https://github.com/user-attachments/assets/7a8cbc31-f91a-4424-a620-16b683b93a8b">

 What made me create WioFetch?
	I wanted to make a Windows version for the much loved "Neofetch". We can say that this is the cheap version of Neofetch! AHAHAHAHA
	
What was installed/used to create WioFetch?
		- Visual Basic Code 
		- Programming language: Python
		- Python libraries: psutil, platform, socket and colorama
							- psutil: To obtain CPU usage information, memory, and other process-related information.
							- platform: For platform information such as operating system, architecture and version.
							- socket: To get the machine name.
							- colorama: To color text on the command line, similar to Neofetch.
							- screeninfo: to get the monitor resolution. If not available, returns "Unknown".
							- GPUtil: for information about the GPU, if available. Otherwise, returns a generic message.
									
Commands: pip install psutil colorama
										pip install screeninfo
										pip install gputil

Banner: https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=xvvsb
PyInstaller: Convert my Python code into an executable (.exe) so that a user who does not have Python + Python Libraries be able to use sysinfo.
								    commands: pip install pyinstaller
										  pyinstaller --version
										  pyinstaller --onefile sysinfo.py
