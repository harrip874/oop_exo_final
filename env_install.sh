
#!/bin/bash

# =====================================
# Mini exercise - Environment installer
# =====================================

# Feature 1: Pretty printing function
pretty_print() {
    printf "\n%s\n\n" "$1"
}

# Feature 2: Detect operating system
pretty_print "Detecting operating system..."

echo "Operating system: $OSTYPE"

# Feature 3: Check and install Python 3
pretty_print "Checking Python 3..."

if command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is already installed."
    python3 --version
else
    echo "Python 3 is not installed. Installing..."

    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update
        sudo apt install -y python3
    else
        echo "Unsupported operating system."
        exit 1
    fi
fi

# Feature 4: Check pip
pretty_print "Checking pip..."

if python3 -m pip --version; then
    echo "Pip is available."
else
    echo "Installing pip..."

    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt install -y python3-pip
    fi
fi

# Feature 5: Install Jupyter Notebook
pretty_print "Installing Jupyter Notebook..."

python3 -m pip install --user notebook

# Feature 6: macOS health check
if [[ "$OSTYPE" == "darwin"* ]]; then
    pretty_print "Checking Homebrew health..."
    brew doctor
fi

# End
pretty_print "Environment setup completed!"
