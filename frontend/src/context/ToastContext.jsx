import {

    createContext,

    useContext

} from "react";

import toast from "react-hot-toast";


const ToastContext = createContext();


export function ToastProvider({

    children
}) {

    // ======================================
    // SUCCESS TOAST
    // ======================================

    const successToast = (message) => {

        toast.success(message, {

            duration: 3000,

            style: {

                background: "#16a34a",

                color: "#fff",

                padding: "16px",

                borderRadius: "12px"
            }
        });
    };


    // ======================================
    // ERROR TOAST
    // ======================================

    const errorToast = (message) => {

        toast.error(message, {

            duration: 3000,

            style: {

                background: "#dc2626",

                color: "#fff",

                padding: "16px",

                borderRadius: "12px"
            }
        });
    };


    // ======================================
    // WARNING TOAST
    // ======================================

    const warningToast = (message) => {

        toast(message, {

            duration: 3000,

            icon: "⚠️",

            style: {

                background: "#ca8a04",

                color: "#fff",

                padding: "16px",

                borderRadius: "12px"
            }
        });
    };


    return (

        <ToastContext.Provider
            value={{

                successToast,

                errorToast,

                warningToast
            }}
        >

            {children}

        </ToastContext.Provider>
    );
}


export function useToast() {

    return useContext(ToastContext);
}