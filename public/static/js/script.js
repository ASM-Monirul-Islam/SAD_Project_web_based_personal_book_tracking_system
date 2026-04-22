// Header Script

const bar = document.querySelector(".profile");
const navbar = document.querySelector(".navbar");
const close = document.querySelector("#close");

if (bar) {
  bar.addEventListener("click", () => {
    navbar.classList.add("active");
  });
}

if (close) {
  close.addEventListener("click", () => {
    navbar.classList.remove("active");
  });
}

document.addEventListener("click", (e) => {
  if (
    navbar.classList.contains("active") &&
    !bar.contains(e.target) &&
    !close.contains(e.target)
  ) {
    navbar.classList.remove("active");
  }
});

// confirm.html

const modal = document.getElementById("confirmModal");
const confirmBtn = document.getElementById("confirmBtn");
const cancelBtn = document.getElementById("cancelBtn");

let currentAction = {};

document.addEventListener("click", function (e) {
  const trigger = e.target.closest(".confirm-action");
  if (!trigger) return;

  e.preventDefault();

  currentAction = {
    url: trigger.dataset.url,
    method: trigger.dataset.method || "GET",
    title: trigger.dataset.title || "Are you sure?",
    message: trigger.dataset.message || "This action cannot be undone.",
  };

  document.getElementById("confirmTitle").innerText = currentAction.title;
  document.getElementById("confirmMessage").innerText = currentAction.message;

  modal.classList.remove("hidden");
});

cancelBtn.onclick = () => {
  modal.classList.add("hidden");
};

confirmBtn.onclick = () => {
  if (currentAction.method === "POST") {
    const form = document.getElementById("globalForm");
    form.action = currentAction.url;
    form.submit();
  } else {
    window.location.href = currentAction.url;
  }
};

// search bar


function runSearch() {
    const query = document.getElementById("searchInput").value;
    const urlParams = new URLSearchParams(window.location.search);

    urlParams.set("q", query);

    window.location.search = urlParams.toString();
}