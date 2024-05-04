import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text("Simple Blog"),
            class_name="nav-left"
        ),
        rx.box(
            rx.link(
                "Home",
                href="/",
            ),
            rx.link(
                "Create Post",
                href="/create_post",
            ),
            class_name="nav-right"
        ),
        class_name="nav"
    )