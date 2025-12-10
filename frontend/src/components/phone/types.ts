import React from "react";

export class TypePhone implements Phone{
    id: number = 0;
    status: number = 0;
}

export interface PhonePayoutPanelProps {
    title: string;
    children: React.ReactNode | React.ReactNode[];
};

// export interface PayoutContext {
//     payout: Payout;
//     formState: Payout;
//     setFormState: React.Dispatch<React.SetStateAction<Payout>>;
//     statuses: PayoutStatus[];
//     currencies: Currency[];
//     onCreateMain: () => void;
//     onEditMain: () => void;
//     onCancelMain: () => void;
//     onUpdateMain: () => void;
//     handleSubmit: (ev: React.FormEvent<HTMLFormElement>) => void;
//     errors: ApiError | undefined;
// }
