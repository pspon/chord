import importlib.resources
import os
import shutil
from mako.template import Template
import mako.runtime
import urllib.request
import uuid

# undefined template values default to empty strings
mako.runtime.UNDEFINED = ""

class Chord(object):
    template_file_path = "default.tmpl"
    static_files = [
        ('js/d3.v7.min.js', 'js/d3.v7.min.js'),
        ('js/d3-chord.js', 'js/d3-chord.js'),
        ('js/popper.min.js', 'js/popper.min.js'),
        ('js/tippy.min.js', 'js/tippy.min.js'),
        ('css/tippy.translucent.css', 'css/tippy.translucent.css')
    ]

    def __init__(
        self,
        matrix,
        names,
        label_style='default',
        pull=None,
        output_dir="."
    ):
        self.html = self.load_template()
        self.matrix = matrix
        self.names = names
        self.label_style = label_style
        self.pull = pull
        self.output_dir = output_dir

    def load_template(self):
        """Loads the template file from the installed package."""
        with importlib.resources.open_text("chord", self.template_file_path) as file:
            return file.read()

    def _copy_static_files(self):
        """Copies the necessary static files to the output directory while maintaining the folder structure."""
        for source, destination in self.static_files:
            # Get the correct resource path using importlib.resources.files
            source_path = importlib.resources.files("chord").joinpath(source)
            destination_path = os.path.join(self.output_dir, destination)
            destination_dir = os.path.dirname(destination_path)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)  # Create subdirectories if they don't exist
            # Copy the file
            shutil.copy(source_path, destination_path)

    def render_html(self):
        """Generates the HTML using the Mako template."""
        self._copy_static_files()  # Ensure CSS/JS are copied before rendering HTML
        self.html = Template(self.html).render(
            matrix=self.matrix,
            names=self.names,
            label_style=self.label_style,
            pull = self.pull
        )

    def return_html(self):
        """Generates the HTML using the Mako template."""
        self._copy_static_files()  # Ensure CSS/JS are copied before rendering HTML
        return Template(self.html).render(
            matrix=self.matrix,
            names=self.names,
            label_style=self.label_style,
            pull = self.pull
        )

    def to_html(self, filename="out.html"):
        """Outputs the generated HTML to a HTML file, along with the necessary static files."""
        self.render_html()
        file = open(filename, "w")
        file.write(self.html)
        file.close()

    def show(self):
        """Outputs the generated HTML to a Jupyter Lab output cell."""
        self.render_html()
        from IPython.display import display, HTML
        display(HTML(self.html))
