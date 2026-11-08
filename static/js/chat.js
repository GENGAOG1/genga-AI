const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const messages = document.querySelector("#messages");
let chatId = messages?.dataset.chatId || null;

function addBubble(role, text) {
  const node = document.createElement("div");
  node.className = `message ${role}`;
  node.textContent = text;
  messages.appendChild(node);
  node.scrollIntoView({behavior: "smooth", block: "end"});
}

document.querySelector("#new-chat")?.addEventListener("click", async () => {
  const r = await fetch("/chat/new", {method: "POST"});
  const data = await r.json();
  if (data.chat_id) location.href = `/chat/?id=${data.chat_id}`;
  else alert(data.error || "Neuer Chat fehlgeschlagen.");
});

form?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;
  addBubble("user", message);
  input.value = "";
  try {
    const r = await fetch("/chat/message", {
      method: "POST", headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message, chat_id: chatId})
    });
    const data = await r.json();
    if (data.chat_id) chatId = data.chat_id;
    addBubble("assistant", data.answer || data.error || "Keine Antwort.");
  } catch {
    addBubble("assistant", "Verbindung fehlgeschlagen.");
  }
});

document.querySelector("#file-input")?.addEventListener("change", async (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  const status = document.querySelector("#upload-status");
  status.textContent = `Lade ${file.name} hoch…`;
  const formData = new FormData(); formData.append("file", file);
  try {
    const r = await fetch("/files/upload", {method: "POST", body: formData});
    const data = await r.json();
    status.textContent = data.error || `Datei: ${data.filename}`;
    if (data.text_preview) addBubble("assistant", `Dateiinhalt (Vorschau):\n${data.text_preview}`);
  } catch { status.textContent = "Upload fehlgeschlagen."; }
});
