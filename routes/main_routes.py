from flask import Blueprint, jsonify
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def home():
    return jsonify({'message': 'Welcome', 'user': current_user.email})