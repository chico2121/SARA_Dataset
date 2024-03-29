# SARA Dataset

Synthetic dataset used for model training in the IEEE Access paper ["A Body Part Embedding Model With Datasets for Measuring Human Motion Similarity in 2D"](https://ieeexplore.ieee.org/document/9366759). See [project page](https://chico2121.github.io/bpe/) for more details.

## Prerequisites

- Python 3
- Numpy

## Downloading and Preprocessing the SARA

- Download and extract the SARA dataset ([Google drive](https://drive.google.com/open?id=1SeFdqo_jMkVDLyykSV0LXFLSccrWdGx0))

- Clone this repository

- Preprocess the dataset (performs motions split into fixed frames)
  
  ```bash
  python preprocess.py /path/to/the/extracted/
  ```

- The directory structure after preprocessing :

   ```
    SARA_released
    |-- test
    |-- train
    `-- |-- Character_ID
        `-- |-- Motion_ID
            `-- |-- The number of frames
                `-- |-- Motion variations
                    |   |-- motion.npy (full-frame motion)
                    `-- |-- motions
                        |-- |-- 1.npy (fixed-frame motion)
                        |-- |-- 2.npy
                        |-- |-- ...
   ```

## Example of Data Path

  ```
  train/FuseFemaleA/Adventure3/100/Height_1|Activity_-1
  ```
  
  `FuseFemaleA` : Character Id. Each character has different body structure.

  `Adventure3` : Motion category + ID.
  
  `100` : Motion frame length. Even the same motion can vary in length depending on the variation characteristics.

  `Height_1|Activity_-1` : The `Height` characteristic has a value of 1, and the `Activity` characteristic has a value of -1. Values range from -1 to 1.
  
  
## Citation
If you use this dataset for your research, please cite the paper:
```
@ARTICLE{9366759,
  author={J. {Park} and S. {Cho} and D. {Kim} and O. {Bailo} and H. {Park} and S. {Hong} and J. {Park}},
  journal={IEEE Access}, 
  title={A Body Part Embedding Model With Datasets for Measuring 2D Human Motion Similarity}, 
  year={2021},
  volume={9},
  number={},
  pages={36547-36558},
  doi={10.1109/ACCESS.2021.3063302}}
```
