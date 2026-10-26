# 🚀 Ultimate Guide to Python Virtual Environments & Conda

Welcome to your quick and easy cheat sheet for managing Python environments, packages, and terminal commands! 

---

## 💻 Basic Terminal Commands

Before jumping into environments, here are some handy commands:

*   **Check installed libraries:**
    ```bash
    pip list
    ```
    *(This shows how many and which libraries are currently installed in your active Python setup.)*

*   **Check Python version & enter the console:**
    ```bash
    python
    ```
    *(This opens the Python REPL where you can test code. To get out, type `exit()` and press Enter.)*

---

## 🤔 Why Do We Need Virtual Environments (venv)?

Virtual environments act like isolated containers for your projects. Instead of installing every library directly onto your computer, you keep project-specific tools in their own bubble. This prevents version conflicts and keeps your system clean!

*Note: If you have **Anaconda** installed, you start in a default environment called the `base` environment.*

---

## 🐍 Conda Environment Cheat Sheet

### 1. Create a New Environment
To create a fresh environment, use this command:
```bash
conda create -n env_name python=3.10 -y
```
*(Replace `env_name` with your desired name, and `3.10` with your desired Python version. The `-y` automatically says "yes" to prompts.)*

### 2. Activate Your Environment
Whenever you create a new virtual environment, you **must activate it** before you can use it:
```bash
conda activate env_name
```

### 3. See All Environments
Want to see a list of every environment you've created?
```bash
conda env list
```
*(Look for the `*` symbol—it tells you which environment is currently active!)*

### 4. Delete an Environment
If you no longer need an environment and want to clean up:
```bash
conda remove --name env_name --all
```

---

## 💾 Saving Space on Your C: Drive (Local Environments)

If you create too many environments globally, your C: Drive might get full! To avoid this, you can create environments directly inside your specific project folder.

**Create an environment in the current folder:**
```bash
conda create --prefix .\env_name python=3.10 -y
```

**Activate that local environment:**
```bash
conda activate .\env_name
```

---

## 📦 Packages & `requirements.txt`

*   **Where do packages come from?** All Python packages and libraries live on [PyPI.org](https://pypi.org). 

Instead of installing packages one by one, you can list all the dependencies your project needs inside a file called `requirements.txt`.

**Install everything at once:**
```bash
pip install -r requirements.txt
```

**The Result:** 
Now, if you type `pip list`, you will see a clean list containing **only** your necessary libraries (and the specific dependency packages they rely on). No extra clutter! ✨