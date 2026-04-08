const API = "http://127.0.0.1:8000/notat";

// ── Navigasjon ──
function visSeksjon(navn) {
  document.getElementById("seksjon-skjema").classList.add("skjult");
  document.getElementById("seksjon-liste").classList.add("skjult");
  document.getElementById(`seksjon-${navn}`).classList.remove("skjult");
}

function toggleMeny() {
  document.getElementById("meny").classList.toggle("skjult");
}

// ── POST – lagre nytt notat ──
async function lagNotat() {
  const title = document.getElementById("title").value.trim();
  const text  = document.getElementById("text").value.trim();

  if (!title || !text) {
    alert("Fyll inn både tittel og tekst.");
    return;
  }

  try {
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, text }),
    });
    if (!res.ok) throw new Error(`Serverfeil: ${res.status}`);

    document.getElementById("title").value = "";
    document.getElementById("text").value  = "";
    visSeksjon("liste");
    await hentNotater();
  } catch (err) {
    console.error("Kunne ikke lagre notat:", err);
    alert("Noe gikk galt. Sjekk at serveren kjører.");
  }
}

// ── GET – hent og vis alle notater ──
async function hentNotater() {
  try {
    const res  = await fetch(API);
    if (!res.ok) throw new Error(`Serverfeil: ${res.status}`);
    const data = await res.json();

    const liste = document.getElementById("liste");
    liste.innerHTML = "";

    if (data.length === 0) {
      liste.innerHTML = '<li class="notat-element tom"><p class="notat-tekst">Ingen notater ennå.</p></li>';
      return;
    }

    data.forEach((note, i) => {
      const li = document.createElement("li");
      li.className = "notat-element";
      li.dataset.id = note.id;
      li.style.animationDelay = `${i * 0.06}s`;
      li.innerHTML = `
        <div class="notat-topp">
          <p class="notat-tittel">${escapeHtml(note.title)}</p>
          <button class="slett-knapp" title="Slett notat" onclick="slettNotat(${note.id})">🗑</button>
        </div>
        <p class="notat-tekst">${escapeHtml(note.text)}</p>
      `;
      liste.appendChild(li);
    });
  } catch (err) {
    console.error("Kunne ikke hente notater:", err);
    alert("Noe gikk galt. Sjekk at serveren kjører.");
  }
}

// ── DELETE – slett ett notat ──
async function slettNotat(id) {
  try {
    const res = await fetch(`${API}/${id}`, { method: "DELETE" });
    if (!res.ok) throw new Error(`Serverfeil: ${res.status}`);

    // Finn kortet og animer det bort
    const kort = document.querySelector(`.notat-element[data-id="${id}"]`);
    if (kort) {
      kort.classList.add("sletter");
      setTimeout(() => {
        kort.remove();
        // Vis tom-melding hvis listen er tom
        const liste = document.getElementById("liste");
        if (liste.children.length === 0) {
          liste.innerHTML = '<li class="notat-element tom"><p class="notat-tekst">Ingen notater ennå.</p></li>';
        }
      }, 300);
    }
  } catch (err) {
    console.error("Kunne ikke slette notat:", err);
    alert("Noe gikk galt. Sjekk at serveren kjører.");
  }
}

// ── HTML-escape mot XSS ──
function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}