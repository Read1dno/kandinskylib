from kandinskylib import Kandinsky
api_key = ''
secret_key = ''

client = Kandinsky(api_key, secret_key)

# Генерация изображения
response = client.generate_image(
    prompt="Кот в солнечных очках",
    scale="3:2",
    style="UHD",
    negative_prompt="Яркие цвета, кислотные цвета",
    path="./image/generated_image.jpg"
)

if response == "generated_image":
    print("generated_image")
else:
    print(response)