import { toastRef } from '@/utils/toastRef';


// export const ErrorStatus = ({ error }: { error: {status: number, data: {detail: string}} }) => {
export const ErrorStatus = ({ error }) => {
    if(toastRef.current)
        toastRef.current.show({
            severity: 'error',
            summary: 'Ошибка ' + error.status,
            detail: error.data.detail,
            life: 3000,
        });
    else console.error(error);
    return null;
};