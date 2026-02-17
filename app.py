from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000, "image": "https://picsum.photos/200?1"},
    {"id": 2, "name": "Mobile", "price": 20000, "image": "https://picsum.photos/200?2"},
    {"id": 3, "name": "Headphones", "price": 3000, "image": "https://picsum.photos/200?3"},
    {"id": 4, "name": "Watch", "price": 7000, "image": "https://picsum.photos/200?4"}
]

cart = []

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/add", methods=["POST"])
def add_to_cart():
    pid = int(request.json["id"])
    for p in products:
        if p["id"] == pid:
            cart.append(p)
            return jsonify({"msg": f"{p['name']} added to cart", "cart": cart})

@app.route("/buy", methods=["POST"])
def buy_now():
    pid = int(request.json["id"])
    for p in products:
        if p["id"] == pid:
            return jsonify({"msg": f"Order placed for {p['name']} ✅"})

@app.route("/cart")
def get_cart():
    return jsonify(cart)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
