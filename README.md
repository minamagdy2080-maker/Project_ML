# Bioinformatics DNA Toolkit Demo

This repository is a starter project for diploma students to practice using Git and managing Python environments.

### 1. Clone the Repository
Open your terminal and run the following command to download the project:
```bash
git clone https://github.com/Dinayahia1718/dna-toolkit-demo.git
cd dna-toolkit-demo
```

### 2. Set Up Your Conda Environment
Using a virtual environment ensures that your bioinformatics tools and Python versions don't conflict with other projects.

```bash
# Create a new environment named 'bio-env' with Python 3.10
conda create --name precision-ml python=3.11 -y

# Activate the environment
conda activate precision-ml
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
