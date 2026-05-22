import {

    createContext,

    useContext,

    useEffect,

    useState

} from "react";


const ThemeContext = createContext();


export function ThemeProvider({

    children
}) {

    const [darkMode, setDarkMode] = useState(

        localStorage.getItem("theme") === "dark"
    );


    useEffect(() => {

        const root = window.document.documentElement;

        if (darkMode) {

            root.classList.add("dark");
        }

        else {

            root.classList.remove("dark");
        }

    }, [darkMode]);


    const toggleTheme = () => {

        const newTheme = !darkMode;

        setDarkMode(newTheme);

        localStorage.setItem(

            "theme",

            newTheme ? "dark" : "light"
        );
    };


    return (

        <ThemeContext.Provider
            value={{

                darkMode,

                toggleTheme
            }}
        >

            {children}

        </ThemeContext.Provider>
    );
}


export function useTheme() {

    return useContext(ThemeContext);
}