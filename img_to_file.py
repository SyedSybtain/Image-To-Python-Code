from paddleocr import PaddleOCR
ocr = PaddleOCR(use_angle_cls = True)

def create_python_file(file_name, text):
    with open(file_name, 'a', encoding = 'utf-8') as file:
        file.write('\n' + text)
        
img = input('Enter image_name with format : your_image.jpg')
img = img
file_name = input("Enter the name of the Python file (including .py extension): ")
result = ocr.ocr(img)
for res in result:
    for r in res:
        text = r[1][0]
        print(text)
        create_python_file(file_name, text)
print(f"Python file '{file_name}' created successfully.")
