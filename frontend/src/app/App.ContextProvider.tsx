import React from 'react';
// import { useSearchParams } from 'react-router';
// import { Loading } from '@/components/loading';
import { AppContext } from './App.Context';

interface IAppContext{
    status: number
}

export const AppContextProvider = ({ children}: {children: React.ReactNode | React.ReactNode[]}) => {
    // const [searchParams, setSearchParams] = useSearchParams();
    const context: IAppContext = {
        status: 3
    };
 
    return (
        <AppContext.Provider value={context}>
            {children}
        </AppContext.Provider>
    );
};
