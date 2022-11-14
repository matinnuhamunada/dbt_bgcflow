from pathlib import Path
import shutil
import sys

def get_all_csv(input_path, output_path, extension=".csv"):
    """
    Copy all file with given extension to target directory
    """
    path = Path(input_path)
    for p in path.rglob(f"*{extension}"):
        filename = p.name
        copy = True

        if filename == "query_network.csv":
            filename = "bigfam_query_network.csv"

        if filename == "gcf_summary.csv":
            filename = "bigfam_gcf_hits.csv"
        
        if "df" in filename:
            filename = filename.split("df_")[-1]
        
        if "mapping" in filename:
            copy = False
        
        if ("0.40" in filename) or ("0.50" in filename):
            copy = False
        
        if "0.30" in filename:
            filename = f"bigscape_{filename}"
        
        if copy:
            outfile = Path(output_path) / filename
            print( p.name, outfile)
            shutil.copy(str(p), str(outfile) )
    return

if __name__ == "__main__":
    get_all_csv(sys.argv[1], sys.argv[2])