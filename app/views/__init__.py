from .home import render_home
from .full_style import render_full_image_style
from .subject_style import render_subject_style
from .background_style import render_background_style
from .dual_style import render_dual_style

PAGES = {
    "Home": render_home,
    "Full Style": render_full_image_style,
    "Subject Style": render_subject_style,
    "Background Style": render_background_style,
    "Dual Style": render_dual_style,
}