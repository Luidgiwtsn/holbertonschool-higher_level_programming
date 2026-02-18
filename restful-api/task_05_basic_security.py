"""
Module de sécurisation d'une API Flask avec Basic Auth et JWT.

Ce module implémente trois niveaux de sécurité :
- Authentification HTTP basique
- Authentification par token JWT
- Contrôle d'accès basé sur les rôles (RBAC)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

# Clé secrète utilisée pour signer les tokens JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Base de données en mémoire des utilisateurs
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ─────────────────────────────────────────────
# Gestionnaires d'erreurs JWT personnalisés
# ─────────────────────────────────────────────

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Retourne 401 si le token est absent ou mal formé."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Retourne 401 si le token est invalide."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    """Retourne 401 si le token a expiré."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    """Retourne 401 si le token a été révoqué."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    """Retourne 401 si un token frais est requis."""
    return jsonify({"error": "Fresh token required"}), 401


# ─────────────────────────────────────────────
# Basic Authentication
# ─────────────────────────────────────────────

@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les credentials pour l'authentification basique.

    Args:
        username (str): Nom d'utilisateur fourni.
        password (str): Mot de passe en clair fourni.

    Returns:
        str | None: Le nom d'utilisateur si valide, sinon None.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Route protégée par authentification basique.

    Returns:
        str: Message de confirmation d'accès.
    """
    return "Basic Auth: Access Granted"


# ─────────────────────────────────────────────
# JWT Authentication
# ─────────────────────────────────────────────

@app.route("/login", methods=["POST"])
def login():
    """
    Authentifie un utilisateur et retourne un token JWT.

    Le corps de la requête doit contenir :
        - username (str)
        - password (str)

    Returns:
        JSON: {"access_token": "<token>"} avec statut 200.
        JSON: {"error": "..."} avec statut 401 si credentials invalides.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 401

    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # On inclut le rôle dans l'identité du token
    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Route protégée par token JWT.

    Returns:
        str: Message de confirmation d'accès.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Route réservée aux utilisateurs avec le rôle 'admin'.

    Returns:
        str: Message d'accès admin si autorisé.
        JSON: {"error": "Admin access required"} avec statut 403 sinon.
    """
    current_user = get_jwt_identity()

    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
