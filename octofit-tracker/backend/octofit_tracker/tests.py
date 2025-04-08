from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTest(APITestCase):
    def test_create_user(self):
        data = {"username": "testuser", "email": "test@example.com", "password": "password123"}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTest(APITestCase):
    def test_create_team(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        data = {"name": "Team A", "members": [str(user._id)]}
        response = self.client.post("/api/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTest(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        data = {"user": str(user._id), "activity_type": "Running", "duration": "00:30:00"}
        response = self.client.post("/api/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTest(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        data = {"user": str(user._id), "score": 100}
        response = self.client.post("/api/leaderboard/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTest(APITestCase):
    def test_create_workout(self):
        data = {"name": "Workout A", "description": "A sample workout."}
        response = self.client.post("/api/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)