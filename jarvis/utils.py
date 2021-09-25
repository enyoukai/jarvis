import yaml

def safe_load(file):
	with open(file, 'r') as f:
		return yaml.safe_load(f)