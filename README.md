# Animal and Insect Identifier

A Python web app that lets users upload an image of an animal or insect, identifies the species, and provides information about it using Gemini’s AI API.

---

## Table of Contents

1. [Features](#features)  
2. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
3. [Usage](#usage)  
4. [How It Works](#how-it-works)  
5. [Project Structure](#project-structure)  

---

## Features

- Upload an image of any animal or insect  
- Identify the species (or closest match)  
- Display relevant facts and background info about the identified creature  
- Powered by Gemini AI for enhanced recognition and details  

---

## Getting Started

### Prerequisites

- Python 3.7+  
- (Optional) Virtual environment tool (`venv` or `virtualenv`)  
- Gemini API key (or whichever AI service you configure)  
- Dependencies listed in `requirements.txt`  

### Installation

```bash
# Clone the repository
git clone https://github.com/nole444/Animal-and-Insect-Identifier.git
cd Animal-and-Insect-Identifier

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
