from ultralytics import YOLO
import datetime


def save(model):
    try:
        success1 = model.export(format="onnx")  # export the model to ONNX format
    except:
        pass



def run_train(yaml):
    now = datetime.datetime.now()
    print('Start', yaml, now)
    model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)
    model.train(data=yaml, epochs=300, patience=30)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    save(model)
    now = datetime.datetime.now()
    print('End', yaml, now)
    print(metrics)


if __name__ == '__main__':
    # run_train("original.yaml")
    # run_train("strong_augumented_2.yaml")
    run_train("original.yaml")

    import os
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
