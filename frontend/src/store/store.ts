import { type TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';
import { configureStore, type ConfigureStoreOptions } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/query';

import { phoneSlice } from '../components/phone/phone.slice';
import { apiPhone } from '../components/phone/phone.api';


export const createStore = (options?: ConfigureStoreOptions['preloadedState'] | undefined) =>
    configureStore({
        reducer: {
            // auth: authSlice.reducer,
            phone: phoneSlice.reducer,
            // [apiAuth.reducerPath]: apiAuth.reducer,
            [apiPhone.reducerPath]: apiPhone.reducer,
        },
        middleware: (getDefaultMiddleware) =>
            getDefaultMiddleware().concat(
                // apiAuth.middleware,
                apiPhone.middleware
            ),
        ...options,
    });

export const store = createStore();
export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

setupListeners(store.dispatch);
