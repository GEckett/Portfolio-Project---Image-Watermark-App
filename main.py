import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark App")

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.add_watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=10)

        self.image_path = ""
        self.image = None

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.load_image()

    def load_image(self):
        image = Image.open(self.image_path)
        self.image = ImageTk.PhotoImage(image)

    def add_watermark(self):
        if self.image:
            original_image = Image.open(self.image_path)

            # Watermark image
            watermark_path = "watermark.png"  # Update this path
            watermark = Image.open(watermark_path).convert("RGBA")

            # Resize watermark to fit the original image
            watermark = watermark.resize(original_image.size)


            # Blend the images
            watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark)

            self.image = ImageTk.PhotoImage(watermarked_image)

            # Provide feedback
            messagebox.showinfo("Watermark Applied", "Watermark has been applied to the image.")

    def add_text_watermark(self, original_image, text, position):
        watermark = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)

        print("Watermark Size:", watermark.size)

        # Font settings (you can modify as needed)
        font_size = 30
        font = ImageFont.load_default()

        # Draw the text on the image
        draw.text(position, text, font=font, fill=(255, 255, 255, 128))

        watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark)

        return watermarked_image

    def save_image(self):
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                watermarked_image = Image.open(self.image_path)

                # Get the original image size
                original_size = watermarked_image.size

                # Create a new blank image with the same size
                new_image = Image.new("RGBA", original_size, (0, 0, 0, 0))

                # Paste the watermarked image onto the new image
                new_image.paste(watermarked_image, (0, 0))

                # Save the new image as PNG
                new_image.save(save_path, format="PNG")

                # Provide feedback
                messagebox.showinfo("Image Saved", "The watermarked image has been saved.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)

    open_button = tk.Button(root, text="Open Image", command=app.open_image)
    open_button.pack(pady=10)

    root.mainloop()







