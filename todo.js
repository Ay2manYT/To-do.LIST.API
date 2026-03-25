function visOpprettNotat() {
  alert("Her kan du lage notater. (Fiks senere med API)");
}

function visOpprettListe() {
  alert("Her kan du lage todo-lister. (Fiks senere med API)");
}

// Legg til ny oppgave i todo-liste 
function leggTilOppgave() {
  const oppgave = document.getElementById("ny-oppgave").value;
  if (!oppgave) return;

  const container = document.getElementById("tasks-container");
  const label = document.createElement("label");
  label.innerHTML = `<input type="checkbox"> ${oppgave}`;
  container.appendChild(label);

  document.getElementById("ny-oppgave").value = "";
}