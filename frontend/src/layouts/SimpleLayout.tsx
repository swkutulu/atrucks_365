import { Outlet } from 'react-router-dom';
import { AppFooter } from '@/components/footer';
import './Layouts.scss';

export const SimpleLayout = () => {
    return (
        <main className="layout-simple">
            <div className="layout-children">
                <Outlet />
            </div>
            <AppFooter />
        </main>
    );
};
