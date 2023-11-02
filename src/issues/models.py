from django.db import models
from shared.django import TimestampMixin
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()


class Issue(TimestampMixin):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    junior = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="junior_issues",
    )
    senior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="senior_issues",
        null=True,
    )

    class Meta:
        db_table = "issues"


# issue: Issue = Issue.objects.first()
# issue.junior: ==> users.User

# john: User = User.objects.get(email='john@email.com')
# john.issues.first().messages.all()


class Message(TimestampMixin):
    content = models.CharField(max_length=100)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="messages"
    )
    issue = models.ForeignKey(
        "issues.Issue", on_delete=models.DO_NOTHING, related_name="messages"
    )

    class Meta:
        db_table = "issues_messages"
