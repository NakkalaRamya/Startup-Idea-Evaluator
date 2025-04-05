from flask import Flask, render_template, request

app = Flask(__name__)

# Rule-based scoring function
def evaluate_idea(idea):
    idea = idea.lower()
    keywords_innovation = ['ai', 'machine learning', 'blockchain', 'automation']
    keywords_scalability = ['global', 'scale', 'cloud', 'saas', 'platform']
    keywords_market = ['demand', 'problem', 'solution', 'market', 'customers']

    innovation_score = sum(1 for word in keywords_innovation if word in idea)
    scalability_score = sum(1 for word in keywords_scalability if word in idea)
    market_score = sum(1 for word in keywords_market if word in idea)

    # Scale to 10
    innovation_score *= 2
    scalability_score *= 2
    market_score *= 2

    summary = "Your idea seems "
    if innovation_score >= 6:
        summary += "innovative, "
    else:
        summary += "somewhat common, "

    if scalability_score >= 6:
        summary += "scalable, "
    else:
        summary += "limited in scalability, "

    if market_score >= 6:
        summary += "and relevant to current market needs."
    else:
        summary += "but needs better market alignment."

    return innovation_score, scalability_score, market_score, summary


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/evaluate', methods=['POST'])
def evaluate():
    idea = request.form['idea']
    innovation, scalability, market, summary = evaluate_idea(idea)

    return render_template(
        'result.html',
        idea=idea,
        innovation=innovation,
        scalability=scalability,
        market=market,
        summary=summary
    )


if __name__ == '__main__':
    app.run(debug=True)
