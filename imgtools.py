import os
from PIL import Image
from IPython.display import display

def load_image(image_path): 
    """
    Đọc ảnh từ đường dẫn cho trước và trả về đối tượng ảnh
    Arguments: image_path
    Returns: đối tượng hình ảnh
    """
    try: 
        image02 = Image.open(image_path)
        return image02
    except Exception as e:
        print('Lỗi khi đọc hình ảnh từ:', image_path, e)
        return None

def is_image_file(image_path):
    """
    return: True - nếu là hình ảnh
            False - nếu không phải
    """
    extensions = ('.png', '.jpeg', '.jpg', '.gif', '.bmp')
    return image_path.lower().endswith(extensions)

def get_image_list(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path):
                img = load_image(file_path)
                if img is not None:
                    image_list.append(img)
    return image_list
