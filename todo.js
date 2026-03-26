const API = "http://127.0.0.1:8000/notat";

// POST samme som post_note
async function lagNotat() {
  const title = document.getElementById("title").value;
  const text = document.getElementById("text").value;

  const res = await fetch(API, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title, text })
  });

  console.log(res.status);
}

// GET samme som get_notes
async function hentNotater() {
  const res = await fetch(API);
  const data = await res.json();

  const liste = document.getElementById("liste");
  liste.innerHTML = "";

  data.forEach(note => {
    const li = document.createElement("li");
    li.textContent = note.title + " - " + note.text;
    liste.appendChild(li);
  });
}