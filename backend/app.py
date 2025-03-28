import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from duckduckgo_search import DDGS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Create a summarization pipeline using BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def clean_text(text: str) -> str:
    """Remove excessive whitespace."""
    return re.sub(r'\s+', ' ', text).strip()

@app.route('/summarize', methods=['POST'])
def summarize():
    """
    1. Receives a query from the user.
    2. Uses DDGS to search the web for relevant snippets.
    3. Combines and cleans the snippets.
    4. Summarizes the text using a BART summarization model.
    5. Returns the summary and the snippets used.
    """
    data = request.get_json(force=True)
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Perform DuckDuckGo search using DDGS
    with DDGS() as ddgs:
        results = ddgs.text(
            query,
            region="us-en",
            safesearch="moderate",
            timelimit=None,
            max_results=5
        )
        results_list = list(results)

    # Combine snippet bodies from the search results
    combined_snippets = " ".join(r.get("body", "") for r in results_list)
    combined_snippets = clean_text(combined_snippets)

    # Truncate text if needed (BART usually handles ~1024 tokens; adjust character count as needed)
    truncated_text = combined_snippets[:4000] if len(combined_snippets) > 4000 else combined_snippets

    # Summarize the text
    summary_output = summarizer(truncated_text, max_length=100, min_length=30, do_sample=False)
    summary_text = summary_output[0]["summary_text"]

    return jsonify({
        "query": query,
        "summary": summary_text,
        "snippets_used": truncated_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)