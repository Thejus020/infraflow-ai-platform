from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Analyze page
@app.route('/analyze', methods=['POST'])
def analyze():

    # ---- Get form data ----
    project = request.form['project']
    app_type = request.form['app_type']
    traffic = request.form['traffic']
    database = request.form['database']

    # ---- AI Analysis Engine ----
    recommendation = []
    risk_score = 0

    # Traffic analysis
    if traffic == "High":
        recommendation.append({
            "title": "Use Load Balancer and Auto Scaling",
            "reason": "High traffic applications require scaling to prevent server overload."
        })
        risk_score += 40

    elif traffic == "Medium":
        recommendation.append({
            "title": "Consider scalable infrastructure",
            "reason": "Medium traffic may increase, scalable systems prevent downtime."
        })
        risk_score += 20

    # Database analysis
    if database == "Yes":
        recommendation.append({
            "title": "Use AWS RDS for managed database",
            "reason": "Managed databases improve reliability and automated backups."
        })
        risk_score += 20

    # Application type analysis
    if app_type == "Static Site":
        recommendation.append({
            "title": "Deploy using AWS S3 + CloudFront",
            "reason": "Static sites perform better using CDN-based hosting."
        })

    elif app_type == "API":
        recommendation.append({
            "title": "Consider Docker containers",
            "reason": "Containerization improves portability and CI/CD automation."
        })
        risk_score += 10

    # Risk level calculation
    if risk_score >= 50:
        risk = "High"
    elif risk_score >= 25:
        risk = "Medium"
    else:
        risk = "Low"

    confidence = 100 - risk_score

    return render_template(
        'result.html',
        project=project,
        recommendation=recommendation,
        risk=risk,
        confidence=confidence
    )


# Run server
if __name__ == '__main__':
    app.run(debug=True)
