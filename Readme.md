
# Background Removal Flask App

This Flask application provides a simple web interface for users to upload images and automatically remove their backgrounds using the `rembg` library. Designed with an iOS-inspired, minimalist aesthetic, it's perfect for quick, on-the-fly background removal tasks.

## Features

- **Easy-to-use Interface**: A clean, minimalist upload form inspired by iOS design.
- **Support for Multiple Image Formats**: Accepts JPG, JPEG, PNG, and WEBP formats.
- **Instant Download**: Processed images are returned immediately for download.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or later
- pip (Python Package Installer)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/YourRepositoryName.git
cd YourRepositoryName
```

2. Create and activate a virtual environment:

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, execute:

```bash
python app.py
```

Navigate to `http://localhost:5000/` in your web browser to use the application.

## Usage

1. Click on the "Select image to upload" button and choose an image from your device.
2. Click on the "Upload Image" button to submit the image.
3. The processed image will be automatically downloaded to your device.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Designed & Developed by [Harsh](https://github.com/Hxrshrathore) with ❤️
