#!/usr/bin/env python3
try:
    import typer
except ModuleNotFoundError:
    print("Module not found error (Check the setup section of the readme)")


def readify(path: str, port: int = 5000):
    """
    Readify - An Awesome CLI tool for Rendering README to your browser.

    :cli_param path: Path of the file \n
    :cli_param port: --port [port]
    """
    try:
        import markdown
        from flask import Flask
        import markdown.extensions.fenced_code
        import markdown.extensions.codehilite
        from pygments.formatters import HtmlFormatter

        app = Flask(__name__)
    except ImportError:
        print("Module not found error (Check the setup section of the readme)")

    @app.route("/")
    def index():
        try:
            readme_file = open(f"{path}", "r")
        except FileNotFoundError:
            print("404: That file couldn't be found or you don't have permission to view it")
        
        md_template_string = markdown.markdown(
            readme_file.read(), extensions=["fenced_code", "codehilite"]
        )

        # Generate Css for syntax highlighting
        formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
        css_string = formatter.get_style_defs()
        md_css_string = "<style>" + css_string + "</style>"

        md_template = md_css_string + md_template_string
        return md_template

    if __name__ == "__main__":
        app.run(port=port)


if __name__ == '__main__':
    typer.run(readify)
