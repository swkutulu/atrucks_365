const prefix = import.meta.env.VITE_COOKIE_AUTH_PREFIX || '';

export const CONSTS = {
    BASE_API_URL: import.meta.env.VITE_BASE_API_URL || 'http://localhost:9200/api/v1',
    COOKIE_EXPIRATION_TIME: 60 * 60 * 24, // 1 day
    TOKEN_COOKIE: `${prefix}auth.token`,
    REFRESH_TOKEN_COOKIE: `${prefix}.auth.refreshToken`,
    CSRFTOKEN_NAME: import.meta.env.VITE_CSRFTOKEN_NAME || 'csrftoken',
    SESSIONID_NAME: import.meta.env.VITE_SESSIONID_NAME || 'sessionid',
    MAX_RETRY_CNT: import.meta.env.VITE_MAX_RETRY_CNT || 2,
    PAGE_SIZE: import.meta.env.VITE_PAGE_SIZE || 50,
};
