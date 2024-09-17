# Django HTML Minifier

This Python script minifies HTML in Django templates while preserving Django template tags such as `{% %}`, `{{ }}`, and `{# #}`.

## Features

- Minifies HTML content while preserving Django template syntax.
- Accepts input and output file paths as command-line arguments.
- Optimizes Django templates by removing unnecessary whitespace and reducing file size.

## Requirements

- Python 3.6+
- `htmlmin` package

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/hoshmandent/django-html-minifier.git
   cd django-html-minifier
   ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from the command line, passing the input and output file paths as arguments:

```bash
python minify_django_html.py /path/to/input/template.html /path/to/output/minified_template.html
```

## Example
For example, to minify a Django template:

```bash
python minify_django_html.py admin/templates/theme_bar.html admin/templates/theme_bar.min.html
```

This will read the `theme_bar.html` file, minify the HTML content, and save the result as `theme_bar.min.html`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.