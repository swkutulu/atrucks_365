import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite';
import viteCompression from 'vite-plugin-compression';
import path from 'path';

export default defineConfig(({ mode }) => {
    // Load env file based on `mode` in the current working directory.
    // Set the third parameter to '' to load all env regardless of the
    // `VITE_` prefix.
    const env = loadEnv(mode, process.cwd(), '');
    return {
        plugins: [
            react(),
            tailwindcss(),
            // viteCompression({
            //     algorithm: 'gzip', // You can also use 'brotliCompress' for Brotli compression
            //     // Other options:
            //     deleteOriginFile: true,
            //     // ext: '.gz', // Extension for compressed files
            // }),
        ],
        define: {
            __APP_ENV__: JSON.stringify(env.VITE_APP_ENV),
        },
        server: {
            port: env.VITE_APP_PORT ? Number(env.VITE_APP_PORT) : 5173,
        },
        resolve: {
            alias: {
                '@': path.resolve(__dirname, './src'),
                '@components': path.resolve(__dirname, './src/components'),
            },
        },
         build: {
            sourcemap: true, // or 'inline' or 'hidden' or true
            rollupOptions: {
                output: {
                    manualChunks(id: any) {
                        if (id.includes("node_modules")) {
                            return id.toString().split("node_modules/")[1].split("/")[0].toString();
                        }
                    },
                },
            },
        },
    };
});

// npx vite-bundle-visualizer