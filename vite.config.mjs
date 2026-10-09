import { defineConfig } from "vite";

export default defineConfig({
  server: {
    watch: {
      // Détecte aussi les sauvegardes atomiques et les fichiers synchronisés.
      useFsEvents: false,
      usePolling: true,
      interval: 150,
    },
  },
});
