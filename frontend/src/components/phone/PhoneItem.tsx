import { useEffect, useState } from 'react';
import { useParams, useSearchParams, useNavigate } from 'react-router';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputMask } from 'primereact/inputmask';
import { apiPhone, useGetInfoQuery, useGetPhoneQuery } from './phone.api';
import { Loading } from '@/components/loading';
import { ResultsHandler } from '@/utils/resultsHandler';
import { Panel } from 'primereact/panel';
import { Button } from 'primereact/button';
// import { usePayoutContext } from './Phone.Context';
// import { PayoutContextProvider } from './Phone.ContextProvider';
// import * as forms from './PhoneForms';
// import { TypePhone } from './types';
import { URLS } from '@/constants';
import { useAppDispatch } from '@/store';
import { t } from '@/i18n';
import './Phone.scss';
import { get } from 'http';

const classBlock = 'rounded shadow-sm shadow-teal-800/5 p-7 mt-5 mb-5';

const PhoneItem = () => {
    return (
        <>
            <div className="mx-auto w-4xl first:mt-0 bg-(--color-bg-form)">
                <div className={classBlock}>
                    <h1>{t('header_phone')}</h1>
                </div>
            </div>
            <PhoneSearch />
            <DownloadInfo />
        </>
    );
};

const PhoneSearch = () => {
    const [phone, setPhone] = useState<string>();
    const [foundPhone, setFoundPhone] = useState();
    const [error, setError] = useState();
    const dispatch = useAppDispatch();
    const clearPhone = () => {
        setPhone('');
        setFoundPhone(null);
    };
    const searchPhone = async () => {
        if (phone) {
            const ph = phone.replaceAll('-', '');
            const { data: res, isError, error } = await dispatch(apiPhone.endpoints.getPhone.initiate({ phone: ph }));
            if(isError) {
                setError(error);
                setFoundPhone(null);
            }
            else{
                setFoundPhone(res);
                setError(null);
            }
        }
    };
    const getOperator = (rowData) => {
        return rowData.opsos?.name;
    };
    const getTerritory = (rowData) => {
        return rowData.territory?.name.split('|').map((item) => {
            return <p>{item}</p>
        })
    };
    const getRange = (rowData) => {
        return (
            <>
                <div>
                    {String(rowData.num_min).replace(rowData.num_prefix, '')} -{' '}
                    {String(rowData.num_max).replace(rowData.num_prefix, '')}{' '}
                </div>
                <div className="text-neutral-400">Номеров: {rowData.capacity}</div>
            </>
        );
    };

    const getError = () => {
        if(error?.status === 404) 
            return (<div className="text-neutral-400 text-center">{t('phone_not_found')}</div>);
    };

    const getSuccess = () => {
        return (
            <DataTable
                className="*:text-[14px] *:align-top!"
                showGridlines
                stripedRows
                value={foundPhone}
                size="small"
                tableStyle={{ width: '100%', minWidth: '50rem' }}
            >
                <Column className="align-top" field="num_prefix" header={t('prefix')}></Column>
                {/* <Column field="num_min" header={t('num_min')}></Column>
                    <Column field="num_max" header={t('num_max')} ></Column>
                    <Column field="capacity" header={t('capacity')} ></Column> */}
                <Column className="align-top" field="range" header={t('range')} body={getRange}></Column>
                <Column className="align-top" field="opsos" header={t('operator')} body={getOperator}></Column>
                <Column className="align-top" field="inn" header={t('inn')}></Column>
                <Column className="align-top" field="territory" header={t('territory')} body={getTerritory}></Column>
            </DataTable>
        );
    };

    return (
        <div className="mx-auto w-4xl first:mt-0 bg-(--color-bg-form)">
            <div className={classBlock}>
                <h2>{t('search_phone')}</h2>
                <div className="flex gap-5 justify-between">
                    <InputMask
                        className="grow"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        mask="999-999-99-99"
                        slotChar="XXX-XXX-XX-XX"
                        placeholder="999-999-99-99"
                    />
                    <Button label={t('search')} onClick={searchPhone} />
                    <Button label={t('clear')} severity="secondary" onClick={clearPhone} />
                </div>
            </div>
            <div className={classBlock + ' min-h-[200px]'}>{foundPhone ? getSuccess() : getError()}</div>
        </div>
    );
};

const DownloadInfo = () => {
    const resultsHandler = new ResultsHandler();
    const { data: info } = resultsHandler.handleResults(useGetInfoQuery({}, { pollingInterval: 0 }));
    if (resultsHandler.getIsBusy()) return <Loading />;

    return (
        <div className="mx-auto w-4xl first:mt-0 bg-(--color-bg-form)">
            <div className={classBlock}>
                <h3>{t('downloaded_info')}</h3>
                <DataTable
                    className="*:text-[12px]!"
                    showGridlines
                    stripedRows
                    value={info}
                    size="small"
                    tableStyle={{ width: '100%', minWidth: '50rem' }}
                >
                    <Column field="name" header={t('file_name')}></Column>
                    <Column field="is_added" header={t('is_added')}></Column>
                    <Column field="is_downloaded" header={t('is_downloaded')}></Column>
                    <Column field="retry_count" header={t('retry_count')}></Column>
                    <Column field="updated_at" header={t('updated_at')}></Column>
                    <Column field="status_message" header={t('status_message')}></Column>
                </DataTable>
            </div>
        </div>
    );
};
export default PhoneItem;
