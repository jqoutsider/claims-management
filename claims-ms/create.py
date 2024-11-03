import functions_framework
from google.cloud import firestore
db = firestore.Client(database="claims-db")

@functions_framework.http
def create(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    if request.method == 'POST':
        data = request.get_json()
        print("Received request with data ={}", data['id'])

        doc = db.collection("Claim").document(data['id'])
        doc.set({
            'description': data['description'],
            'userId': data['userId'],
            'productId': data['productId'],
            'incidentDate': data['incidentDate'],
            'creationDate': data['creationDate'],
            'veredict': data['veredict'],

        })
    return 'Claim with id={} created!'.format(data['id']), 201