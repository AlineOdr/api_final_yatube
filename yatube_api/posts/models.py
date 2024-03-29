from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name=('Имя'), max_length=200)
    slug = models.SlugField(verbose_name=('Адрес'), unique=True)
    description = models.TextField(verbose_name=('Описание'))

    class Meta:
        verbose_name = ('Группа')
        verbose_name_plural = ('Группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name=('Сообщество'),
        help_text='Группа, к которой будет относиться пост'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    class Meta:
        verbose_name = ('Пост')
        verbose_name_plural = ('Посты')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = ('Комментарий')
        verbose_name_plural = ('Комментарии')

    def __str__(self) -> str:
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        verbose_name = ('Подписчик')
        verbose_name_plural = ('Подписчики')
        constraints = [models.CheckConstraint(
            check=~models.Q(following=models.F('user')),
            name='cannot subscribe to yourself'),
            models.UniqueConstraint(name='unique_subscribe',
                                    fields=['user', 'following'],)]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
