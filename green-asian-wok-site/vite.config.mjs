import { defineConfig } from "vite";

export default defineConfig({
  build: {
    outDir: "dist/client",
  },
  base: "./",
  server: {
    host: "0.0.0.0",
    allowedHosts: ["terminal.local"],
  },
});
