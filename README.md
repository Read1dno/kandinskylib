# KandinskyLib

A library for interacting with the Kandinsky AI image generation API.

## Installation

You can install the library using pip:

```bash
pip install kandinskylib
```

## Usage

# Generator

```python
from kandinskylib import Kandinsky

api_key = 'your_api_key'
secret_key = 'your_secret_key'
client = Kandinsky(api_key, secret_key)

# Generate an image
response = client.generate_image(
    prompt="A cat in sunglasses",
    scale="3:2",
    style="UHD",
    negative_prompt="Bright colors, neon colors",
    path="./image/generated_image.jpg"
)
print(response)
```

# Available Styles

```python
from kandinskylib import styles

# List available styles
styles_response = styles()
print(styles_response)
```
