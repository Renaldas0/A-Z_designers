from django.http import HttpResponse


class StripeWebHook_Handler:
    # Handles Stripe wenhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # Handles any unknown or unexpected webhook events

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
