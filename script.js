const today = new Date().toISOString().split("T")[0];

let selectedMood = "😊";

const prompts = [
  "what made you smile today?",
  "what challenged you today?",
  "what did you learn today?",
  "who did you appreciate today?",
  "what moment stood out today?"
];

document.getElementById("todayDate").innerText = today;
document.getElementById("promptText").innerText =
  prompts[Math.floor(Math.random() * prompts.length)];

function setMood(mood) {
  selectedMood = mood;
}

/* storage */

function getData() {
  return JSON.parse(localStorage.getItem("memories") || "{}");
}

function saveData(data) {
  localStorage.setItem("memories", JSON.stringify(data));
}

/* saves the memory */

function saveMemory() {
  const text = document.getElementById("memoryInput").value;
  if (!text.trim()) return;

  const data = getData();

  data[today] = {
    text,
    mood: selectedMood
  };

  saveData(data);

  document.getElementById("status").innerText = "saved ✔";

  renderAll();
}

/* keeps track of the streak */

function calculateStreak(data) {
  let streak = 0;

  let d = new Date();

  while (true) {
    const key = d.toISOString().split("T")[0];

    if (data[key]) {
      streak++;
      d.setDate(d.getDate() - 1);
    } else {
      break;
    }
  }

  return streak;
}

/* calendar creation */

function renderCalendar(data) {
  const calendar = document.getElementById("calendar");
  calendar.innerHTML = "";

  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();

  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);

  for (let i = 1; i <= lastDay.getDate(); i++) {
    const date = new Date(year, month, i).toISOString().split("T")[0];

    const div = document.createElement("div");
    div.className = "day";

    if (data[date]) {
      div.classList.add("has-memory");
      div.innerHTML = `
        <div>${i}</div>
        <div>${data[date].mood}</div>
      `;
    } else {
      div.innerHTML = `<div>${i}</div>`;
    }

    calendar.appendChild(div);
  }
}

/* making a list */

function renderList(data) {
  const list = document.getElementById("memoryList");
  list.innerHTML = "";

  Object.keys(data)
    .sort()
    .reverse()
    .forEach(date => {
      const entry = data[date];

      const div = document.createElement("div");
      div.className = "memory-item";

      div.innerHTML = `
        <strong>${date}</strong> ${entry.mood}<br/>
        ${entry.text}
      `;

      list.appendChild(div);
    });
}

/* the rendering part of it */

function renderAll() {
  const data = getData();

  renderList(data);
  renderCalendar(data);

  document.getElementById("streakCount").innerText =
    calculateStreak(data);

  if (data[today]) {
    document.getElementById("memoryInput").value = data[today].text;
    selectedMood = data[today].mood;
  }
}

renderAll();