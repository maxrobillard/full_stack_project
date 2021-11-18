from typing import List, Optional
from fastapi import Request


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None
        self.verifpassword: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.email = form.get("email")
        self.password = form.get("password")
        self.verifpassword = form.get("re_password")

    async def is_valid(self):
            if not self.username:
                self.errors.append("nom et prenom requis")
            if not self.email:
                self.errors.append("adresse mail requise")
            if not self.email.__contains__("@"):
                self.errors.append("format de l'adresse mail invalide")
            if not self.password or not len(self.password) >= 5:
                self.errors.append("le mot de passe doit faire plus de 5 caractères")
            if not self.password == self.verifpassword:
                self.errors.append("les mots de passe ne sont pas identiques")
            if not self.errors:
                return True
            return False
