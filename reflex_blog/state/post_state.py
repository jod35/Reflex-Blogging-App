import reflex as rx
from typing import List,Dict
from reflex_blog.post_data import posts


class PostState(rx.State):
    posts: List[Dict[str,str]] = []
    post: Dict[str,str] = {}
    title: str = ""
    body: str = ""


    async def load_posts(self) -> List[Dict[str,str]]:
        
        self.posts = posts


    async def create_post(self,form_data:dict):
        print(f"form data: {form_data}")

        self.posts.append(form_data)


    async def select_post(self, post_:dict):
        self.post = post_
        self.body = post_['body']
        self.title = post_['title']
        print(f"current post body: {self.post['body']}")


