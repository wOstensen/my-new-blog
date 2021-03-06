import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		""" this function should return False for question
		wherein the pub_date is in the future """
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		""" was_published_recently should return True for questions
		whose pub_date is within the last day """
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date=time)
		self.assertEqual(recent_question.was_published_recently(), True)
