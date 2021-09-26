import yaml

def safe_load(file):
	with open(file, 'r') as f:
		return yaml.safe_load(f)

def to_id(str):
	return str.replace(' ', '-').lower()
