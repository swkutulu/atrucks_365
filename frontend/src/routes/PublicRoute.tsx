import { type ReactNode, Suspense } from 'react';
import { Navigate } from 'react-router-dom';
import { ErrorBoundary } from '@/components/error/ErrorBoundary';
import { Loading } from '@/components/loading';
import { URLS } from '@/constants';
import { useAppSelector } from '@/store';


type Props = {
    children: ReactNode;
};

type PropsState = {
    text?: string;
};

function ErrorState(props: PropsState) {
    const { text = 'An internal error occurred on the server' } = props;

    return <div>{text}</div>;
}


function PublicRoute(props: Props) {
    const { children } = props;
    const { isAuthenticated } = useAppSelector((state) => state.auth);

    if (isAuthenticated) {
        return <Navigate to={URLS.HOME} />;
    }

    return (
        <ErrorBoundary fallback={<ErrorState text="An error occurred in the application." />}>
            {/* {children} */}
            <Suspense fallback={<Loading />}>{children}</Suspense>
        </ErrorBoundary>
    );
}

export default PublicRoute;
