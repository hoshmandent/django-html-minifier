import re
import htmlmin
import argparse

def minify_django_html(input_file, output_file):
    """
    Minify a Django template without affecting Django template tags.

    Args:
        input_file (str): The path to the Django template input file.
        output_file (str): The path to the output file where minified HTML will be saved.
    """
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Define regex patterns for Django template tags
    django_tags = r'{%.*?%}|{{.*?}}'

    # Split the content into Django tags and HTML
    parts = re.split(f'({django_tags})', content)

    # Minify only the HTML parts
    for i in range(len(parts)):
        if not re.match(django_tags, parts[i]):
            parts[i] = htmlmin.minify(parts[i], remove_empty_space=True, remove_all_empty_space=True)

    # Join the parts back together
    minified_content = ''.join(parts)

    # Write the minified content to the output file
    with open(output_file, 'w') as file:
        file.write(minified_content)

    print(f"Minified HTML has been saved to {output_file}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Minify a Django HTML template while preserving template tags.")
    
    # Add arguments for input and output file paths
    parser.add_argument('input_file', type=str, help="Path to the input Django template file")
    parser.add_argument('output_file', type=str, help="Path to save the minified HTML file")

    # Parse the arguments
    args = parser.parse_args()

    # Call the minification function with the provided arguments
    minify_django_html(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
