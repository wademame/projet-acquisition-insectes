# test_serveur_iphone.py
# Lance ce script, puis declenche le Raccourci depuis l'iPhone

from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        heure = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{heure}] Requete recue : {self.path}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK - signal recu')

    def log_message(self, format, *args):
        pass

print("Serveur demarre sur le port 8080...")
print("Declenche maintenant le Raccourci depuis l'iPhone.")
print("Ctrl+C pour arreter.")
serveur = HTTPServer(('0.0.0.0', 8080), Handler)
serveur.serve_forever()