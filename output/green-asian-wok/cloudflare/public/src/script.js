/* Plain JavaScript. No framework, runtime dependencies, or customer data storage. */
(function () {
  "use strict";
  const ORDER_URL = "https://www.greenasianwok.ie/shopDetail?rId=3238";
  const SIDES = Object.freeze([
    { id: "boiled-rice", name: "Boiled Rice", cents: 60 },
    { id: "chips", name: "Chips", cents: 60 },
    { id: "fried-rice", name: "Fried Rice", cents: 100 },
    { id: "fried-noodles", name: "Fried Noodles", cents: 200 },
  ]);
  const DISHES = Object.freeze([
    {
      id: "sweet-sour",
      name: "Sweet & Sour Chicken",
      category: "mains",
      cents: 1100,
      description: "Hong Kong style.",
      allergens: ["Gluten", "Eggs", "Sesame seeds"],
      image: "./assets/photos/sweet-sour.webp",
      requiresSide: true,
    },
    {
      id: "salt-chilli",
      name: "Salt & Chilli Chicken Strips",
      category: "starters",
      cents: 680,
      description: "Crispy chicken strips. Spicy.",
      allergens: ["Gluten", "Eggs", "Sesame seeds", "Sulphur dioxide"],
      image: "./assets/photos/salt-chilli.webp",
      requiresSide: false,
    },
    {
      id: "gyoza",
      name: "Deep Fried Chicken Gyoza",
      category: "starters",
      cents: 780,
      description: "With teriyaki sauce. Japanese style.",
      allergens: ["Gluten", "Eggs", "Peanuts", "Soya", "Milk"],
      requiresSide: false,
    },
  ]);
  function money(cents) {
    if (!Number.isSafeInteger(cents) || cents < 0)
      throw new RangeError("Price must be non-negative integer cents.");
    return new Intl.NumberFormat("en-IE", {
      style: "currency",
      currency: "EUR",
    }).format(cents / 100);
  }
  function filterDishes(query = "", category = "all") {
    const words = query
      .trim()
      .toLocaleLowerCase("en-IE")
      .split(/\s+/)
      .filter(Boolean);
    return DISHES.filter(
      (dish) =>
        (category === "all" || dish.category === category) &&
        words.every((word) =>
          `${dish.name} ${dish.description}`
            .toLocaleLowerCase("en-IE")
            .includes(word),
        ),
    );
  }
  function dishTotal(dishId, sideId) {
    const dish = DISHES.find((item) => item.id === dishId);
    if (!dish) throw new RangeError("Unknown dish.");
    const side = SIDES.find((item) => item.id === sideId);
    if (sideId && (!side || !dish.requiresSide))
      throw new RangeError("Invalid side for this dish.");
    return {
      cents: dish.cents + (side?.cents || 0),
      ready: !dish.requiresSide || Boolean(side),
    };
  }
  function escapeText(value) {
    return String(value).replace(
      /[&<>"']/g,
      (character) =>
        ({
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
        })[character],
    );
  }
  // Expose only pure menu logic to Node tests. Browser execution stays independent.
  if (typeof module !== "undefined" && module.exports)
    module.exports = {
      money,
      filterDishes,
      dishTotal,
      escapeText,
      DISHES,
      SIDES,
      ORDER_URL,
    };
  if (typeof document === "undefined") return;

  const menuDialog = document.getElementById("menu-dialog");
  const locationDialog = document.getElementById("location-dialog");
  const menuView = document.getElementById("menu-view");
  const dishView = document.getElementById("dish-view");
  const search = document.getElementById("menu-search");
  const results = document.getElementById("menu-results");
  const back = document.getElementById("back-menu");
  let category = "all";
  let selectedDish = null;
  let returnToMenu = false;
  let returnFocus = null;

  function openDialog(dialog, trigger) {
    returnFocus = trigger || document.activeElement;
    dialog.showModal();
  }
  function showMenu() {
    selectedDish = null;
    dishView.hidden = true;
    menuView.hidden = false;
    back.hidden = true;
    menuDialog.setAttribute("aria-labelledby", "menu-title");
    renderMenu();
  }
  function renderMenu() {
    const matches = filterDishes(search.value, category);
    results.innerHTML = matches
      .map(
        (dish) =>
          `<button class="menu-row" type="button" data-dish="${dish.id}"><span class="menu-row-copy"><span class="menu-row-name">${escapeText(dish.name)}</span><span class="menu-row-description">${escapeText(dish.description)}</span></span><span class="menu-row-price">${money(dish.cents)}</span><img class="icon" src="./assets/icons/arrow-right.svg" alt="" /></button>`,
      )
      .join("");
    document.getElementById("menu-empty").hidden = matches.length > 0;
    document.getElementById("results-count").textContent =
      `${matches.length} ${matches.length === 1 ? "dish" : "dishes"} found`;
  }
  function showDish(id, trigger) {
    selectedDish = DISHES.find((dish) => dish.id === id);
    if (!selectedDish) return;
    returnToMenu = menuDialog.open;
    if (!menuDialog.open) openDialog(menuDialog, trigger);
    const dish = selectedDish;
    menuView.hidden = true;
    dishView.hidden = false;
    back.hidden = !returnToMenu;
    menuDialog.setAttribute("aria-labelledby", "detail-title");
    dishView.innerHTML = `${dish.image ? `<img class="detail-photo" src="${dish.image}" alt="${escapeText(dish.name)}" />` : ""}
      <h2 id="detail-title" class="detail-title" tabindex="-1">${escapeText(dish.name)}</h2>
      <p class="detail-description">${escapeText(dish.description)}</p>
      <p class="allergens"><strong>Contains:</strong> ${dish.allergens.map(escapeText).join(", ")}.</p>
      <form id="dish-form">${dish.requiresSide ? `<fieldset class="side-options"><legend>Choose your side</legend><p class="required-copy" id="side-help">Choose one side to see your total and continue.</p>${SIDES.map((side) => `<label class="side-option"><input type="radio" name="side" value="${side.id}" required aria-describedby="side-help" /><span>${side.name}</span><span class="side-option-price">+${money(side.cents)}</span></label>`).join("")}</fieldset>` : ""}
      <div class="price-total"><span>${dish.requiresSide ? "Dish + selected side" : "Dish price"}</span><output id="dish-total" aria-live="polite">${money(dish.cents)}</output></div>
      <button class="button continue-order" type="submit" ${dish.requiresSide ? "disabled" : ""}>Continue to order <img class="icon dark-icon" src="./assets/icons/arrow-right.svg" alt="" /></button>
      <p class="handoff-note">You’ll select your dish and pay on our official ordering page. Prices and availability are confirmed there. For allergies, please check with the restaurant before ordering.</p></form>`;
    menuDialog.scrollTop = 0;
    document.getElementById("detail-title").focus({ preventScroll: true });
  }
  document.addEventListener("click", (event) => {
    const menuTrigger = event.target.closest("[data-open-menu]");
    const locationTrigger = event.target.closest("[data-open-location]");
    const dishTrigger = event.target.closest("[data-dish]");
    if (menuTrigger) {
      showMenu();
      openDialog(menuDialog, menuTrigger);
      search.focus();
    }
    if (locationTrigger) openDialog(locationDialog, locationTrigger);
    if (dishTrigger) showDish(dishTrigger.dataset.dish, dishTrigger);
    if (event.target.closest(".close-dialog"))
      event.target.closest("dialog").close();
    const filter = event.target.closest("[data-category]");
    if (filter) {
      category = filter.dataset.category;
      document
        .querySelectorAll("[data-category]")
        .forEach((button) =>
          button.setAttribute("aria-pressed", String(button === filter)),
        );
      renderMenu();
    }
  });
  search.addEventListener("input", renderMenu);
  document.getElementById("reset-search").addEventListener("click", () => {
    search.value = "";
    category = "all";
    document
      .querySelectorAll("[data-category]")
      .forEach((button) =>
        button.setAttribute(
          "aria-pressed",
          String(button.dataset.category === "all"),
        ),
      );
    renderMenu();
    search.focus();
  });
  back.addEventListener("click", () => {
    const id = selectedDish?.id;
    showMenu();
    const previous = results.querySelector(`[data-dish="${id}"]`);
    (previous || search).focus();
  });
  dishView.addEventListener("change", (event) => {
    if (!event.target.matches('input[name="side"]')) return;
    const total = dishTotal(selectedDish.id, event.target.value);
    document.getElementById("dish-total").textContent = money(total.cents);
    dishView.querySelector(".continue-order").disabled = !total.ready;
  });
  dishView.addEventListener("submit", (event) => {
    event.preventDefault();
    const side = dishView.querySelector('input[name="side"]:checked')?.value;
    const total = dishTotal(selectedDish.id, side);
    if (total.ready && event.target.reportValidity())
      window.location.assign(ORDER_URL);
  });
  [menuDialog, locationDialog].forEach((dialog) => {
    dialog.addEventListener("close", () => {
      if (returnFocus?.isConnected) returnFocus.focus({ preventScroll: true });
    });
    dialog.addEventListener("click", (event) => {
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (
        event.clientX < rect.left ||
        event.clientX > rect.right ||
        event.clientY < rect.top ||
        event.clientY > rect.bottom
      )
        dialog.close();
    });
  });
  renderMenu();
})();
