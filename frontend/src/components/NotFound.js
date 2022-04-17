import {useLocation} from "react-router-dom";

const NotFound = () => {
    let location = useLocation()
    return (
        <div>
            Page "{location.pathname}" not found
        </div>
    )
}

export default NotFound