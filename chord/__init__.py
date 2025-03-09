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
        ('css/tippy.translucent.css', 'css/tippy.translucent.css'),
        ('css/locked.svg', 'css/locked.svg')
    ]

    def __init__(
        self,
        matrix,
        names,
        label_style='default',
        details='',
        details_thumbs='',
        thumbs_width='',
        thumbs_margin='',
        thumbs_font_size='',
        rotate='',
        asymmetric=False,
        width='',
        callout_stroke_width='',
        callout_line_color='',
        colors='',
        directed=False,
        reverse_gradient=False,
        gradient_colors=True,
        chord_stroke_color='',
        arc_stroke_color='',
        chord_stroke_width='',
        arc_stroke_width='',
        labels_color_match=False,
        data_table='',
        data_table_column_width='',
        data_table_show_indices='',
        data_table_unique_column='',
        arc_numbers=False,
        inner_radius_scale='',
        outer_radius_scale='',
        pull='',
        output_dir="."
    ):
        self.html = self.load_template()
        self.matrix = matrix
        self.names = names
        self.label_style = label_style
        self.details = details
        self.details_thumbs = details_thumbs
        self.thumbs_width = thumbs_width
        self.thumbs_margin = thumbs_margin
        self.thumbs_font_size = thumbs_font_size
        self.rotate = rotate
        self.asymmetric = asymmetric
        self.width = width
        self.callout_stroke_width = callout_stroke_width
        self.callout_line_color = callout_line_color
        self.colors = colors
        self.directed = directed
        self.reverse_gradient = reverse_gradient
        self.gradient_colors = gradient_colors
        self.chord_stroke_color = chord_stroke_color
        self.arc_stroke_color = arc_stroke_color
        self.chord_stroke_width = chord_stroke_width
        self.arc_stroke_width = arc_stroke_width
        self.labels_color_match = labels_color_match
        self.data_table = data_table
        self.data_table_column_width = data_table_column_width
        self.data_table_show_indices = data_table_show_indices
        self.data_table_unique_column = data_table_unique_column
        self.arc_numbers = arc_numbers
        self.inner_radius_scale = inner_radius_scale
        self.outer_radius_scale = outer_radius_scale
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
            details=self.details,
            details_thumbs=self.details_thumbs,
            thumbs_width=self.thumbs_width,
            thumbs_margin=self.thumbs_margin,
            thumbs_font_size=self.thumbs_font_size,
            rotate=self.rotate,
            asymmetric=self.asymmetric,
            width=self.width,
            callout_stroke_width=self.callout_stroke_width,
            callout_line_color=self.callout_line_color,
            colors=self.colors,
            directed=self.directed,
            reverse_gradient=self.reverse_gradient,
            gradient_colors=self.gradient_colors,
            chord_stroke_color=self.chord_stroke_color,
            arc_stroke_color=self.arc_stroke_color,
            chord_stroke_width=self.chord_stroke_width,
            arc_stroke_width=self.arc_stroke_width,
            labels_color_match=self.labels_color_match,
            data_table=self.data_table,
            data_table_column_width=self.data_table_column_width,
            data_table_show_indices=self.data_table_show_indices,
            data_table_unique_column=self.data_table_unique_column,
            arc_numbers=self.arc_numbers,
            inner_radius_scale=self.inner_radius_scale,
            outer_radius_scale=self.outer_radius_scale,
            pull=self.pull
        )

    def return_html(self):
        """Generates the HTML using the Mako template."""
        self._copy_static_files()  # Ensure CSS/JS are copied before rendering HTML
        return Template(self.html).render(
            matrix=self.matrix,
            names=self.names,
            label_style=self.label_style,
            details=self.details,
            details_thumbs=self.details_thumbs,
            thumbs_width=self.thumbs_width,
            thumbs_margin=self.thumbs_margin,
            thumbs_font_size=self.thumbs_font_size,
            rotate=self.rotate,
            asymmetric=self.asymmetric,
            width=self.width,
            callout_stroke_width=self.callout_stroke_width,
            callout_line_color=self.callout_line_color,
            colors=self.colors,
            directed=self.directed,
            reverse_gradient=self.reverse_gradient,
            gradient_colors=self.gradient_colors,
            chord_stroke_color=self.chord_stroke_color,
            arc_stroke_color=self.arc_stroke_color,
            chord_stroke_width=self.chord_stroke_width,
            arc_stroke_width=self.arc_stroke_width,
            labels_color_match=self.labels_color_match,
            data_table=self.data_table,
            data_table_column_width=self.data_table_column_width,
            data_table_show_indices=self.data_table_show_indices,
            data_table_unique_column=self.data_table_unique_column,
            arc_numbers=self.arc_numbers,
            inner_radius_scale=self.inner_radius_scale,
            outer_radius_scale=self.outer_radius_scale,
            pull=self.pull
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
