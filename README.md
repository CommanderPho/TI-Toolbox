
# Temporal Interference Toolbox

[![Docker Pulls](https://img.shields.io/docker/pulls/idossha/simnibs?cacheSeconds=86400)](https://hub.docker.com/r/idossha/simnibs)
[![GitHub Release](https://img.shields.io/github/v/release/idossha/TI-toolbox?cacheSeconds=3600)](https://github.com/idossha/TI-toolbox/releases)
[![GitHub License](https://img.shields.io/github/license/idossha/TI-toolbox?cacheSeconds=86400)](https://github.com/idossha/TI-toolbox/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/idossha/TI-toolbox/branch/main/graph/badge.svg)](https://codecov.io/gh/idossha/TI-toolbox)

Releases, guides, and wiki please see: [https://idossha.github.io/TI-Toolbox/](https://idossha.github.io/TI-Toolbox/)

Reference: https://www.biorxiv.org/content/10.1101/2025.10.06.680781v3

## Contact

For inquiries regarding the TI-Toolbox, please contact:

- **Ido Haber**
- Email: ihaber@wisc.edu



# Pho TODO for Dev

# Workflow Summary
What you want to do	Command
Interactive development shell	./dev/bash_dev/loader_dev.sh
Run unit tests	./tests/test.sh --unit-only
Full test suite	./tests/test.sh --verbose
Run the GUI app (normal mode)	Use the Desktop App or ./loader.sh


# Scratch

PROJECT_DIR="/mnt/PROJECT" SUBJECT_ID="phohale" simnibs_python /ti-toolbox/ti-toolbox/cli/../analyzer/main_analyzer.py --m2m_subject_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/m2m_phohale --field_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/Simulations/flex_subcortical_labeling_8_max_maxTI_optimized/TI/niftis/flex_subcortical_labeling_8_max_maxTI_optimized_TI_subject_TI_max.nii.gz --space voxel --analysis_type cortical --output_dir /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/Simulations/flex_subcortical_labeling_8_max_maxTI_optimized/Analyses/Voxel/whole_head_template_coregistered --atlas_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/m2m_phohale/segmentation/template_coregistered.mgz --whole_head --visualize


flex_subcortical_labeling_51_mean_maxTI_optimized

simnibs_python /ti-toolbox/ti-toolbox/cli/../analyzer/main_analyzer.py --m2m_subject_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/m2m_phohale --field_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/Simulations/flex_subcortical_labeling_26_mean_maxTI_optimized/TI/niftis/flex_subcortical_labeling_26_mean_maxTI_optimized_TI_subject_TI_max.nii.gz --space voxel --analysis_type cortical --output_dir /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/Simulations/flex_subcortical_labeling_26_mean_maxTI_optimized/Analyses/Voxel/whole_head_template_coregistered --atlas_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/m2m_phohale/segmentation/template_coregistered.mgz --whole_head --visualize



Copyable command (for manual execution):
PROJECT_DIR="/mnt/PROJECT" SUBJECT_ID="phohale" simnibs_python /ti-toolbox/ti-toolbox/cli/../analyzer/main_analyzer.py --m2m_subject_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/m2m_phohale --field_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/Simulations/flex_subcortical_labeling_17_mean_maxTI_optimized/TI/niftis/flex_subcortical_labeling_17_mean_maxTI_optimized_TI_subject_TI_max.nii.gz --space voxel --analysis_type cortical --output_dir /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/Simulations/flex_subcortical_labeling_17_mean_maxTI_optimized/Analyses/Voxel/whole_head_template_coregistered --atlas_path /mnt/PROJECT/derivatives/SimNIBS/sub-phohale/m2m_phohale/segmentation/template_coregistered.mgz --whole_head --visualize



Available Simulations:
-------------------
  1. NewTwo
  2. flex_rh_DK40_35_focality_maxTI_mapped
  3. flex_rh_DK40_35_focality_maxTI_optimized
  4. flex_rh_DK40_35_max_maxTI_mapped
  5. flex_rh_DK40_35_max_maxTI_optimized
  6. flex_rh_DK40_6_focality_maxTI_mapped
  7. flex_rh_DK40_6_focality_maxTI_optimized
  8. flex_subcortical_labeling_10_mean_maxTI_mapped
  9. flex_subcortical_labeling_10_mean_maxTI_optimized
 10. flex_subcortical_labeling_11_mean_maxTI_mapped
 11. flex_subcortical_labeling_11_mean_maxTI_optimized
 12. flex_subcortical_labeling_17_mean_maxTI_mapped
 13. flex_subcortical_labeling_17_mean_maxTI_optimized
 14. flex_subcortical_labeling_26_mean_maxTI_mapped
 15. flex_subcortical_labeling_26_mean_maxTI_optimized
 16. flex_subcortical_labeling_28_mean_maxTI_mapped
 17. flex_subcortical_labeling_28_mean_maxTI_optimized
 18. flex_subcortical_labeling_49_mean_maxTI_mapped
 19. flex_subcortical_labeling_49_mean_maxTI_optimized
 20. flex_subcortical_labeling_51_mean_maxTI_mapped
 21. flex_subcortical_labeling_51_mean_maxTI_optimized
 22. flex_subcortical_labeling_52_mean_maxTI_mapped
 23. flex_subcortical_labeling_52_mean_maxTI_optimized
 24. flex_subcortical_labeling_53_mean_maxTI_mapped
 25. flex_subcortical_labeling_53_mean_maxTI_optimized
 26. flex_subcortical_labeling_54_max_maxTI_mapped
 27. flex_subcortical_labeling_54_max_maxTI_optimized
 28. flex_subcortical_labeling_54_mean_maxTI_mapped
 29. flex_subcortical_labeling_54_mean_maxTI_optimized
 30. flex_subcortical_labeling_8_max_maxTI_mapped
 31. flex_subcortical_labeling_8_max_maxTI_optimized