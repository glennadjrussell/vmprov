#!venv/bin/python
from flask import Flask, jsonify
import infrastructure as infra

app = Flask(__name__)

DEFAULT_APP_NAME = "Engineering Operations"

@app.route('/api/v1.0/vms', methods=['GET'])
def get_vms():
	return jsonify({
		"vms": infra.get_vms_from_app(DEFAULT_APP_NAME)
	})

@app.route('/api/v1.0/vms/<int:id>/acquire', methods=['GET'])
def acquire_vm(id):
	infra.acquire_vm(DEFAULT_APP_NAME,id)
	return jsonify({"status": "success"})

@app.route('/api/v1.0/vms/<int:id>/release', methods=['GET'])
def release_vm(id):
	infra.release_vm(DEFAULT_APP_NAME,id)
	return jsonify({"status": "success"})

@app.route('/api/v1.0/images', methods=['GET'])
def get_images():
	return jsonify({
		"images": infra.get_images()
	})

if __name__ == '__main__':
	app.run(debug=True)
