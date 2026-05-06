import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            # We want the relative path from `Extracted`
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, start=path)
            ziph.write(file_path, arcname)

if __name__ == '__main__':
    extracted_dir = r"c:\Users\Justin\Downloads\LegitNaTo\Extracted"
    revised_dir = r"c:\Users\Justin\Downloads\LegitNaTo\revisedAIA"
    
    if not os.path.exists(revised_dir):
        os.makedirs(revised_dir)
        
    aia_path = os.path.join(revised_dir, "TicTacToe.aia")
    
    with zipfile.ZipFile(aia_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(extracted_dir, zipf)
        
    print(f"Successfully built {aia_path}")
