import yaml
import re
import sys

def validate_footnotes(file_path):
    """
    Validate that all footnotes in sso_pricing lines have matching definitions.

    Args:
        file_path (str): Path to the YAML file to validate.

    Returns:
        list: List of validation errors.
    """
    errors = []
    footnotes = set()
    sso_pricing_footnotes = set()

    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Extract footnotes from footnotes entries
    for entry in data:
        if 'footnotes' in entry:
            match = re.match(r'\[\^(.+)\].*', entry['footnotes'])
            if match:
                footnote_name = match.group(1)
                footnotes.add(footnote_name)

    # Extract footnotes from other entries
    for entry in data:
        for key, val in entry.items():
            if key == "footnotes":
                continue
            match = re.search(r'\[\^([^]]+)\]', str(val))
            if match:
                sso_pricing_footnote = match.group(1)
                sso_pricing_footnotes.add(sso_pricing_footnote)

    # Check for footnotes without definitions
    for footnote in sso_pricing_footnotes:
        if footnote not in footnotes:
            errors.append(f"Footnote for '{footnote}' is referenced but has no definition.")

    # Check for definitions without footnotes
    for footnote in footnotes:
        if footnote not in sso_pricing_footnotes:
            errors.append(f"Footnote for '{footnote}' is defined, but is not used.")

    if errors:
        raise ValueError("Validation errors:\n" + "\n".join(errors))

if __name__ == "__main__":
    try:
        validate_footnotes(sys.argv[1])
        print("No validation errors found.")
    except ValueError as e:
        print(f"Found Validation Errors: {e}")
        print()
        print(f"Hint: make sure the footnote is declared with a 'footnote:' key and a value that starts with the footnote name, for example: 'footnote: [^vendorname]'. The footnote must also be used in another field to be valid and get displayed. For example:  'sso_pricing: $5/u/m [^vendorname]'." )
        sys.exit(1)
