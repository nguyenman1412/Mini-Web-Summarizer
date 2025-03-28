# Mini Web Summarizer

This project is a simple **Retrieval-Augmented Summarization** system. It uses a Flask backend to perform web searches via DuckDuckGo (using the `DDGS` class) and summarizes the combined snippets using a pre-trained BART summarization model from Hugging Face. A basic frontend is provided to interact with the system.

## Features

- **Web Search Integration:** Uses DuckDuckGo to fetch text snippets related to a user's query.
- **Text Summarization:** Leverages a transformer-based model (facebook/bart-large-cnn) to generate concise summaries.
- **Simple Frontend:** An HTML/CSS/JS interface built with Bootstrap for easy interaction.
- **Containerization:** A Dockerfile is provided for containerizing the backend.
- **CORS Support:** The Flask backend is set up with CORS, allowing the frontend to communicate seamlessly.

## Project Structure
mini_web_summarizer/
├── backend/
│   ├── app.py             # Flask backend code
│   ├── requirements.txt   # Python dependencies for backend
│   └── Dockerfile         # Docker configuration for backend
└── frontend/
├── index.html         # Simple HTML page for the UI
├── css/
│   └── styles.css     # Custom styles (optional)
└── js/
└── app.js         # JavaScript to call the backend API
## Requirements

- **Python 3.9+**
- **Flask**
- **Flask-CORS**
- **duckduckgo_search**
- **transformers**
- **torch**
- **regex**

Install dependencies by running:

```bash
cd mini_web_summarizer/backend
pip install -r requirements.txt
Running the Application

Backend

Locally
	1.	Navigate to the backend directory:
        cd mini_web_summarizer/backend
    2.	Run the Flask app:
        python app.py
The backend will start on http://localhost:5100.
Using Docker
    1.	Build the Docker image:
        docker build -t mini-web-summarizer .
    2.	Run the container:
        docker run -p 5100:5100 mini-web-summarizer
Frontend
    You can open the frontend/index.html file directly in your browser, or serve it using a simple HTTP server:
        cd mini_web_summarizer/frontend
        python -m http.server 8000
    Then navigate to http://localhost:8000 in your browser.
Usage
	1.	Enter a Query: On the frontend, type your query (e.g., “What is machine learning?”) into the provided form.
	2.	Get a Summary: The backend will perform a web search, summarize the retrieved text, and display the summary along with the snippets used.
	3.	View Results: The summarized answer and the snippets will be displayed on the page.
Future Work
	•	Domain-Specific Enhancements: Incorporate domain-specific data or fine-tune the summarization model for niche topics.
	•	Improved Snippet Selection: Enhance the retrieval process with full-page scraping and advanced snippet ranking.
	•	Image Recognition Integration: As mentioned previously, the next project will focus on image recognition.
License
    This project is open source and available under the MIT License.
