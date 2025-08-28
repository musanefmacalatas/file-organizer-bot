import os
import shutil

# 📂 Target folders (auto-create kung wala pa)
folders = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".psd"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar"],
}

# 🗂️ Ask user for folder name
folder_name = input("Enter the folder name to organize (e.g., Documents, Pictures, Downloads): ")

# 🏠 Build full path
source_folder = os.path.join(os.path.expanduser("~"), folder_name)

# ✅ Check if folder exists
if not os.path.exists(source_folder):
    print(f"❌ Error: The folder '{folder_name}' does not exist in your User directory.")
else:
    print(f"📂 Organizing files in: {source_folder}\n")

    # 🗂️ Organize files
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            for folder, extensions in folders.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    target_folder = os.path.join(source_folder, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"✅ Moved {filename} → {folder}")
                    break

    print("\n🎉 Done! Your folder is now organized.")
