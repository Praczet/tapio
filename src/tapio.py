#!/usr/bin/env python3

import os
import cairo
import yaml
import gi
import array
from PIL import Image

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
#!/usr/bin/env python3

from gi.repository import Gtk, Gdk, Gio
#!/usr/bin/env python3

# === Configuration ===
PET_NAME = "marvin"
ENTITY_DIR = os.path.join(os.path.dirname(__file__), "../entities", PET_NAME)
CONFIG_FILE = os.path.join(ENTITY_DIR, "config.yaml")
FRAMES_DIR = os.path.join(ENTITY_DIR, "frames")

# === Helper Functions ===


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_gdk_texture_from_file(path):
    """Load Gdk.Texture from file using GdkPixbuf"""
    return Gdk.Texture.new_from_filename(path)


# === Pet Class ===


class PetWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        # Load config
        self.pet_config = load_yaml(os.path.join(ENTITY_DIR, "config.yaml"))

        # Load image texture
        frame_path = os.path.join(FRAMES_DIR, "marvin_idle1.png")
        self.texture = load_gdk_texture_from_file(frame_path)

        # Set up window
        self.set_decorated(False)
        # self.set_type_hint(Gdk.WindowTypeHint.UTILITY)
        self.set_keep_above(True)

        # Set size based on image
        self.set_default_size(self.texture.get_width(), self.texture.get_height())

        # Transparent background setup
        self.set_child(Gtk.DrawingArea())
        self.get_child().set_draw_func(self.on_draw)

        # Set RGBA visual for transparency
        display = self.get_display()
        visual = display.get_rgba_visual()
        if visual is not None and display.is_composited():
            self.set_visual(visual)

        # Center on screen
        self.center_on_screen()

    def center_on_screen(self):
        display = self.get_display()
        monitor = display.get_primary_monitor()
        geometry = monitor.get_geometry()
        scale_factor = monitor.get_scale_factor()

        screen_width = geometry.width // scale_factor
        screen_height = geometry.height // scale_factor

        win_width, win_height = self.get_default_size()
        x = (screen_width - win_width) // 2
        y = (screen_height - win_height) // 2

        self.present()
        self.move(x, y)

    def on_draw(self, area, cr, width, height):
        # Clear background (transparent)
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()

        # Draw Marvin
        Gdk.cairo_set_source_texture(cr, self.texture)
        cr.rectangle(0, 0, self.texture.get_width(), self.texture.get_height())
        cr.fill()


# === Application Class ===


class TapiroApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.tapio.DesktopPet")
        self.connect("activate", self.activate)

    def activate(self, app):
        win = PetWindow()
        win.present()


# === Main ===


def main():
    app = TapiroApp()
    app.run()


if __name__ == "__main__":
    main()
