from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/news")
def get_latest_news():
    try:
        with open("scraped_data_tech_crunch.json", "r", encoding="utf-8") as json_file:
            tech_crunch_contents = json.load(json_file)
            data = tech_crunch_contents[:5]
        with open("scraped_data_ycombinator.json", "r", encoding="utf-8") as json_file:
            ycombinator_contents = json.load(json_file)
            for content in ycombinator_contents[:5]:
                data.append(content)

        # Convert to JSON string with real UTF-8 characters
        json_str = json.dumps({"results": data}, ensure_ascii=False)

        # Return with proper content type
        return Response(json_str, content_type="application/json; charset=utf-8")

    except Exception as e:
        error_str = json.dumps({"error": str(e)}, ensure_ascii=False)
        return Response(error_str, content_type="application/json; charset=utf-8", status=500)

if __name__ == "__main__":
    app.run(debug=True)
