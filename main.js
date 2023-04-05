document.getElementById("submitButton").addEventListener("click", async () => {
    const textInput = document.getElementById("textInput").value;
    displayContent("textPrompt", textInput);
  
    const response = await sendPromptToServer(textInput);
    displayContent("apiResponse", response.generated_text);
  });
  
  function displayContent(elementId, content) {
    document.getElementById(elementId).textContent = content;
  }
  
  async function sendPromptToServer(prompt) {
    const response = await fetch("http://127.0.0.1:5000/send_prompt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    return await response.json();
  }
  