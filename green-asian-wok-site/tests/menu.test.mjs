import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import vm from "node:vm";
const context = { module: { exports: {} }, Intl };
vm.runInNewContext(
  readFileSync(new URL("../src/script.js", import.meta.url), "utf8"),
  context,
);
const { money, filterDishes, dishTotal, escapeText, DISHES, SIDES, ORDER_URL } =
  context.module.exports;
test("EUR formatting preserves integer cents", () => {
  assert.equal(money(680), "€6.80");
  assert.equal(money(1160), "€11.60");
  assert.equal(money(0), "€0.00");
  for (const value of [-1, 1.5, Infinity, NaN, "1100"])
    assert.throws(() => money(value));
});
test("search handles spaces, case, multiple words and no results", () => {
  assert.equal(filterDishes("  SWEET   chicken  ")[0].id, "sweet-sour");
  assert.equal(filterDishes("teriyaki")[0].id, "gyoza");
  assert.equal(filterDishes("unavailable dish").length, 0);
  assert.equal(filterDishes("").length, 3);
});
test("category and search intersect without losing the query", () => {
  assert.equal(filterDishes("chicken", "mains").length, 1);
  assert.equal(filterDishes("chicken", "starters").length, 2);
  assert.equal(filterDishes("sweet", "starters").length, 0);
});
test("required side gates continuation and each option updates the correct total", () => {
  assert.equal(dishTotal("sweet-sour").ready, false);
  assert.equal(dishTotal("sweet-sour").cents, 1100);
  for (const side of SIDES) {
    const total = dishTotal("sweet-sour", side.id);
    assert.equal(total.ready, true);
    assert.equal(total.cents, 1100 + side.cents);
  }
  assert.equal(dishTotal("salt-chilli").ready, true);
  assert.equal(dishTotal("salt-chilli").cents, 680);
  assert.throws(() => dishTotal("missing"));
  assert.throws(() => dishTotal("sweet-sour", "missing"));
  assert.throws(() => dishTotal("salt-chilli", "chips"));
});
test("rendered text cannot become markup", () => {
  assert.equal(
    escapeText('<img onerror="x">&\''),
    "&lt;img onerror=&quot;x&quot;&gt;&amp;&#39;",
  );
});
test("verified menu records keep allergens and a real provider handoff", () => {
  assert.equal(DISHES.find((dish) => dish.id === "gyoza").cents, 780);
  assert.ok(DISHES.every((dish) => dish.allergens.length > 0));
  assert.equal(new URL(ORDER_URL).hostname, "www.greenasianwok.ie");
  assert.equal(new URL(ORDER_URL).searchParams.get("rId"), "3238");
});
test("all referenced local HTML and CSS assets exist", () => {
  const html = readFileSync(new URL("../index.html", import.meta.url), "utf8");
  for (const match of html.matchAll(/(?:src|href)="(\.\/[^"#]+)"/g)) {
    assert.ok(existsSync(new URL("../" + match[1], import.meta.url)), match[1]);
  }
  const css = readFileSync(
    new URL("../src/style.css", import.meta.url),
    "utf8",
  );
  for (const match of css.matchAll(/url\(["']([^"']+)["']\)/g))
    assert.ok(
      existsSync(new URL("../src/" + match[1], import.meta.url)),
      match[1],
    );
});
