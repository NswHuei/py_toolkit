import qrcode
from PIL import Image
import matplotlib.pyplot as plt

def generate_qr(data, filename="qr_code.png", show=True, save=True):
    """
    Generate a QR code from input data.

    Parameters:
    - data (str): The content to encode in the QR code.
    - filename (str): File name to save the QR code image.
    - show (bool): Whether to display the QR code image.
    - save (bool): Whether to save the QR code image to file.
    """
    # Create the QR code image
    qr_img = qrcode.make(data)

    # Show in notebook if requested
    if show:
        plt.imshow(qr_img, cmap="gray")
        plt.axis("off")
        plt.show()

    # Save to file if requested
    if save:
        qr_img.save(filename)
        print(f"QR code saved as {filename}")


# Example usage
generate_qr("https://github.com/your_username", filename="qr_code.png", show=True, save=True)
