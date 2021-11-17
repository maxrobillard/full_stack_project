from typing import List, Optional

from fastapi import Request


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username:
            self.errors.append("Adresse mail nécessaire")
        if not self.username.__contains__("@"):
            self.errors.append("Adresse mail non valide")
        if not self.password or not len(self.password) >= 5:
            self.errors.append("Mot de passe non valide")
        if not self.errors:
            return True
        return False
