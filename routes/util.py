from app import app
from error_handles import forbidden
from flask import jsonify, request
from pyzbar.pyzbar import decode
from PIL import Image

def bar_code(image):
    text = ""
    img = Image.open("BarCode.jpeg")
    all_info = decode(img)
    for i in all_info:
        text += (i.data.decode("utf-8"))
    return text

@app.route("/image", methods=["POST"])
def process_image():
    file = request.files['image']
    file.save('img1.jpg')
    roll_no = bar_code('img1.jpg')
    return jsonify({"roll_no": roll_no})


if __name__ == "__main__":
    app.run(debug=True)