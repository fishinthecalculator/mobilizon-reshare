from tortoise.models import Model
from tortoise import fields


class Event(Model):
    id = fields.UUID(pk=True)
    name = fields.TextField()

    # tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
    # participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')
    # modified = fields.DatetimeField(auto_now=True)
    # prize = fields.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "event"


class SocialNetwork(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name

    class Meta:
        table = "social_network"
