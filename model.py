import os
import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models
from dotenv import load_dotenv
from google import genai
import re

# --- Load Environment Variables ---
load_dotenv()  # Loads variables from .env into os.environ
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")  # Should be set in your .env file

# --- Google GenAI Setup ---
client = genai.Client(api_key=GENAI_API_KEY)

# --- Image Classification Setup ---
model = models.resnet50(pretrained=True)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

def classify_image(file_path):
    """
    Classify an image using the pre-trained ResNet50 model.
    Returns only the common name (without any leading identification number)
    of the top predicted label.
    """
    try:
        img = Image.open(file_path).convert("RGB")
        input_tensor = preprocess(img)
        input_batch = input_tensor.unsqueeze(0)
        if torch.cuda.is_available():
            input_batch = input_batch.to("cuda")
            model.to("cuda")
        with torch.no_grad():
            output = model(input_batch)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        top_prob, top_catid = torch.topk(probabilities, 1)
        with open("imagenet_classes.txt", "r") as f:
            labels = [line.strip() for line in f.readlines()]
        # Get the full predicted label from the file.
        full_label = labels[top_catid.item()]
        # Remove any leading numbers and whitespace (e.g., "138 " or "138:")
        cleaned_label = re.sub(r'^\d+\s*[:\-]?\s*', '', full_label)
        # If the label contains a comma, take only the first part as the common name.
        common_name = cleaned_label.split(",")[0].strip()
        return common_name
    except Exception as e:
        return f"Classification error: {e}"

def get_details_from_gemini(label):
    """
    Uses the Gemini API via Google GenAI to fetch details about the given label.
    Filters out unwanted summary content.
    """
    prompt = f"Give me information about {label}"
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        text = response.text.strip()
        # Optionally filter out unwanted summary text (customize as needed)
        if "Summary:" in text:
            text = text.split("Summary:")[0].strip()
        return text
    except Exception as e:
        return f"Error: Unable to fetch details from Gemini via GenAI. {e}"
