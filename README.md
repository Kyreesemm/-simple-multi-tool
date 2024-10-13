# Simple Multi-Tool

Simple Multi-Tool is a versatile tool designed to perform a variety of tasks, ranging from file management to network utilities. This tool is perfect for developers, system administrators, and anyone who needs a set of handy utilities in one place.

## Features

- File system operations
- Network utilities
- Image processing
- Text manipulation
- Security tools
- Entertainment features
- And more!

## Installation

To get started with Simple Multi-Tool, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kyreesemm/-simple-multi-tool.git
   ```
2. **Go to the repository directory:**
   ```bash
   cd simple-multi-tool
   ```
3. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   ```
   ```bash
   .\venv\Scripts\activate
   ```
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Using:**
   ```bash
   python main.py [chapter] [command]
   ```

## Building an executable file

To make it easier for you to use this utility, you can assemble it into an executable file and add it to the 'PATH' in Windows, for example, so that it always works from the command line.

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```
2. **Create an executable file:**
   ```bash
   pyinstaller --onefile main.py
   ```

After this, you have one executable file, which you can place for example in the System32 folder and use from the command prompt.



## Utility commands

My utility has fairly simple commands, but they may not be convenient to type. I will not write all the commands here, since you can view the rest by entering the command:
   ```bash
   python main.py --help
   ```
Or if you have built a utility, then use this command:
   ```bash
   main --help
   ```

Here are some of the commands that are available in Simple multi-tool:
- 'file_system'     Some operations with the file system.
- 'network_utils'   Network operations.
- 'image_tools'     Some image processing.
- 'dev_utils'       A few development tools.
- 'entertainment'   Of course, there are also entertainments.
There are also other sections that have their own functionality.

**Command Syntax:**

To use a tool from a certain section, you need to write the following command (I’ll show you with an example without compiling it into an executable file):
   ```bash
   python main.py [chapter] [command]
   ```
And so, where 'chapter' you write the section you need, for example: 'file_system'. And where there is 'command' you write for example: '--list'.

View all chapters:
   ```bash
   python main.py --help
   ```
View commands for a specific chapter:
   ```bash
   python main.py [chapter (example: file_system)] --help
   ```



## Improvements

In this project, I will always welcome suggestions for improvements. I want this project to be useful, so I will wait for requests for improvements.


## LICENSE

This project is licensed under the Creative Commons Attribution 4.0 International License. You are free to share and adapt the material for any purpose, even commercially, as long as you provide appropriate credit, provide a link to the license, and indicate if changes were made. See the [LICENSE](LICENSE) file for more details.
