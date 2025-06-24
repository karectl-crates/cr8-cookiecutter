import sys
import re

destination_type = "{{ cookiecutter.destination_type }}"
destination_name = "{{ cookiecutter.destination_name }}"

def validate_destination_name(name):
    if not name or not name.strip():
        return False, "Destination name cannot be blank."
    if ' ' in name or not re.match(r'^[a-zA-Z0-9_-]+$', name):
        return False, "Destination name must be a single word (no spaces, only letters, numbers, underscores, and hyphens allowed)."
    return True, ""


# Only validate if destination_type is filestore
if destination_type == "filestore":
    is_valid, error_msg = validate_destination_name(destination_name)
    
    #if not is_valid:
    #    raise ValueError(f"VALIDATION_ERROR: {error_msg}")