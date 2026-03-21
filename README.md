# Bioinformatics DNA Toolkit Demo

This repository is a starter project for diploma students to practice using Git and managing Python environments.

### 1. Clone the Repository
Open your terminal and run the following command to download the project:
```bash
git clone [https://github.com/YOUR_USERNAME/dna-toolkit-demo.git](https://github.com/YOUR_USERNAME/dna-toolkit-demo.git)
cd dna-toolkit-demo
```

### 2. Set Up Your Environment
It is best practice to use a virtual environment so you don't mess up your system Python.

```bash
# Create the environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Requirements
Install the necessary bioinformatics libraries listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Run the Script
Test that everything is working:

```Bash
python scripts/dna_utils.py
