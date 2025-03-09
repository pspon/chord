from mako.template import Template
import mako.runtime
import urllib.request
import uuid

# undefined template values default to empty strings
mako.runtime.UNDEFINED = ""


class Chord(object):
    template_file_path = "default.tmpl"

    with open(template_file_path, 'r') as file:
        template = file.read()

    def __init__(
        self,
        matrix,
        names,
        label_style = 'default'
    ):
        self.html = Chord.template
        self.matrix = matrix
        self.names = names
        self.label_style = label_style

    def __str__(self):
        return self.html

    def render_html(self):
        """Generates the HTML using the Mako template."""
        self.html = Template(Chord.template).render(
            matrix=self.matrix,
            names=self.names,
            label_style=self.label_style
        )

    def return_html(self):
        """Generates the HTML using the Mako template."""
        self.html = Template(Chord.template).render(
            matrix=self.matrix,
            names=self.names,
            label_style=self.label_style
        )
        return(self.html)

    def to_html(self, filename="out.html"):
        """Outputs the generated HTML to a HTML file. """
        self.render_html()
        file = open(filename, "w")
        file.write(self.html)
        file.close()

    def show(self):
        """Outputs the generated HTML to a Jupyter Lab output cell."""
        self.render_html()
        from IPython.display import display, HTML

        display(HTML(self.html))
