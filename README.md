Animal and Insect Identifier

A Python web app that lets users upload an image of an animal or insect, identifies the species, and provides information about it using Gemini’s AI API.

Table of Contents

Features

Getting Started

Prerequisites

Installation

Configuration

Usage

How It Works

Project Structure

Features

Upload an image of any animal or insect

Identify the species (or closest match)

Display relevant facts and background info about the identified creature

Powered by Gemini AI for enhanced recognition and details

Getting Started
Prerequisites

Python 3.7+

(Optional) Virtual environment tool (venv or virtualenv)

Gemini API key (or whichever AI service you configure)

Dependencies listed in requirements.txt

Installation
# Clone the repository
git clone https://github.com/nole444/Animal-and-Insect-Identifier.git
cd Animal-and-Insect-Identifier

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

Configuration

Set your Gemini API key as an environment variable:

export GEMINI_API_KEY=your_api_key_here   # macOS/Linux
set GEMINI_API_KEY=your_api_key_here      # Windows

Usage

Run the app:

python main.py


Open your browser and go to:
👉 http://localhost:5000

Upload an image of an animal or insect, and the app will return the identified species along with information about it.

How It Works

The user uploads an image via the web interface.

The app processes the image and sends it to the recognition model.

Gemini AI API is called to provide details about the species.

The results (name + details) are shown back to the user.

Project Structure
├── controller.py        # Handles input/output flow between components
├── model.py             # Recognition logic and Gemini API calls
├── view.py              # UI templates and rendering
├── main.py              # Entry point of the application
├── imagenet_classes.txt # Class labels used for image recognition
└── README.md            # Project documentation
