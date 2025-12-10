import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from '@/store';
import { PrimeReactProvider } from 'primereact/api';
import App from '@/app/App';


import '@/assets/scss/theme.css'; // подключение tailwind и темы PrimeReact
import '@/assets/scss/index.scss'; // стили приложения

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <Provider store={store}>
            <PrimeReactProvider value={{ unstyled: false, }}>
                <App></App>
            </PrimeReactProvider>
        </Provider>
    </StrictMode>
);
