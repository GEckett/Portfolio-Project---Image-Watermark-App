import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark App")

        # Create a frame to hold the image label
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        # Image label
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        # Title text
        self.title_label = tk.Label(self.root, text="Image Watermark App", font=("Helvetica", 16, "bold"))
        self.title_label.pack()

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # Open Image button with icon
        self.open_icon = Image.open("open_icon.png")  # Replace with the actual path to your open icon
        self.open_icon = self.open_icon.resize((30, 30))
        self.open_icon = ImageTk.PhotoImage(self.open_icon)
        self.open_button = tk.Button(self.buttons_frame, text="Open Image", command=self.open_image,
                                     image=self.open_icon, compound=tk.TOP)
        self.open_button.grid(row=0, column=0, padx=10)

        # Add Watermark button with icon
        self.add_icon = Image.open("add_icon.png")  # Replace with the actual path to your add icon
        self.add_icon = self.add_icon.resize((30, 30))
        self.add_icon = ImageTk.PhotoImage(self.add_icon)
        self.add_watermark_button = tk.Button(self.buttons_frame, text="Add Watermark", command=self.add_watermark,
                                              image=self.add_icon, compound=tk.TOP)
        self.add_watermark_button.grid(row=0, column=1, padx=10)

        # Save Image button with icon
        self.save_icon = Image.open("save_icon.png")  # Replace with the actual path to your save icon
        self.save_icon = self.save_icon.resize((30, 30))
        self.save_icon = ImageTk.PhotoImage(self.save_icon)
        self.save_button = tk.Button(self.buttons_frame, text="Save Image", command=self.save_image,
                                     image=self.save_icon, compound=tk.TOP)
        self.save_button.grid(row=0, column=2, padx=10)

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
                original_image = Image.open(self.image_path).convert("RGBA")

                # Watermark image
                watermark_path = "watermark.png"  # Update this path
                watermark = Image.open(watermark_path).convert("RGBA")

                # Resize watermark to fit the original image
                watermark = watermark.resize(original_image.size)

                # Blend the images
                watermarked_image = Image.alpha_composite(original_image, watermark)

                # Save the watermarked image as PNG
                watermarked_image.save(save_path, format="PNG")

                # Provide feedback
                messagebox.showinfo("Image Saved", "The watermarked image has been saved.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)

    root.mainloop()







