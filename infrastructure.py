from ravello_sdk import *
import json
import os

client = RavelloClient()
client.login(os.environ["VMPROV_USER"], os.environ["VMPROV_PASSWORD"])

def get_app_id(app_name):
        app_id=0
        for app in client.get_applications():
                if app['name'].lower() == app_name.lower():
                        app_id = app['id']
                        break
        return app_id

def get_vms_from_app(app_name):
	result = []
	app_id = get_app_id(app_name)
	app = client.get_application(app_id)
	vms = client.get_vms(app_id, level='deployment')
	for vm in vms:
		print('\tName: {0:<40}, State: {1}'.format(vm['name'].encode('utf-8'), vm['state']))
		vm_desc = vm.get('description', None)
		owner = None
		if vm_desc and vm_desc.startswith("user="):
			owner = vm_desc[5:]

		result_map = {
				"id": vm['id'],
				"name": vm['name'].encode('utf-8'),
				"state": vm['state']
			}

		if owner:
			result_map["owner"] = owner

		result.append(result_map)

	return result

def get_vm(app_name, vmid):
    app_id = get_app_id(app_name)
    app = client.get_application(app_id)
    vm = client.get_vm(app_id, vmid)
    return vm

def acquire_vm(app_name, vmid):
    vm = get_vm(app_name, vmid)
    vm['description'] = 'user=grussell'
    vm = client.update_vm(app, vm)
    client.publish_application_updates(app)

def release_vm(app_name, vmid):
    vm = get_vm(app_name, vmid)
    vm['description'] = ''
    vm = client.update_vm(app, vm)
    client.publish_application_updates(app)

def get_images():
    images = client.get_images()
    for image in images:
        print image

    return images
