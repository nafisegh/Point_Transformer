# Point Transformer for Toronto-3D (.ply) Point Cloud Segmentation

This repository contains code for preprocessing, training, and evaluating a **Point Transformer** model on the **Toronto-3D** dataset. The dataset consists of `.ply` LiDAR point cloud tiles collected across the City of Toronto.

---

## 📌 Dataset

This project uses the **Toronto-3D** dataset released by Weikai Tan et al.

- GitHub project page:  
  [https://github.com/WeikaiTan/Toronto-3D](https://github.com/WeikaiTan/Toronto-3D)

- Direct Google Drive dataset link:  
  [https://drive.google.com/drive/folders/1oMtUf4kkMg1QCulGFFyW5u3Nweat9brt?usp=share_link](https://drive.google.com/drive/folders/1oMtUf4kkMg1QCulGFFyW5u3Nweat9brt?usp=share_link)

The raw point clouds are provided in **.ply format**.

---

## 📌 Preprocessing

All preprocessing is performed using **`read.py`**.

### Extracted Features

Only the following attributes were used:

- **x**
- **y**
- **z**
- **intensity**

No normalized height or additional LiDAR features were computed.

### Output Format

The script divides the dataset into:

- **train**
- **validation**
- **test**

and saves each split as a **`.npz` file** for efficient loading.

---

## 📌 Model

The model is based on the **Point Transformer** architecture for semantic segmentation.

The implementation is located in:

