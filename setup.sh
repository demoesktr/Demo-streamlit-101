#!/bin/bash

# Mortgage Calculator Setup Script
# For Unix/Linux/macOS

set -e  # Exit on error

echo "🏠 Mortgage Calculator Setup"
echo "=============================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher from https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "✅ Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the application:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo "  2. Run the app:"
echo "     streamlit run main.py"
echo ""
echo "To run tests:"
echo "     pytest"
echo ""
echo "To deactivate the virtual environment:"
echo "     deactivate"
echo ""
