import { createSlice, type PayloadAction } from '@reduxjs/toolkit';

export const payouts = [] as Phone[];
export interface IStatePhone {
    loading: boolean;
    error: { msg?: string; status?: number };
    phone: Phone | null;
    phones: Phone[];
};

const initialState: IStatePhone = {
    loading: true,
    error: {},
    phone: null,
    phones: [],
};

export const phoneSlice = createSlice({
    name: 'phone',
    initialState,
    reducers: {

    } 
});

// export default payoutSlice.reducer;