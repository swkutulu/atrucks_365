import React from 'react';
// import {type AppContext} from './types';

export const AppContext = React.createContext(undefined);
// export const Context = React.createContext<AppContext | undefined>(undefined);

export const useAppContext = () => {
    const context = React.useContext(AppContext);
    if (!context) throw new Error('Use app context within provider!');
    return context;
};
