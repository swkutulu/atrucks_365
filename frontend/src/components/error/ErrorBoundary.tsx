import React, { type ReactNode } from 'react';

interface ErrorBoundaryProps {
    fallback: ReactNode;
    children: ReactNode;
    // state?: unknown;
}

// export const ErrorBoundary: React.FC<ErrorBoundaryProps> = ({ fallback, children }) => {
export const ErrorBoundary: React.FC<ErrorBoundaryProps> = (props) => {
    const { fallback, children } = props;

    // if (state.hasError) {
    //     return { fallback };
    // }

    return  children;
};

