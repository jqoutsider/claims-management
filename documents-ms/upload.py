import os
from google.cloud import storage
from werkzeug.datastructures import FileStorage
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cloud storage bucket
BUCKET_NAME = "documents-claims-bucket"

def upload_file_to_bucket(request):
    if request.method != 'POST':
        return jsonify({"error": "Forbiden method"}), 405

    # Verifica que el request sea multipart/form-data
    if not request.content_type.startswith('multipart/form-data'):
        return jsonify({"error": "The content type must be multipart/form-data"}), 400

    # Start Google Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)

    # Extract the file from the request
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "There is no file attached"}), 400

    # check and get the file metadata required
    fileName = file.filename
    uploadedBy = request.form.get("uploadedBy")
    claimId = request.form.get("claimId")

    if not uploadedBy or not claimId:
        return jsonify({"error": "The uploadedBy and claimId are required"}), 400

    try:
        # Create a bucket reference to a new file
        blob = bucket.blob(fileName)
        
        # add the metadata to the file
        blob.metadata = {
            uploadedBy: uploadedBy,
            claimId: claimId,
            fileName: fileName
        }
        
        # Upload the file to the bucket
        blob.upload_from_file(file.stream, content_type=file.mimetype)
        
        return jsonify({"mensaje": "File uploaded succesfully", "file": fileName}), 200
    except Exception as e:
        print(f"Error on file upload: {e}")
        return jsonify({"error": f"error on file upload: {str(e)}"}), 500