import { type ReactNode, Suspense } from 'react';
import { Navigate } from 'react-router-dom';
import { ErrorBoundary } from '@/components/error/ErrorBoundary';
import { Loading } from '@/components/loading';
// import { useAppSelector } from '@/store';
import { URLS } from '@/constants';

type Props = {
    redirectTo?: string;
    children: ReactNode;
};

type PropsState = {
    text?: string;
};

function ErrorState(props: PropsState) {
    const { text = 'An internal error occurred on the server' } = props;
    return <div>{text}</div>;
}

const PrivateRoute = (props: Props) => {
    const { redirectTo = URLS.LOGIN, children } = props;
    // const { isAuthenticated } = useAppSelector((state) => state.auth);
    const isAuthenticated = true
    if (!isAuthenticated) {
        return <Navigate to={redirectTo} />;
    }
    return (
        <ErrorBoundary fallback={<ErrorState text="An error occurred in the application." />}>
            <Suspense fallback={<Loading />}>{children}</Suspense>
        </ErrorBoundary>
    );
}

export default PrivateRoute;
