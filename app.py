from flask import Flask, request, render_template_string

app = Flask(__name__)
scanned_items = ""

@app.route('/checkout', methods=['POST'])
def checkout():
    global scanned_items
    data = request.get_json()
    scanned_items = data.get("items", "")
    return {"status": "received"}, 200

@app.route('/')
def show_cart():
    return render_template_string("""
    <html>
    <head><title>Smart Trolley</title></head>
    <body>
        <h1>Scanned Items</h1>
        <pre>{{ items }}</pre>
        <form action="/pay" method="post">
            <button type="submit">Pay</button>
        </form>
    </body>
    </html>
    """, items=scanned_items)

@app.route('/pay', methods=['POST'])
def pay():
    global scanned_items
    scanned_items = ""
    return "<h2>Payment Successful!</h2><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run()
