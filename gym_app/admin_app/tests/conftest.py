import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from ..models import Exercise, WorkoutPlan
from django.utils import timezone, dateformat
