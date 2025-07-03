# 🔐 Random Password Generator - Flask Web App

A simple and elegant password generator built using **Flask**, **Bootstrap**, and **WTForms**. This app takes your name, date of birth, and desired password length to generate three strong, randomized passwords, which you can easily copy to your clipboard.

---

## 🚀 Features

- ✔️ Clean and responsive dark UI using Bootstrap 5
- 🔐 Passwords based on name, DOB, and special characters
- 📅 Date of Birth input via WTForms `DateField`
- 🧪 Input validation using Flask-WTF and WTForms
- 📋 Copy-to-clipboard functionality using JavaScript
- ♻️ Form resets and results clear on page reload
- 🔁 Generate 3 passwords per request using the same input

## Run Locally

```bash
pip install -r requirements.txt
python app.py

## 🔗 Live Demo

[Click here to use the password generator](https://password-generator-svle.onrender.com)