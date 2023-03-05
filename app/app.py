from flask import Flask, request, jsonify
from views import enigma, de_enigma

app = Flask(__name__)


# Rota para a página do enigma
@app.route('/enigma', methods=['POST'])
def enigma_view():
    json_data = request.get_json()

    # Check if 'msg' field is present
    if 'msg' not in json_data:
        return jsonify({'error': 'No "msg" field present in request'}), 400
    
    msg = json_data['msg']
    
    # Get 'seed' field if present
    if 'seed' in json_data:
        seed = json_data['seed']
    else:
        seed = None
    
    # Process the received data
    msg = enigma(msg, seed)
    
    # Return a response
    response = {'msg': msg}
    if seed is not None:
        response['seed'] = seed
    
    return jsonify(response), 200

# Rota para a página de decifrar o enigma
@app.route('/de-enigma', methods=['POST'])
def de_enigma_view():
    json_data = request.get_json()

    # Check if 'msg' field is present
    if 'msg' not in json_data:
        return jsonify({'error': 'No "msg" field present in request'}), 400
    
    msg = json_data['msg']
    
    # Get 'seed' field if present
    if 'seed' in json_data:
        seed = json_data['seed']
    else:
        seed = None
    
    # Process the received data
    msg = de_enigma(msg, seed)
    
    # Return a response
    response = {'msg': msg}
    if seed is not None:
        response['seed'] = seed
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)