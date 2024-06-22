# HT Generator Project

Welcome to the **HT Generator** project, a versatile and user-friendly tool for generating various `.htaccess` and `.htpasswd` configurations. This project, created by [Leandro Sepulveda](http://www.leandrosepulveda.com), aims to simplify the creation and management of these critical files for web security and access control.

## Features

### Main Menu
The main menu provides a straightforward interface for selecting various options related to `.htaccess` and `.htpasswd` management. Simply type the number corresponding to the desired option and press ENTER.

### Options

1. **Htpasswd Generator**: 
   - Generate `.htpasswd` files for password-protecting directories on Unix/Linux/MacOS/BSD systems.
   - Prompts for username, password, and folder location for file generation.

2. **Htaccess Authentication**: 
   - Create `.htaccess` files for basic authentication.
   - Prompts for authentication name, `.htpasswd` file location, and folder location for file generation.

3. **Hotlink Protection of Images**: 
   - Prevent unauthorized websites from linking directly to your images.
   - Prompts for allowed domains, whether to allow blank referers, files to protect, and folder location for file generation.

4. **Block IPs with .htaccess**: 
   - Block specific IP addresses from accessing your website.
   - Prompts for blocked IP addresses and folder location for file generation.

5. **Block Hitbots with .htaccess**: 
   - Block unwanted bots and crawlers from your website.
   - Prompts for blocked domains, redirection URL (optional), and folder location for file generation.

6. **Exit**: 
   - Exit the program with a friendly farewell message.

## Usage

To use the HT Generator, simply run the `views.py` script. You'll be greeted with a header displaying the project name, version, and author details. Follow the prompts in the main menu to generate the desired `.htaccess` or `.htpasswd` file.

### Example

For generating a `.htpasswd` file:

1. Select option `1` from the main menu.
2. Enter the username and password.
3. Specify the folder location for the generated file.

### Compatibility

- The Htpasswd Generator is supported only on Unix/Linux/MacOS/BSD systems.

## Author

**Leandro Sepulveda**
- [Website](http://www.leandrosepulveda.com)

Enjoy enhanced security and simplified management of your web server configurations with the HT Generator!
