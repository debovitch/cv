import { defineConfig } from "vite";
import { readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL(".", import.meta.url));

export default defineConfig({
  build: {
    rolldownOptions: {
      // Chaque CV et le catalogue doivent rester accessibles après publication.
      input: Object.fromEntries(
        readdirSync(root)
          .filter((file) => file.endsWith(".html"))
          .map((file) => [file.replace(/\.html$/, ""), fileURLToPath(new URL(file, import.meta.url))]),
      ),
    },
  },
  server: {
    watch: {
      // Détecte aussi les sauvegardes atomiques et les fichiers synchronisés.
      useFsEvents: false,
      usePolling: true,
      interval: 150,
    },
  },
});
