# Phishing Detector

## Table of Contents
-----------------

1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Solution Overview](#solution-overview)
4. [Technical Details](#technical-details)
5. [Features](#features)
6. [Prerequisites](#prerequisites)
7. [Installation](#installation)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction
---------------

Phishing Detector is a project that aims to detect phishing websites using machine learning algorithms. The project uses a combination of features extracted from the website's HTML, CSS, and JavaScript code to identify potential phishing attempts. This project is designed to be a robust and scalable solution for detecting phishing websites, and can be used by individuals, organizations, and internet service providers to protect against phishing attacks.

## Problem Statement
-------------------

Phishing is a type of cybercrime that involves tricking individuals into revealing sensitive information, such as login credentials or financial information, by masquerading as a trustworthy entity. Phishing attacks can have devastating consequences, including financial loss, identity theft, and compromised national security. Despite the many efforts to combat phishing, it remains a significant threat to online security.

## Solution Overview
-------------------

Phishing Detector uses a machine learning-based approach to detect phishing websites. The project involves the following components:

1. **Data Collection**: A dataset of labeled phishing and legitimate websites is collected.
2. **Feature Extraction**: Features are extracted from the website's HTML, CSS, and JavaScript code, including metadata, keyword extraction, and syntax analysis.
3. **Model Training**: A machine learning model is trained on the extracted features to classify websites as phishing or legitimate.
4. **Model Deployment**: The trained model is deployed as a web application that takes a website URL as input and returns a classification result.

## Technical Details
-------------------

Phishing Detector uses the following technologies:

1. **Python**: The project is built using Python 3.8+.
2. **Machine Learning**: The project uses scikit-learn and TensorFlow for machine learning tasks.
3. **Web Development**: The project uses Flask for web development.
4. **Database**: The project uses SQLite for data storage.

## Features
------------

Phishing Detector includes the following features:

1. **Real-time Classification**: The project provides real-time classification results for input website URLs.
2. **Accurate Detection**: The project uses a robust machine learning model to detect phishing websites with high accuracy.
3. **Scalability**: The project is designed to handle a large volume of website classifications.
4. **User-friendly Interface**: The project provides a user-friendly interface for users to input website URLs and view classification results.

## Prerequisites
----------------

* Python 3.8+
* Virtual environment (e.g., `virtualenv`, `conda`)
* Git Large File Storage (LFS)

## Installation
--------------

### Step 1: Create a Virtual Environment

Create a new virtual environment using your preferred method. For example, using `virtualenv`:
```bash
virtualenv -p python3.8 venv
```
Activate the virtual environment:
```bash
source venv/bin/activate
```
### Step 2: Install Dependencies

Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```
### Step 3: Install Git LFS

Install Git LFS using the following command:
```bash
git lfs install
```
### Step 4: Track Large Files

Track large files using Git LFS:
```bash
git lfs track "data.zip"
```
Commit the `.gitattributes` file:
```bash
git add .gitattributes
git commit -m "Track large file with Git LFS"
```
### Step 5: Clone the Repository

Clone the repository using the following command:
```bash
git clone https://github.com/ybigsur5/phishing-detector.git
```
## Usage
-----

### Training the Model

Train the model using the following command:
```bash
python train.py
```
### Testing the Model

Test the model using the following command:
```bash
python test.py
```
### Using the Model

Use the model to detect phishing websites by running the following command:
```bash
python detect.py <website_url>
```
Replace `<website_url>` with the URL of the website you want to check.

## Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
-------

This project is licensed under the MIT License. See the `LICENSE` file for details.

## .gitignore
------------

The following files and directories are ignored by Git:
```markdown
# Ignore build outputs
build/
dist/

# Ignore log files
*.log

# Ignore temporary files
*.tmp
*.swp

# Ignore IDE settings
.vscode/
.idea/

# Ignore virtual environment
venv/
```
## Result


![Screenshot at 2025-03-27 06-58-43](https://github.com/user-attachments/assets/608a5368-f8ba-47d3-926b-2d94285f7544)
![Screenshot at 2025-03-27 06-58-24](https://github.com/user-attachments/assets/5c32b1f3-d83c-43a5-87e2-373283e88756)
