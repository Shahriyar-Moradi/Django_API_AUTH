
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser  # Import your CustomUser model

@pytest.mark.django_db
def test_create_user_api():
    # Create an API client
    client = APIClient()

    # Define the API endpoint URL (replace 'user-list' with your actual endpoint)
    url = reverse('user-login')

    # Define data for creating a user
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }

    # Send a POST request to the API
    response = client.post(url, data, format='json')

    # Assertions
    assert response.status_code == status.HTTP_201_CREATED
    assert CustomUser.objects.filter(username='testuser').exists()

    # Additional assertions (customize based on your user creation logic)
    user = CustomUser.objects.get(username='testuser')
    assert user.email == 'test@example.com'
    assert user.check_password('password123')  # Ensure the password is set correctly

    # Optionally, you can check other fields and permissions as needed
    # assert user.is_active
    # assert not user.is_staff
    # assert not user.is_superuser
