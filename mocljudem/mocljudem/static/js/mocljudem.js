document.addEventListener("DOMContentLoaded", function () {
  const expandButtons = document.querySelectorAll(".expand-button");
  expandButtons.forEach((button) => {
    const statusEl = button.closest(".status");

    button.addEventListener("click", function () {
      const descriptionCol = statusEl.querySelector(".description-col");
      const isExpanded = descriptionCol.getAttribute("aria-hidden") === "false";
      descriptionCol.setAttribute("aria-hidden", isExpanded ? "true" : "false");
      if (isExpanded) {
        statusEl.classList.remove("expanded");
        statusEl.style.cursor = "pointer";
        button.setAttribute("aria-expanded", "false");
        button.setAttribute("aria-label", "Razširi");
      } else {
        statusEl.classList.add("expanded");
        statusEl.style.cursor = "";
        button.setAttribute("aria-expanded", "true");
        button.setAttribute("aria-label", "Strni");
      }
    });

    statusEl.addEventListener("click", function (event) {
      const closestButton = event.target.closest(".expand-button");
      if (closestButton === button) {
        return;
      }
      const isExpanded = statusEl.classList.contains("expanded");
      if (isExpanded) {
        return;
      }
      button.click();
    });
    statusEl.style.cursor = "pointer";
  });

  const newsletterForm = document.querySelector(".newsletter-form");
  if (newsletterForm) {
    newsletterForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const campaign_slug = "danes-je-nov-dan";
      const segment_id = 21;
      const email = this.querySelector("#newsletter-email").value;

      let url = `https://moj.djnd.si/${campaign_slug}/prijava?segment_id=${segment_id}`;
      url += `&email=${encodeURIComponent(email)}`;
      window.open(`${url}`, `_blank`);
    });
  }
});
