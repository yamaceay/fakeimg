import os
from selenium import webdriver
from nqdm import nqdm
import time
import io
from PIL import Image

driver = webdriver.Chrome(executable_path="chromedriver.exe")

def get_face():
    time.sleep(2)
    driver.get("https://www.thispersondoesnotexist.com")
    face = driver.find_element_by_id("face")
    return face.screenshot_as_png

def save_face(i, img=get_face()):
    if not os.path.exists("faces"):
        os.mkdir("faces")
    with open(f"faces/face_{i}.png", "wb") as file:
        data = img
        file.write(data)

def save_faces(n1, n2, imgs=None):
    if imgs is None:
        imgs = [get_face() for x in nqdm(range(n1, n2))]
    for i, img in zip(range(n1, n2), imgs):
        save_face(i, img)

save_faces(0, 500)

driver.quit()