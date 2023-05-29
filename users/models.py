from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Manager personalizado para el modelo User.

    Permite la creación de usuarios y superusuarios.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un nuevo usuario.

        Args:
            email (str): Email del usuario.
            password (str, optional): Contraseña del usuario. Si no se proporciona, se generará una contraseña aleatoria.
            **extra_fields: Campos adicionales del usuario.

        Returns:
            User: Instancia del usuario creado.
        """
        if not email:
            raise ValueError('El email es obligatorio')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea y guarda un nuevo superusuario.

        Args:
            email (str): Email del superusuario.
            password (str, optional): Contraseña del superusuario. Si no se proporciona, se generará una contraseña aleatoria.
            **extra_fields: Campos adicionales del superusuario.

        Returns:
            User: Instancia del superusuario creado.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Modelo de usuario personalizado.

    Hereda de AbstractBaseUser para proporcionar funcionalidad básica de autenticación de usuarios.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Obtiene el nombre completo del usuario.

        Returns:
            str: Nombre completo del usuario.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        Obtiene el nombre corto del usuario.

        Returns:
            str: Nombre corto del usuario.
        """
        return self.first_name

    def __str__(self):
        """
        Representación de cadena del usuario.

        Returns:
            str: Representación de cadena del usuario (email).
        """
        return self.email

