"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from reflex_blog.pages.home import index
from reflex_blog.pages.create_post import create_post_page
from reflex_blog.pages.post_detail import post_detail_page
from reflex_blog.state.post_state import PostState


import reflex as rx


app = rx.App(
    stylesheets = [
        "/styles/main.css"
    ]
)
app.add_page(index,on_load=[
    PostState.load_posts
])

app.add_page(create_post_page, route="/create_post")

app.add_page(post_detail_page, route="/post/[uid]")