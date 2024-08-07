# KandinskyLib

A library for interacting with the Kandinsky AI image generation API.

## Installation

You can install the library using pip:

```bash
pip install kandinskylib
```

# Usage

## Generator

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

## Available Styles

```python
from kandinskylib import styles

# List available styles
styles_response = styles()
print(styles_response)
```

# Documentation
`class Kandinsky`
`__init__(self, api_key, secret_key)`
Initializes the client for API interaction.

- `api_key` (str): Your API key.
- `secret_key` (str): Your secret key.
`get_model(self)`
Fetches the model ID for image generation.

- Returns: `str` - The model ID or `None` in case of an error.
`generate_image(self, prompt, scale='1:1', style='UHD', negative_prompt="Яркие цвета, кислотные цвета", path='./image/generated_image.jpg')`
Generates an image based on a text prompt.

- `prompt` (str): Text prompt for image generation. The length should be less than 1000 characters.
- `scale` (str): Aspect ratio of the image in the format 'w
'. Default is '1:1'.
- `style` (str): Image style. Default is 'UHD'.
- `negative_prompt` (str): Negative text prompt to exclude unwanted elements.
- `path` (str): Path to save the generated image. Default is './image/generated_image.jpg'.
- Returns: `str` - Message about the result of the generation.
`_check_generation(self, request_id, attempts=10, delay=10)`

Checks the status of image generation.

- `request_id` (str): Generation request ID.
- `attempts` (int): Number of status check attempts. Default is 10.
- `delay` (int): Delay between status check attempts in seconds. Default is 10.
- Returns: `list` - List of generated images in base64 format or raises an exception in case of an error.

`_get_max_resolution(self, scale)`
Determines the maximum resolution of the image based on the aspect ratio.

- `scale` (str): Aspect ratio in the format 'w'.
- Returns: `tuple` - Width and height of the image.

`_save_image(self, base64_str, output_file)`
Saves the image to a file.

- `base64_str` (str): Base64 string of the image.
- `output_file` (str): Path to save the image.
  
`def styles()`
Fetches the list of available styles for image generation.

- Returns: `list` - List of available styles.

## License

This project is licensed under the terms of the MIT License - see the LICENSE file for details.
