# Steganography Tool

This Python script allows users to perform steganography, hiding data within images using the least significant bit (LSB) method.

## Installation

1. Install the required libraries:

    bash
    pip install Pillow customtkinter numpy
    

2. Clone this repository:

    bash
    git clone https://github.com/danush2705/Steganography-Tool.git
    

3. Navigate to the repository folder:

    bash
    cd Steganography-tool
    

4. Run the script:

    bash
    python newui.py
    

## Features

- *Encoding*: Hide data within PNG images using the LSB method.
- *Decoding*: Extract hidden data from steganographic images.
- *Encryption*: Securely encrypt data before embedding it in images.
- *Image Quality Metrics*: Calculate Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM) to evaluate image quality.

## Usage

1. Run the script to open the Steganography Tool interface.

2. Choose between encoding or decoding data.

3. For encoding:
    - Select an image file to hide data in.
    - Enter the data to be hidden.
    - Click the "Encrypt & Encode" button for secure encoding.

4. For decoding:
    - Select a steganographic image containing hidden data.
    - Click the "Decode" button to extract the hidden data.

## FAQ

- *What is Steganography?*

  Steganography is the practice of hiding information within other data.

- *How does the Steganography Tool work?*

  This tool hides data within images using the least significant bit (LSB) method.

- *Is the embedded data secure?*

  Yes, we use encryption for data security.

- *What types of files can I use?*

  PNG images are primarily supported.

- *Is there a data size limit?*

  Yes, there's a maximum capacity, and you'll be alerted if you exceed it.

- *How can I prevent data loss?*

  Keep backups and records of embedded images.

- *Can I extract data from images?*

  Yes, the tool can extract hidden data.

- *Does it affect image quality?*

  There is a minimal impact on image quality.

- *Commercial use allowed?*

  Yes, but follow data privacy laws.

- *Where can I get support?*

  Contact our support team for assistance.

## Credits

- [Pillow](https://python-pillow.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [NumPy](https://numpy.org/)

## License

This project is licensed under the [MIT License](LICENSE).
