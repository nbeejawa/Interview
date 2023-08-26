import zipfile

def extract_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(dest_dir)            

if __name__ == '__main__':
    extract_archive("C:/Users/beeja/OneDrive/Documents/GitHub/Interview/compressed.zip", 
                    "C:/Users/beeja/OneDrive/Documents/GitHub/Interview")