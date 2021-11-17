from typing import List, Optional

from fastapi import Request


class ArticleCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.body: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.body = form.get("contenu")

    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("titre non valide")
        if not self.body or not len(self.body) >= 20:
            self.errors.append("Contenu trop court")
        if not self.errors:
            return True
        return False