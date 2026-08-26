document.addEventListener("DOMContentLoaded", function () {
  const expandButtons = document.querySelectorAll(".expand-button");
  expandButtons.forEach((button) => {
    const statusEl = button.closest(".status");
    const descriptionCol = statusEl.querySelector(".description-col");

    function expandDescription() {
      statusEl.classList.add("expanded");
      statusEl.style.cursor = "";
      button.setAttribute("aria-expanded", "true");
      button.setAttribute("aria-label", "Strni");
      descriptionCol.setAttribute("aria-hidden", "false");
      descriptionCol.removeAttribute("hidden");
    }

    function collapseDescription() {
      statusEl.classList.remove("expanded");
      statusEl.style.cursor = "pointer";
      button.setAttribute("aria-expanded", "false");
      button.setAttribute("aria-label", "Razširi");
      descriptionCol.setAttribute("aria-hidden", "true");
      descriptionCol.setAttribute("hidden", "until-found");
    }

    descriptionCol.addEventListener("beforematch", function () {
      expandDescription();
    });

    button.addEventListener("click", function () {
      const isExpanded = statusEl.classList.contains("expanded");
      if (isExpanded) {
        collapseDescription();
      } else {
        expandDescription();
      }
    });

    statusEl.addEventListener("click", function (event) {
      const closestButton = event.target.closest(".expand-button");
      const isExpanded = statusEl.classList.contains("expanded");
      if (closestButton === button || isExpanded) {
        return;
      }
      expandDescription();
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
