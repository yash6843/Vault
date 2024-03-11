# Vault - A Simple password managing tool

This is a simple command-line interface based password manager and generator written in python.
It allows you to store your passwords securely and generate random, strong passwords.

## Features

- Store and manage passwords
- Search entry functionality
- Remove entry functionaliy
- View a list of all saved entries
- Generate random passwords of a desired length
- Password encryption
- Transcript/Make encrypted file with all entries , encryption password can be given by user

## Getting Started

Prerequisites:

To run this program, you will need to have a python interpreter installed on your computer.

## Usage

When you run the program, you first need to enter a 4 digit PIN to log-in
By default the PIN is **2024**
Later on you can change it too.

![alt text](https://media.discordapp.net/attachments/1216395074967965737/1216789045917777981/image.png?ex=6601aa1b&is=65ef351b&hm=a2569d933879f1a608856600f1387bc4abf0b8a172b6daa5fe4ad5de8a674fbe&=&format=webp&quality=lossless&width=1060&height=506)

Password Manager Menu:

1.  Add entry
2.  Remove entry
3.  Search entry
4.  List all entries
5.  Change log-in PIN
6.  Password Generator
7.  Generate a trnascript (Makes a encrypted zip file with all the data)
8.  Quit

## Generate password

To generate a strong, random password. Enter the option respective to the pass-gen i.e 6 and then enter the desired password length. The program will generate a random, strong password of the length and will display it on the screen

## Security

This program encrypts the saved passwords using a simple encrypting algorithm by cryptocode module. This provides some level of security, but it is not recommended to store highly sensitive passwords.
