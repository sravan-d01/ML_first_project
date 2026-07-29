from flask import Flask, render_template
from load_data import load_data, get_data_summary

app = Flask(__name__)


@app.route("/")
def index():
    # Landing page, no section selected yet
    return render_template("index.html", active="none")


@app.route("/data-loading")
def data_loading():
    """Loads the dataset (server-side) and renders the summary into the page."""
    error = None
    summary = None

    try:
        # Load the CSV file
        df = load_data()

        # Generate the summary
        summary = get_data_summary(df)

    except FileNotFoundError as e:
        error = str(e)
    except Exception as e:
        error = f"Unexpected error: {e}"

    return render_template(
        "index.html",
        active="data-loading",
        summary=summary,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
