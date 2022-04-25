import {useParams, Link} from "react-router-dom";

const UserDetail = ({users}) => {
    let {id} = useParams();
    const user = users.find((u) => u.id === Number(id));
    return(
        <div>
            <div>ID: {user.id}</div>
            <div>Name: {user.username}</div>
            <div>Repo: {user.first_name}</div>
            <div>Desc: {user.last_name}</div>
            <div>Desc: {user.email}</div>
            <div>Desc: {user.phone_number}</div>
        </div>
    )
}
export default UserDetail