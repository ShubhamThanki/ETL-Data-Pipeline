from flask import Flask, render_template
from main import main as run_full_etl  # Reuse your main.py logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_etl', methods=['POST'])
def run_etl():
    try:
        run_full_etl()
        status_msg = "✅ ETL process completed successfully."
    except Exception as e:
        status_msg = f"❌ ETL failed: {str(e)}"

    return render_template('index.html', status=status_msg)

if __name__ == '__main__':
    app.run(debug=True)
