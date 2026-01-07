---
name: Fix whole_head analysis detection and display
overview: "The issue is that when \"Region: All\" is selected in the Analysis GUI, the analysis completes successfully but doesn't appear in the NIFTI viewer. This is because: (1) `detect_voxel_analyses` only looks for NIfTI files directly in analysis directories, but whole_head analysis stores NIfTI files in subdirectories; (2) The loading logic doesn't handle the whole_head directory structure. The fix will modify both detection and loading to handle whole_head analyses."
todos:
  - id: update-detect-voxel-analyses
    content: Modify detect_voxel_analyses() to detect whole_head directories by checking for subdirectories containing NIfTI files
    status: pending
  - id: update-loading-logic
    content: Update analysis loading logic to handle whole_head case by checking subdirectories when region name starts with 'whole_head_'
    status: pending
    dependencies:
      - update-detect-voxel-analyses
---

# Fix whole_head Analysis Detection and Display

## Problem Analysis

When "Region: All" is selected in the Analysis GUI panel:

1. Analysis completes successfully and creates directory: `Analyses/Voxel/whole_head_{atlas_name}/`
2. NIfTI files are stored in subdirectories: `Analyses/Voxel/whole_head_{atlas_name}/region_name/{region_name}_ROI.nii.gz`
3. `detect_voxel_analyses()` in `nifti_viewer_tab.py` only checks for NIfTI files directly in directories, missing the whole_head case
4. Even if detected, the loading logic expects files directly in the analysis directory

## Solution

### 1. Update `detect_voxel_analyses()` method

**File**: `ti-toolbox/gui/nifti_viewer_tab.py` (lines 106-132)Modify to detect whole_head analyses by:

- Checking if a directory contains subdirectories with NIfTI files
- If found, add the parent directory name (e.g., "whole_head_{atlas_name}") to the regions list
- Keep existing behavior for region-specific analyses (NIfTI files directly in directory)

### 2. Update analysis loading logic

**File**: `ti-toolbox/gui/nifti_viewer_tab.py` (lines 982-1015)Modify to handle whole_head case:

- Check if selected region name starts with "whole_head_"
- If yes, look for NIfTI files in subdirectories
- Options for display:
- Option A: Load all region NIfTI files from subdirectories (may be too many)
- Option B: Create/load a combined visualization if it exists
- Option C: Load the first available region file as a representative sample
- **Recommended**: Option C initially, with potential enhancement to Option B later

### 3. Testing considerations

- Verify whole_head analyses appear in the analysis region combo box
- Verify selecting whole_head analysis loads and displays correctly
- Ensure region-specific analyses still work as before

## Implementation Details

### Detection Logic

```python
# In detect_voxel_analyses():
# For each directory in Analyses/Voxel/:
#   - Check for .nii* files directly (existing behavior)
#   - Also check if it contains subdirectories with .nii* files (new for whole_head)
#   - If subdirectories found, add parent directory to regions list
```



### Loading Logic

```python
# In load_files_for_freeview():
# If region_name starts with "whole_head_":
#   - Look in subdirectories for NIfTI files
#   - Load the first available file (or all files, depending on chosen option)
# Else:
#   - Use existing logic (files directly in directory)




```