from flask import Flask, render_template

app = Flask(__name__)

VIZ = {
    "dashboard1": "https://public.tableau.com/views/OlympicPerformanceAnalysis_17931144556200/Dashboard1",
    "dashboard2": "https://public.tableau.com/views/OlympicPerformanceAnalysis_17931144556200/Dashboard2",
    "story": "https://public.tableau.com/views/OlympicPerformanceAnalysis_17931144556200/Story1",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard1")
def dashboard1():
    return render_template("dashboard.html", title="Medal and Sport Performance", viz_url=VIZ["dashboard1"])

@app.route("/dashboard2")
def dashboard2():
    return render_template("dashboard.html", title="Performance and Regional Efficiency", viz_url=VIZ["dashboard2"])

@app.route("/story")
def story():
    return render_template("dashboard.html", title="Olympic Performance Story", viz_url=VIZ["story"])

if __name__ == "__main__":
    app.run(debug=True)