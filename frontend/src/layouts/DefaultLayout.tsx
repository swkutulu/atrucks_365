import { Outlet } from 'react-router-dom';
import { AppHeader } from '@/components/header';
import { AppFooter } from '@/components/footer';
import { ScrollTop } from 'primereact/scrolltop';
import './Layouts.scss';


export const DefaultLayout = () => {
    return (
        <main className="layout-default">
            {/* <AppHeader /> */}
            <div className="layout-children">
                <Outlet />
            </div>
            <AppFooter />
            <ScrollTop className="bottom-8!" />
        </main>
    );
};
