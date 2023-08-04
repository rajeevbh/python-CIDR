from flask import Flask, render_template, request
import ipaddress

app = Flask(__name__)

def cidr_to_range(cidr):
    network = ipaddress.ip_network(cidr)
    return network.network_address, network.broadcast_address, network.num_addresses

@app.route("/", methods=["GET", "POST"])
def index():
    network_address = None
    broadcast_address = None
    total_count = None

    if request.method == "POST":
        cidr_input = request.form.get("cidr_input")
        try:
            network_address, broadcast_address, total_count = cidr_to_range(cidr_input)
        except ValueError:
            pass

    return render_template("index.html", network_address=network_address, broadcast_address=broadcast_address, total_count=total_count)

if __name__ == "__main__":
    app.run(debug=True)
