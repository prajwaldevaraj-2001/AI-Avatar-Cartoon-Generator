from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Function to apply a cartoon filter
def cartoonize(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"

        img = Image.open(file)
        img = np.array(img)
        cartoon_img = cartoonize(img)
        
        # Convert back to PIL image
        img_pil = Image.fromarray(cartoon_img)
        img_io = io.BytesIO()
        img_pil.save(img_io, "JPEG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/jpeg")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
