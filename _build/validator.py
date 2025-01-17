import yamale

def main():
    schema = yamale.make_schema('_build/schema.yaml')
    data = yamale.make_data('_data/vendors.yml')

    try:
        yamale.validate(schema, data)
        print("Validation successful!")
    except yamale.YamaleError as e:
        print("Validation failed: {e}")
        raise

if __name__ == "__main__":
    main()
