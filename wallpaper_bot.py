import os
from bing_image_downloader import downloader

# Define parameters
search_query = "4K nature wallpapers"
download_folder = r"C:\Users\himan\Desktop\Folder_of_Bot\wallpapers"
image_limit = 50  # Number of images to download

# Download images
downloader.download(
    search_query,
    limit=image_limit,
    output_dir=download_folder,
    adult_filter_off=True,
    force_replace=False
)

# The path to downloaded images
download_path = os.path.join(download_folder, search_query)

# Rename images sequentially from 1.jpg to n.jpg
for idx, filename in enumerate(sorted(os.listdir(download_path)), start=1):
    old_path = os.path.join(download_path, filename)
    new_path = os.path.join(download_folder, f"{idx}.jpg")  # Rename to 1.jpg, 2.jpg, ...
    os.rename(old_path, new_path)

# Remove the extra folder created by the downloader
os.rmdir(download_path)

print("Download and renaming complete!")
print()
