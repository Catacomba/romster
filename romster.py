import os
import sys
import json
import shutil
from pathlib import Path
from tqdm import tqdm

CONFIG_FILE = "rom_mappings.json"


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"Config file '{CONFIG_FILE}' not found. The config file is expected to be in the same directory as this script.")
        sys.exit(1)

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def check_permissions(src, dst):
    if not os.access(src, os.R_OK):
        print(f"No read permission for source directory: {src}")
        sys.exit(1)

    if os.path.exists(dst):
        if not os.access(dst, os.W_OK):
            print(f"No write permission for destination directory: {dst}")
            sys.exit(1)
    else:
        try:
            os.makedirs(dst, exist_ok=True)
        except PermissionError:
            print(f"Cannot create destination directory: {dst}")
            sys.exit(1)


def collect_files(source_dir):
    files = []
    for root, _, filenames in os.walk(source_dir):
        for name in filenames:
            files.append(os.path.join(root, name))
    return files


def preview(files, mappings, dest_root):
    print("\nPreview (first 5 files):\n")

    shown = 0
    for f in files:
        ext = Path(f).suffix.lower()

        if ext in mappings:
            target_dir = os.path.join(dest_root, mappings[ext])
            target_file = os.path.join(target_dir, os.path.basename(f))

            print(f"Source: {f}")
            print(f"Dest:   {target_file}\n")

            shown += 1
            if shown >= 5:
                break

    if shown == 0:
        print("No matching files found based on config mappings.")

    input("\nPress ENTER to continue or CTRL+C to cancel...")


def copy_files(files, mappings, dest_root):
    total = 0

    # Count only files that match mapping
    for f in files:
        if Path(f).suffix.lower() in mappings:
            total += 1

    if total == 0:
        print("No files to copy.")
        return

    with tqdm(total=total, desc="Copying ROMs", unit="file") as pbar:
        for f in files:
            ext = Path(f).suffix.lower()

            if ext not in mappings:
                continue

            console_folder = mappings[ext]
            dest_dir = os.path.join(dest_root, console_folder)
            os.makedirs(dest_dir, exist_ok=True)

            dest_file = os.path.join(dest_dir, os.path.basename(f))

            # Skip if already exists
            if os.path.exists(dest_file):
                pbar.update(1)
                continue

            try:
                shutil.copy2(f, dest_file)
            except PermissionError:
                print(f"\nPermission denied copying: {f}")
            except Exception as e:
                print(f"\nError copying {f}: {e}")

            pbar.update(1)


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("python rom_sorter.py <source_directory> <destination_root>")
        sys.exit(1)

    source_dir = os.path.abspath(sys.argv[1])
    dest_root = os.path.abspath(sys.argv[2])

    if not os.path.isdir(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        sys.exit(1)

    mappings = load_config()

    check_permissions(source_dir, dest_root)

    print("Scanning files...")
    files = collect_files(source_dir)

    print(f"Found {len(files)} total files.")

    preview(files, mappings, dest_root)

    copy_files(files, mappings, dest_root)

    print("\nDone!")


if __name__ == "__main__":
    main()

