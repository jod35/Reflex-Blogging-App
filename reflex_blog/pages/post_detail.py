import reflex as rx
from reflex_blog.components.navbar import navbar
from reflex_blog.components.posts import post_list
from reflex_blog.state.post_state import PostState
from reflex_blog.components.update_modal import update_post_modal


def post_detail_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.box(
                rx.heading(PostState.post['title']),
                rx.text(f"By: {PostState.post['author']}"),
                rx.text(f"On: {PostState.post['created_at']}", class_name="date"),
                class_name="post_detail_header"
            ),
            rx.box(
                rx.text(PostState.post['body']),
                class_name="post_detail_body"
            ), 
            update_post_modal(),
            class_name="main"   
        ),

        
        class_name="page",
    )