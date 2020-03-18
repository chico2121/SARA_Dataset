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
    `-- |-- Character_Id
        `-- |-- Action_Id
            `-- |-- The number of frames of the action
                `-- |-- Motion variations
                    |   |-- motion.npy (full-frame motion)
                    `-- |-- motions
                        |-- |-- 1.npy (fixed-frame motion)
                        |-- |-- 2.npy
                        |-- |-- ...
   ```

## Acknowledgments
This code borrows heavily from [2D-Motion-Retargeting](https://github.com/ChrisWu1997/2D-Motion-Retargeting) 