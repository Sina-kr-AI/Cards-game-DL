import os
import shutil
import pathlib

import os
import shutil
import pathlib

new_dir = pathlib.Path("cards_dataset")

def make_subset(base_dir, subset_dir, start, end):

    categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for category in categories:
        dir = new_dir / subset_dir / category
        dir.mkdir(parents=True, exist_ok=True)  
        
        files = sorted(os.listdir(os.path.join(base_dir, category)))  
        fnames = files[start:end]  
        
        for fname in fnames:
            shutil.copyfile(
                src=os.path.join(base_dir, category, fname),
                dst=os.path.join(dir, fname)
            )


make_subset("train","train_data",start=0,end=7624)
make_subset("valid","val_data",start=0,end=265)
make_subset("test","test_data",start=0,end=265)