from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import h5py
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import io

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model ResNet50 tanpa top layer
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Load fitur dan nama file dari HDF5
with h5py.File('model/features.h5', 'r') as h5f:
    features = np.array(h5f['features'])
    image_names = [name.decode('utf-8') for name in h5f['image_names']]

# Load narasi
narrative_df = pd.read_csv('narasi-karmawibhangga.csv')
narrative_dict = {
    row['filename']: {
        'tema': row['Tema'],
        'narasi': row['Narasi'],
        'makna_moral': row['Makna moral']
    } for _, row in narrative_df.iterrows()
}

# Fungsi preprocessing query image
def preprocess_query_image_bytes(file_bytes, target_size=(224, 224)):
    img = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    img = img.resize(target_size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

# Fungsi cari gambar serupa
def find_similar(query_feature, features, top_k=3):
    sims = cosine_similarity(query_feature, features)[0]
    top_indices = sims.argsort()[-top_k:][::-1]
    return top_indices, sims[top_indices]
@app.get('/')
def index():
    return 'Halo dunia!'
@app.post('/predict')
async def predict(image: UploadFile = File(...)):
    try:
        contents = await image.read()
        query_img = preprocess_query_image_bytes(contents)
        query_feature = model.predict(query_img)

        indices, scores = find_similar(query_feature, features, top_k=1)

        idx = indices[0]
        score = scores[0]
        fname = image_names[idx]
        narasi = narrative_dict.get(fname, {
            'tema': 'Tidak diketahui',
            'narasi': 'Tidak ditemukan',
            'makna_moral': 'Tidak tersedia'
        })
        result = {
            'filename': fname,
            'similarity': float(score),
            **narasi
        }
        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})