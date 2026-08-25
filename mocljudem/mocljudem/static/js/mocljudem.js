document.addEventListener("DOMContentLoaded", function () {
  const expandButtons = document.querySelectorAll(".expand-button");
  expandButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const statusEl = button.closest(".status");
      const descriptionCol = statusEl.querySelector(".description-col");
      const isExpanded = descriptionCol.getAttribute("aria-hidden") === "false";
      descriptionCol.setAttribute("aria-hidden", isExpanded ? "true" : "false");
      if (isExpanded) {
        statusEl.classList.remove("expanded");
        button.setAttribute("aria-expanded", "false");
        button.setAttribute("aria-label", "Razširi");
      } else {
        statusEl.classList.add("expanded");
        button.setAttribute("aria-expanded", "true");
        button.setAttribute("aria-label", "Strni");
      }
    });
  });
});
