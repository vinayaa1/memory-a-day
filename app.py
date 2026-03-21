from flask import Flask, request, render_template_string
from datetime import date
from memory_store import save_memory, memory_exists, load_memories, get_random_memory
from ai_helper import analyze_memory

app = Flask('Memory a Day')

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Memory A Day</title>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Quicksand', sans-serif;
            background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            text-align: center;
            width: 350px;
        }

        h1 {
            margin-bottom: 15px;
        }

        textarea {
            width: 100%;
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
            font-family: inherit;
        }

        button {
            background: #ff8fab;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            color: white;
            font-size: 14px;
            cursor: pointer;
            transition: 0.2s;
        }

        button:hover {
            background: #ff6f91;
        }

        a {
            display: block;
            margin: 5px;
            color: #6c63ff;
            text-decoration: none;
            font-weight: 600;
        }

        a:hover {
            text-decoration: underline;
        }

        .result {
            margin-top: 15px;
            background: #f7f7ff;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Memory A Day</h1>

        <a href="/all">view all memories</a>
        <a href="/random">random memory</a>

        <form method="POST">
            <textarea name="memory" rows="4" placeholder="write your memory here..."></textarea><br><br>
            <button type="submit">save memory</button>
        </form>

        {% if result %}
            <div class="result">
                <h3>your reflection:</h3>
                <pre>{{ result }}</pre>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

#this is how to get to the home page!
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    today = date.today().isoformat()

    if request.method == "POST":
        user_memory = request.form["memory"]

        if not memory_exists(today):
            analysis = analyze_memory(user_memory)
            save_memory(today, user_memory)
            result = analysis
        else:
            result = "you already wrote a memory today."

    return render_template_string(HOME_HTML, result=result)


#this is how to view all the memories you have written before
@app.route("/all")
def view_all():
    memories = load_memories()

    html = "<h1>all memories</h1><br>"

    if not memories:
        html += "<p>no memories yet.</p>"
    else:
        for date, entry in memories.items():
            html += f"<p><b>{date}</b>: {entry['memory']}</p>"

    html += '<br><a href="/">⬅ back</a>'

    return html


#this is for the random memory
@app.route("/random")
def random_page():
    result = get_random_memory()

    html = "<h1>random memory</h1><br>"

    if result is None:
        html += "<p>no memories yet.</p>"
    else:
        date, memory = result
        html += f"<p><b>{date}</b>: {memory}</p>"

    html += '<br><a href="/">⬅ back</a>'

    return html


#run the apppp
if __name__ == "__main__":
    app.run(debug=True)