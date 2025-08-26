#!/usr/bin/env python3
"""
Clean notebook metadata to fix GitHub rendering issues.
Removes widget metadata and other problematic content.
"""

import json
import os
import nbformat
from pathlib import Path

def clean_notebook_metadata(notebook_path):
    """Clean notebook metadata to fix GitHub rendering issues."""
    print(f"Cleaning {notebook_path}...")
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Clean metadata
    if hasattr(nb, 'metadata'):
        # Remove widget metadata
        if 'widgets' in nb.metadata:
            del nb.metadata['widgets']
            print(f"  - Removed widgets metadata from {notebook_path}")
        
        # Remove other problematic metadata
        problematic_keys = [
            'application/vnd.jupyter.widget-state+json',
            'application/vnd.jupyter.widget-view+json',
            'application/vnd.jupyter.widget-view+json'
        ]
        
        for key in problematic_keys:
            if key in nb.metadata:
                del nb.metadata[key]
                print(f"  - Removed {key} from {notebook_path}")
    
    # Clean cell metadata
    for i, cell in enumerate(nb.cells):
        if hasattr(cell, 'metadata') and cell.metadata:
            # Remove widget metadata from cells
            if 'widgets' in cell.metadata:
                del cell.metadata['widgets']
                print(f"  - Removed widgets metadata from cell {i+1}")
            
            # Remove other problematic cell metadata
            if 'application/vnd.jupyter.widget-view+json' in cell.metadata:
                del cell.metadata['application/vnd.jupyter.widget-view+json']
                print(f"  - Removed widget view metadata from cell {i+1}")
    
    # Write cleaned notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"  ✓ Cleaned {notebook_path}")

def main():
    """Main function to clean all notebooks in the current directory."""
    current_dir = Path('.')
    notebook_files = list(current_dir.glob('*.ipynb'))
    
    if not notebook_files:
        print("No notebook files found in current directory.")
        return
    
    print(f"Found {len(notebook_files)} notebook(s) to clean:")
    for nb_file in notebook_files:
        print(f"  - {nb_file}")
    
    print("\nCleaning notebooks...")
    for nb_file in notebook_files:
        try:
            clean_notebook_metadata(nb_file)
        except Exception as e:
            print(f"  ✗ Error cleaning {nb_file}: {e}")
    
    print("\nNotebook cleaning completed!")

if __name__ == "__main__":
    main()
