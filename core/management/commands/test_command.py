from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "testing command line functions"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--send", type=bool, help="True for send, False for skip")
        parser.add_argument("--message", type=str, help="message to relay")
    
    def handle(self, *args, **options):
        send = options["send"]
        message = options["message"]
        if send:
            print("Sending message: ", message)
        return "done"