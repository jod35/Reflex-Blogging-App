import reflex as rx
from reflex_blog.state.post_state import PostState


def update_post_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.link("Edit Post", size="1")),
        rx.dialog.content(
            rx.dialog.title("Edit Post"),
            rx.flex(
                rx.text(
                    "Title",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    default_value=PostState.post["title"],
                    placeholder="Enter your title",
                ),
                rx.text(
                    "Body",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.text_area(
                    name="body",
                    placeholder="Enter The Post Body",
                    
                    value=PostState.post["body"],
                ),
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        color_scheme="gray",
                        variant="soft",
                    ),
                ),
                rx.dialog.close(
                    rx.button("Save"),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
    )
