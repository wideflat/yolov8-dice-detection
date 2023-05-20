# yolov8-dice-detection

## <div align="left">Objective</div>
I trained [Ultralytics YOLOv8 model](https://github.com/ultralytics/ultralytics/tree/main) on a custom dataset. The dataset I used is 6 sided dice dataset available at [roboflow]
(https://public.roboflow.com/object-detection/dice).


## Steps

### 1. Preparation
I created a virtual environment in vscode and activate it.
```bash
virtualenv venv --python=python3.9
venv\Scripts\activate
```

I installed pytorch and ultralytics libraries.
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install ultralytics
```
Once the installation is completed, run [1_check_cuda.py](https://github.com/wideflat/yolov8-dice-detection/1_check_cuda.py) and check if cuda is available.


### 2. Data preparation
Run [2_data_preparation.ipynb](https://github.com/wideflat/yolov8-dice-detection/2_data_preparation.ipynb) to dowload dataset.
There are 618 images in total and I set aside 20% of them for validation purpose.


### 3. Train
Run [3_train.py](https://github.com/wideflat/yolov8-dice-detection/3_train.py) and train the YOLOv8N model.
I trained the model with 'epochs=100'.

[`data.yaml`](https://github.com/wideflat/yolov8-dice-detection/data.yaml) is already provided by roboflow together with their 6 sided dice dataset.

The results of the training is saved in [runs/detect/train](https://github.com/wideflat/yolov8-dice-detection/tree/main/runs/detect/train).
Here is some of the outputs.

##### Precision-Recall Curve
<img width="75%" src="https://github.com/wideflat/yolov8-dice-detection/blob/main/runs/detect/train/PR_curve.png">

##### Confusion Matrix
<img width="75%" src="https://github.com/wideflat/yolov8-dice-detection/blob/main/runs/detect/train/confusion_matrix_normalized.png">

#### Metrics
<img src="https://github.com/wideflat/yolov8-dice-detection/blob/main/runs/detect/train/results.png">

#### Labels vs. Predictions

- **Labels**
<img src="https://github.com/wideflat/yolov8-dice-detection/blob/main/runs/detect/train/val_batch0_labels.jpg">

- **Predictions**
<img src="https://github.com/wideflat/yolov8-dice-detection/blob/main/runs/detect/train/val_batch0_pred.jpg">


### 4. Prediction
Pick a random picture from validation dataset and run [4_predict.py](https://github.com/wideflat/yolov8-dice-detection/3_predict.py) to see if the trained model works.
The image with predictions will be popped off in a new window.

...END



