from flask import Flask, url_for

app = Flask(__name__)


@app.route('/show-routes')
def show_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = f"[{arg}]"

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote(f"{rule.endpoint}: {url} ({methods})")
        output.append(line)

    return "<br>".join(sorted(output))
