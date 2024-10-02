# Categorize a Password as Strong or Weak

This project is a Python-based password strength categorizer that helps users determine whether their password is strong or weak based on predefined rules. This tool aims to promote good password practices by highlighting weak passwords and encouraging stronger ones.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Password Strength Criteria](#password-strength-criteria)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Password security is an important aspect of protecting your online presence. This project provides a simple script that categorizes a password as either "strong" or "weak" based on various factors such as length, use of special characters, numbers, and more. The goal is to provide a user-friendly tool that can evaluate passwords and encourage users to create stronger ones.

## Features

- Categorizes passwords as **strong** or **weak**
- Provides feedback to help users improve their password strength
- Easy-to-use command line interface
- Lightweight and requires minimal dependencies

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YSayaovong/Categorize-A-Password-as-Strong-or-Weak.git
    cd Categorize-A-Password-as-Strong-or-Weak
    ```

2. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script using Python:

python categorize_password.py

You will be prompted to enter a password, and the program will evaluate its strength based on predefined rules.

Password Strength Criteria
The script uses the following criteria to categorize a password as strong or weak:

Length: The password must be at least 8 characters long.
Uppercase and Lowercase Letters: The password must contain both uppercase and lowercase letters.
Numbers: The password must include at least one numeric character.
Special Characters: The password should contain at least one special character (e.g., !, @, #, $, etc.).
If a password meets all the criteria, it is categorized as strong; otherwise, it is categorized as weak.

Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

You can copy and paste this code into your `README.md` file on GitHub.
