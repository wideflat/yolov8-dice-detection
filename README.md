# yolov8-dice-detection

## <div align="left">Objective</div>
I used custom dataset and trained yolov8 model. The dataset I used is 6 sided dice dataset available at roboflow.
[https://public.roboflow.com/object-detection/dice]

## Steps

<summary>Preparation</summary>
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

### 1. Preparation


