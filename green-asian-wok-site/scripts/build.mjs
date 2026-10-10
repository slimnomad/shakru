// Static build: ship the exact HTML, CSS and JavaScript without a framework.
import { cpSync, mkdirSync, rmSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const output = path.join(root, "dist/client");
rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
for (const name of ["index.html", "assets", "src"]) {
  cpSync(path.join(root, name), path.join(output, name), { recursive: true });
}
console.log("Static HTML/CSS/JS built in dist/client.");
