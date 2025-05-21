import os
import fitz  # PyMuPDF

# Target folder
folder = r"C:\Users\clint\Desktop\Truck_Presentations"
threshold_size = 25 * 1024 * 1024  # 25MB

for filename in os.listdir(folder):
    if filename.lower().endswith(".pdf"):
        filepath = os.path.join(folder, filename)
        size = os.path.getsize(filepath)

        if size > threshold_size:
            print(f"Compressing: {filename} ({size / (1024 * 1024):.2f} MB)")

            try:
                doc = fitz.open(filepath)
                compressed_path = os.path.join(folder, filename)  # Overwrite same file

                # Save compressed to temp file first
                temp_path = compressed_path.replace(".pdf", "_tmp.pdf")
                doc.save(temp_path, garbage=4, deflate=True, clean=True)
                doc.close()

                os.remove(filepath)  # Remove original
                os.rename(temp_path, compressed_path)  # Rename compressed to original name

                print(f"Compressed and replaced: {filename}")

            except Exception as e:
                print(f"Error compressing {filename}: {e}")
