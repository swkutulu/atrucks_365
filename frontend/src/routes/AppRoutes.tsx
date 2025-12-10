import { lazy, Suspense } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router';
import { URLS } from '@/constants';
import { SimpleLayout } from '@/layouts/SimpleLayout';
import { DefaultLayout } from '@/layouts/DefaultLayout';
import { LoadingFull } from '@/components/loading';
import PrivateRoute from './PrivateRoute';
import PublicRoute from './PublicRoute';

const NotFound = lazy(() => import('@/components/error/404'));
const PhoneItem = lazy(() => import('../components/phone/PhoneItem'));

export const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Suspense fallback={<LoadingFull />}>
                <Routes>
                    <Route path="/" element={<DefaultLayout />}>
                        <Route
                            index
                            path={URLS.HOME}
                            element={
                                <PrivateRoute redirectTo={URLS.LOGIN}>
                                    <PhoneItem />
                                </PrivateRoute>
                            }
                        />
                    </Route>
                </Routes>
            </Suspense>
        </BrowserRouter>
    );
};
