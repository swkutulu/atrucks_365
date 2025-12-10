import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '@/store';

// const cachedTime = 60 * 30; // in seconds

export const apiPhone = createApi({
    reducerPath: 'apiPhone',
    baseQuery: baseQuery,
    tagTypes: ['Phones'],
    endpoints: (build) => ({
        getPhone: build.query({
            query: ({ phone }) => {
                return `/abcdef/phone-norm-search/${phone}/`;
            },
            keepUnusedDataFor: 0,
        }),
        getInfo: build.query({
            query: () => {
                return '/abcdef/info/';
            },
            keepUnusedDataFor: 0,
        }),
    }),
});

export const {
    useGetPhoneQuery,
    useGetInfoQuery,
} = apiPhone;
