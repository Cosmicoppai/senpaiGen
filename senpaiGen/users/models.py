from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class userManager(BaseUserManager):
    def create_user(self, nickname, email, password=None, staff=False, active=True, admin=False):
        if nickname and email and password:
            user_obj = self.model(email=self.normalize_email(email),
                                  nickname=nickname, )

            user_obj.set_password(password)
            user_obj.staff = staff
            user_obj.admin = admin
            user_obj.active = active
            user_obj.save(using=self.db)

            return user_obj
        raise ValueError("Enter all the Required Fields")

    def create_staffuser(self, nickname, email, password):
        user = self.create_user(nickname, email, password)
        user.staff = True
        user.save(using=self.db)
        return user

    def create_superuser(self, nickname, email, password):
        user = self.create_user(nickname, email, password)

        user.staff = True
        user.admin = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    nickname = models.CharField(max_length=20, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True, verbose_name='email address')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = userManager()

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.nickname

    def get_email(self):
        return self.email

    def get_nickname(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=120, blank=False, null=False, default='kanak-uni')
    id_proof = models.ImageField(blank=False, null=False, upload_to='id_proof')
    about = models.CharField(max_length=250, blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='profile_pic')
    id_proof_submitted = models.BooleanField(default=True)
    email_confirmed = models.BooleanField(default=False)
    id_proof_approved = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.id_proof)

    def get_id_status(self):
        return self.id_proof_submitted
