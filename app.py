from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def upload_form():
    # Render an HTML form for uploading images.
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    try:
        # Convert bytes to a PIL image
        input_image = Image.open(file.stream)
        
        # Remove the background
        output_image = remove(input_image)
        
        # Convert PIL image to byte array for sending as file
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')  # Save your PIL image to a byte array
        img_byte_arr.seek(0)  # Move to the beginning of the byte array
        
        # Set the output filename
        output_filename = 'processed_image.png'
        
        return send_file(
        img_byte_arr,
        mimetype='image/png',  # Ensure the MIME type matches your image format
        as_attachment=True,
        download_name='processed_image.png'  # This specifies the name of the file to be downloaded
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
