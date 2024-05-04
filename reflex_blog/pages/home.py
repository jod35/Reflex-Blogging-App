import reflex as rx
from reflex_blog.components.navbar import navbar
from reflex_blog.components.posts import post_list


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            post_list(
                
            ),
            class_name="main"
        ),
        class_name="page",
    )