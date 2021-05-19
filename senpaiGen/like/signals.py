from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from like.models import Like
from post.models import Post


@receiver(post_save, sender=Like)  # Top count the total_likes
def post_save_like_count(sender, instance, created, *args, **kwargs):

    if created:
        # obj = Post.objects.filter(title=instance.post.title).values('total_no_of_likes')
        liked_post = Post.objects.get(pk=instance.post.id)  # get the liked post
        # print(obj)
        try:
            liked_post.total_no_of_likes += 1  # Update the no of likes
            liked_post.save()  # Save the count
        except AttributeError:
            pass

        # print(instance.post.total_no_of_likes, obj.total_no_of_likes)


