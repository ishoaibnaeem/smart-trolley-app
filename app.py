from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# We will store the scanned items as a list of dictionaries.
# Each scanned item should include: name, price, image.
scanned_items = []

@app.route('/checkout', methods=['POST'])
def checkout():
    global scanned_items
    data = request.get_json()
    # Expecting JSON data in the following format:
    # { "items": [ { "name": "Milk", "price": 1.99, "image": "http://example.com/milk.jpg" }, ... ] }
    items = data.get("items", [])
    scanned_items = items
    return jsonify({"status": "received"}), 200

@app.route('/')
def show_cart():
    return render_template("index.html", items=scanned_items)

@app.route('/pay', methods=['POST'])
def pay():
    global scanned_items
    scanned_items = []  # reset the cart after payment
    return "<h2>Payment Successful!</h2><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run()

