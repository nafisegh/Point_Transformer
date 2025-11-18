README
Point Transformer for Toronto-3D (.ply) Point Cloud Segmentation
This repository contains code for preprocessing, training, and evaluating a Point Transformer model on the Toronto-3D dataset. The dataset consists of .ply LiDAR point cloud tiles collected across the City of Toronto.
📌 Dataset
This project uses the Toronto-3D dataset released by Weikai Tan et al.
GitHub project page:
https://github.com/WeikaiTan/Toronto-3D
Direct Google Drive dataset link:
https://drive.google.com/drive/folders/1oMtUf4kkMg1QCulGFFyW5u3Nweat9brt?usp=share_link
The raw point clouds are provided in .ply format.
📌 Preprocessing
All preprocessing is performed using read.py.
Extracted Features
Only the following attributes were used:
x
y
z
intensity
No normalized height or additional LiDAR features were computed.
Output Format
The script divides the dataset into:
train
validation
test
and saves each split as a .npz file for efficient loading.
📌 Model
The model is based on the Point Transformer architecture for semantic segmentation.
The implementation is located in:
models/point_transformer_seg.py
The trained weights are saved as:
point_transformer_full_model.pth
📌 Training
To train the model, run:
python train.py
train.py:
Loads .npz training and validation data
Builds the Point Transformer segmentation model
Trains using the specified hyperparameters
Saves model checkpoints
📌 Evaluation
To evaluate the model on the test set:
python test.py
test.py loads:
The trained model
The .npz test split
and reports segmentation performance metrics.
📌 Utility Functions
General helper functions (data loading, point cloud utilities, metrics, etc.) are implemented in:
utils.py
📁 Repository Structure
├── models/
│   └── point_transformer_seg.py       # Model implementation
│
├── read.py                            # Preprocessing (.ply → .npz)
├── train.py                           # Training script
├── test.py                            # Evaluation script
├── utils.py                           # Utility functions
│
├── point_transformer_full_model.pth   # Trained model weights
├── README.md                          # Documentation
