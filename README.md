# SARA Dataset

Synthetic dataset using for model training in our paper [_A Body Part Embedding Model With Datasets for Measuring Human Motion Similarity in 2D_](https://www.overleaf.com/1277422435svrhgrnqbpgv), ECCV 2020.

## Prerequisites

- Python 3
- Numpy

## Downloading and Preprocessing the SARA

- Download and extract the SARA dataset ([Google drive](https://drive.google.com/open?id=1SeFdqo_jMkVDLyykSV0LXFLSccrWdGx0))

- Clone this repository

- Preprocess the dataset (split motion into fixed frames)
  
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