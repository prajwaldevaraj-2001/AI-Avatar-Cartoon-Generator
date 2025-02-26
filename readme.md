# AI Avatar & Cartoon Generator 🎨🤖  

## Overview  
The **AI Avatar & Cartoon Generator** is a Flask-based web application that applies a **cartoon filter** to user-uploaded images. This project utilizes **OpenCV, NumPy, and Pillow (PIL)** for image processing.  

## Features 🚀  
✅ **Upload an Image** – Users can upload any image from their device.  
✅ **Cartoonize Effect** – Converts the image into a cartoon-style representation.  
✅ **Instant Processing** – The output image is generated in real time.  
✅ **Downloadable Output** – Users receive the processed image as a downloadable file.  
✅ **Web-Based UI** – Simple interface using HTML & CSS.  

## Tech Stack 🛠  
- **Backend:** Flask (Python)  
- **Image Processing:** OpenCV, NumPy, Pillow (PIL)  
- **Frontend:** HTML, CSS  
- **Deployment:** GitHub Codespaces (or local server)  

## Installation & Setup ⚙️  

### 1️⃣ Clone the Repository<br> 
git clone https://github.com/yourusername/AI-Avatar-Cartoon-Generator.git<br>
cd AI-Avatar-Cartoon-Generator<br>

2️⃣ Install Dependencies<br>
Ensure you have Python 3.8+ installed. Then, install required packages:<br>
pip install flask opencv-python numpy pillow

3️⃣ Run the Application<br>
python app.py<br>
The app will start at http://127.0.0.1:5000/. Open it in your browser.<br>

Usage 💡<br>
1️⃣ Open the application in your browser.<br>
2️⃣ Click on the "Choose File" button to upload an image.<br>
3️⃣ Click "Generate" to apply the cartoon effect.<br>
4️⃣ Download the cartoonized image.<br>

Known Issues & Fixes 🔧<br>
❌ ImportError: libGL.so.1 not found<br>
👉 Fix: Install OpenCV dependencies using:<br>
sudo apt-get install libgl1-mesa-glx<br>
❌ Large Images Processing Slow<br>
👉 Fix: Resize images before processing.<br>

Future Enhancements 🌟<br>
🚀 More Filters – Add sketch, oil painting, pencil drawing effects.<br>
🎨 Enhanced UI – Improve design using Bootstrap/Tailwind CSS.<br>
📦 Cloud Storage – Allow users to save & share images.<br>


```
Project Structure 📂
AI-Avatar-Cartoon-Generator/
│── static/               # CSS, JS, Images
│── templates/            # HTML Templates
│   ├── index.html        # Main UI Page
│── app.py                # Flask Backend
│── requirements.txt      # Dependencies List
│── README.md             # Project Documentation

