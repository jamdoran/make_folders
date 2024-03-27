import os

# Folder names to create
folders = ['Capture', 'HQX', 'Restored', 'Movies']

# Create each folder in the current directory
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print ('Folders created')

