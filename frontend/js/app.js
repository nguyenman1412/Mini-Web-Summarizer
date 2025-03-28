document.getElementById('searchForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const query = document.getElementById('queryInput').value.trim();
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = "Searching and summarizing...";

  try {
    const response = await fetch('http://localhost:5100/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const data = await response.json();

    if (data.error) {
      resultDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
      return;
    }

    resultDiv.innerHTML = `
      <h4>Summary:</h4>
      <p>${data.summary}</p>
      <hr>
      <h5>Snippets Used:</h5>
      <p>${data.snippets_used}</p>
    `;
  } catch (error) {
    console.error(error);
    resultDiv.innerHTML = '<div class="alert alert-danger">An error occurred while processing your request.</div>';
  }
});