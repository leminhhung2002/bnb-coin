from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .import models

# Create your views here.


@csrf_exempt
def index(req):
    routes = [
        {
            "url": "/api/",
            "method": "*",
            "description": "This is the index page."
        }
    ]

    return JsonResponse({
        "message": "Welcome to the BNB Kingdom API.",
        "routes": routes
    })


@csrf_exempt
def get_user_data(req, wallet_address):
    if req.method != "GET":
        return JsonResponse({
            "message": "Method not allowed."
        }, status=405)

    try:
        user = models.Users.objects.get(wallet_address=wallet_address)
    except models.Users.DoesNotExist:
        return JsonResponse({
            "message": "User not found."
        }, status=404)

    return JsonResponse({
        "message": "User data found.",
        "user": {
            "id": user.user_id,
            "created_at": user.created_at,
            "date_created": user.date_created,
            "wallet_address": user.wallet_address
        }
    })


@crsf_exempt
def register_user(req):
    if req.method != "POST":
        return JsonResponse({
            "message": "Method not allowed."
        }, status=405)

    if "wallet_address" not in req.POST:
        return JsonResponse({
            "message": "Missing wallet_address."
        }, status=400)

    wallet_address = req.POST["wallet_address"]

    try:
        user = models.Users.objects.get(wallet_address=wallet_address)
        return JsonResponse({
            "message": "User already exists."
        }, status=400)
    except models.Users.DoesNotExist:
        user = models.Users(
            wallet_address=wallet_address
        )
        user.save()
        return JsonResponse({
            "message": "User registered."
        })
    return JsonResponse({
        "message": "Something went wrong."
    })


@csrf_exempt
def save_buy_history(req):
    if req.method != "POST":
        return JsonResponse({
            "message": "Method not allowed."
        }, status=405)

    if "wallet_address" not in req.POST:
        return JsonResponse({
            "message": "Missing wallet_address."
        }, status=400)

    if "amount_bnb" not in req.POST:
        return JsonResponse({
            "message": "Missing amount_bnb."
        }, status=400)

    wallet_address = req.POST["wallet_address"]
    amount_bnb = req.POST["amount_bnb"]

    try:
        user = models.Users.objects.get(wallet_address=wallet_address)
    except models.Users.DoesNotExist:
        return JsonResponse({
            "message": "User not found."
        }, status=404)

    buy_history = models.BuyHistory(
        user=user,
        amount_bnb=amount_bnb
    )
    buy_history.save()

    return JsonResponse({
        "message": "Buy history saved."
    })


@csrf_exempt
def get_buy_history(req, wallet_address):
    if req.method != "GET":
        return JsonResponse({
            "message": "Method not allowed."
        }, status=405)

    try:
        history = models.BuyHistory.objects.filter(
            user__wallet_address=wallet_address)
    except models.BuyHistory.DoesNotExist:
        return JsonResponse({
            "message": "Buy history not found."
        }, status=404)

    history_data = []
    for i in history:
        history_data.append({
            "id": i.buy_history_id,
            "user_id": i.user.user_id,
            "wallet_address": i.user.wallet_address,
            "created_at": i.created_at,
            "date_created": i.date_created,
            "date_started": i.get_date_started(),
            "date_finished": i.get_date_finished(),
            "amount_bnb": i.amount_bnb,
            "is_complete": i.is_complete_task(),
            "program_type": i.get_program_type(),
            "note": i.note
        })

    return JsonResponse({
        "message": "Buy history found.",
        "history": history_data
    })
