# Computer Vision and Pattern Recognition

## Mini Project: Image Classification

### Description

The police commissioner has given you a labled image dataset.

Your task is to classify them between two classes:

- 0 : Normal (No weapon is seen)
- 1 : Weapon (A weapon can be detected)

Develop an algorithm to detect any possible dangers to help alert the relevant authorities.

### Core Objectives

1. Prepare the given dataset.
  - Download the dataset from [here](https://drive.google.com/drive/folders/1qm0jkcNPWN3jBj7jQiZhndbKUsx4Ozfl).
  - Download 7zip from [here](https://www.7-zip.org/download.html).
  - E.g. Data cleaning, visualization, pre-processing, normalization.
2. Minimally, develop a vanilla baseline classifier to discriminate between the two classes above the baseline recognition rate of 50% from a random classifier.
3. Provide improvements for the baseline method.
4. Show empirical observations. 
  - E.g. Plot learning curves, recognition rates, scores, numerical results.
5. Present your work CLEARLY and nicely.

## TODO
- [x] Download dataset
- [ ] Data cleaning (remove duplicates, etc.)
- [x] Data augmentation (flip, rotate, crop, etc.)
- [x] Baseline model (Pixel input -> Fully connected layers -> Softmax)
- [ ] Poster

### Possible improvements
- [X] Improvement 1 (Convolution layers)
- [x] Improvement 2 (Regularization: Dropout, Batch normalization)
- [x] Improvement 3 (Loss function: Cross entropy, L2 loss)
- [x] Improvement 4 (Optimizer: SGD, Adam)
- [x] Improvement 5 (Hyperparameter tuning: Learning rate decay, batch size, etc.)
- [ ] Improvement 6 (Over/Under sampling)
- [ ] Improvement 7 (Feature extraction methods from lectures)

## For Local Setup
1. Clone this project repository
2. Download the dataset from link: https://drive.google.com/drive/folders/1qm0jkcNPWN3jBj7jQiZhndbKUsx4Ozfl
3. Unzip the dataset and move the `frames` folder into the root of the project
  - The folder structure should look like this:
  ```
  .
  ├── frames
  │   ├── test
  │   │   ├── norm
  │   │   └── weap
  │   └── train
  │       ├── norm
  │       └── weap
  ├── data_preperation.ipynb
  ```
4. (Optional) Create and activate a python environment and install the necessary dependencies listed in `requirements.txt`
5. Run `data_preperation.ipynb` to create the prepared dataset; all work should be done with this dataset
6. Proceed with your work
