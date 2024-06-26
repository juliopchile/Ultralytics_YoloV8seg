import os
from ultralytics import FastSAM, SAM, YOLO, NAS
from config import backbones_directory, yolo_models, sam_models, fast_sam_models, nas_models


def model_path(name: str) -> str:
    """
    Constructs the model path given the model name.

    Args:
        name (str): The name of the model.

    Returns:
        str: The full path to the model file.
    """
    return os.path.join(backbones_directory, f"{name}.pt")


# ? Descargar modelos
def download_models(models_to_download: list = None):
    """
    Downloads and loads the models specified in the list. If no list is provided, all models are downloaded.

    Args:
        models_to_download (list, optional): List of model names to download. Defaults to None.

    Returns:
        None
    """

    if models_to_download is None:
        models_to_download = yolo_models + sam_models + fast_sam_models + nas_models

    for model in models_to_download:
        if model in yolo_models:
            YOLO(model_path(model))
        elif model in sam_models:
            SAM(model_path(model))
        elif model in fast_sam_models:
            FastSAM(model_path(model))
        elif model in nas_models:
            NAS(model_path(model))


# ? Cargar modelos
def load_ultralytics_YOLO(model_name='yolov8n-seg'):
    return YOLO(model_path(model_name))


def load_ultralytics_SAM(model_name='sam_b'):
    return SAM(model_path(model_name))


def load_ultralytics_FastSAM(model_name='FastSAM-s'):
    return FastSAM(model_path(model_name))


def load_ultralytics_NAS(model_name='yolo_nas_s'):
    return NAS(model_path(model_name))


if __name__ == "__main__":
    # Descargar todos los modelos
    # download_models(downloadable_models)

    # Descargar solo los necesarios
    download_models(yolo_models[3:7])

    # Cargar un modelo y hacer inferencia con la camara (YoloNas no funciona)
    model = load_ultralytics_YOLO("yolov9e-seg")
    model.info()
    model.predict(source=0, save=False, show=True)


