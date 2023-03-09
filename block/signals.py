from django.db.models.signals import post_delete
from django.dispatch import receiver
from block.models import blog
import os
@receiver(post_delete, sender=blog)
def log_deleted_question(sender, instance, using, **kwargs):
    
       if instance.images:
            if os.path.isfile(instance.images.path):
                 os.remove(instance.images.path)
    
