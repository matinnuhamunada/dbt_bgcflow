from pathlib import Path
import shutil
import sys

def get_all_csv(input_path, output_path, extension=".csv"):
    """
    Copy all file with given extension to target directory
    """
    path = Path(input_path)
    for p in path.rglob(f"*{extension}"):
        outfile = Path(output_path) / p.name
        print( outfile )
        shutil.copy(str(p), str(outfile) )
    return

if __name__ == "__main__":
    get_all_csv(sys.argv[1], sys.argv[2])