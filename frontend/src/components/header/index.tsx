import { useState, useEffect } from 'react';
import { NavLink, Link, useNavigate } from 'react-router-dom';
import { InputText } from 'primereact/inputtext';
import { IconField } from 'primereact/iconfield';
import { InputIcon } from 'primereact/inputicon';
import { URLS } from '@/constants';
import { useAppDispatch, useAppSelector } from '@/store';

import Logo from '@/assets/images/logo.svg';
import './Header.scss';

export const AppHeader = () => {
    const navigate = useNavigate();
    const [isFixed, setIsFixed] = useState(false);
    // const { isAuthenticated } = useAppSelector((state) => state.auth);
    const isAuthenticated = true;
    const dispatch = useAppDispatch();

    useEffect(() => {
        const handleScroll = () => {
            if (window.pageYOffset > 100) {
                setIsFixed(true);
            } else {
                setIsFixed(false);
            }
        };

        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    });

    const roundedBox = 'flex items-center justify-start bg-header p-5 gap-7 rounded-full h-[78px]';
    const headerClasses =
        'flex items-center justify-end gap-5 p-2 transition-width transition-opacity duration-500 ease-in-out will-change-auto';
    const headerClassesFixed = `${headerClasses} is-fixed fixed right-0 opacity-40 hover:opacity-100`;
    
    const doLogout = async () => {
        // await dispatch(userLogout());
        // navigate(URLS.LOGIN);
    }
    return (
        <header className={isFixed ? headerClassesFixed : headerClasses}>
            <div className={roundedBox}>
                <Link to={URLS.HOME} className="logo mr-7">
                    <img src={Logo} className="h-[1.2rem]" />
                </Link>
                {isAuthenticated ? (
                    <>
                        <NavLink to={URLS.PAYOUTS} className={'text-primary! hover:text-primary-600! hide-fixed'}>
                            Payouts
                        </NavLink>
                        <button className="cursor-pointer text-primary hover:text-primary-600 hide-fixed">
                            <a onClick={() => doLogout()}>
                                <i className="pi pi-sign-out text-2xl"></i>
                            </a>
                        </button>
                    </>
                ) : (
                    <>
                    <button className="cursor-pointer text-primary hover:text-primary-600 hide-fixed">
                        <Link to={URLS.LOGIN}>
                            <i className="pi pi-user text-2xl"></i>
                        </Link>
                    </button>
                    </>
                )}
            </div>
        </header>
    );
};
