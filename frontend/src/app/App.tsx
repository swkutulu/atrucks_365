import { Toast } from 'primereact/toast';
import { toastRef } from '@/utils/toastRef';
import { AppRoutes } from '@/routes';
// import { useEffect } from 'react';
import { AppContextProvider } from '@/app/App.ContextProvider';

const App = () => {
    return (
        <>
        <AppContextProvider>
            <Toast ref={toastRef} />
            <AppRoutes />
        </AppContextProvider>
        </>
    );
};
export default App;

