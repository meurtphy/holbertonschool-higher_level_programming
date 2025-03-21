from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

# Lire JSON
def read_json():
    with open('products.json') as f:
        return json.load(f)

# Lire CSV
def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["price"] = float(row["price"])
            products.append(row)
    return products

# Lire depuis SQLite
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"name": r[0], "category": r[1], "price": r[2]} for r in rows]
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def products():
    source = request.args.get("source")
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sql()
    else:
        return render_template("product_display.html", error="❌ Source invalide.")

    # Si une erreur SQL survient
    if isinstance(data, dict) and "error" in data:
        return render_template("product_display.html", error=data["error"])

    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
