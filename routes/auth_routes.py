from flask import Blueprint, request, redirect, url_for
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login')
def login():
    return auth_service.get_google_auth_url()

@auth_bp.route('/login/callback')
def callback():
    return auth_service.handle_google_callback()