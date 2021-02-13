import praw
from django.conf import settings
from django.core.management.base import BaseCommand

from map.models import Submission


class Command(BaseCommand):
    help = 'Scrapes hot posts from a subreddit'

    def add_arguments(self, parser):
        parser.add_argument('subreddit')

    def handle(self, *args, **options):
        reddit = praw.Reddit(**settings.PRAW)
        subreddit = reddit.subreddit(options['subreddit'])

        for submission in subreddit.hot(limit=10):
            Submission.objects.get_or_create(
                reddit_id=submission.id,
                defaults=dict(
                    url=submission.url,
                    title=submission.title,
                    author=submission.author.name,
                    data={k: str(v) for k, v in submission.__dict__.items()}
                )
            )
