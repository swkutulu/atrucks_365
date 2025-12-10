import { fetchBaseQuery, retry } from '@reduxjs/toolkit/query/react';
import Cookies from 'js-cookie';
import { CONSTS } from '@/constants';


export const baseQuery = fetchBaseQuery({
    baseUrl: CONSTS.BASE_API_URL,
    credentials: 'include',
    mode: 'cors',
    prepareHeaders: (headers, { getState }) => {
        // const token = (getState() as RootState).auth.token;
        // if (token) {
        //     headers.set('authorization', `Token ${token}`);
        //     // headers.set('authorization', `Session ${token}`);
        //     // headers.set('authentication', `Bearer ${token}`);
        // }
        const csrftoken = Cookies.get(CONSTS.CSRFTOKEN_NAME);
        if (csrftoken) headers.set(`X-${CONSTS.CSRFTOKEN_NAME}`, csrftoken);
        // const session_id = Cookies.get(CONSTS.SESSIONID_NAME);
        // if (session_id) headers.set(CONSTS.SESSIONID_NAME, session_id);
        
        return headers;
    },
});

export const baseQueryWithRetry = retry(baseQuery, { maxRetries: CONSTS.MAX_RETRY_CNT });
